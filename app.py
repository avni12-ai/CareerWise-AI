0"""
CareerWise AI - Flask Backend Server
Intelligent Career Guidance Expert System
Developed for AIES (Artificial Intelligence & Expert Systems)
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import json
import os
import uuid

from expert_system.knowledge_base import (
    CAREERS,
    SKILLS_METADATA,
    INTERESTS_METADATA,
    SUBJECTS_METADATA,
    WORK_STYLES_METADATA,
    PRODUCTION_RULES,
    PRESET_PROFILES
)
from expert_system.forward_chaining import ForwardChainingEngine
from expert_system.backward_chaining import BackwardChainingEngine
from expert_system.explanation import ExplanationFacility
from expert_system.roadmap_generator import RoadmapGenerator

app = Flask(__name__)
app.secret_key = "careerwise_expert_system_aies_secret_key"

# In-memory storage for assessment results to bypass 4KB cookie limitations
ASSESSMENT_CACHE = {}

# Instantiate inference engines and helper facilities
forward_engine = ForwardChainingEngine()
backward_engine = BackwardChainingEngine()
explanation_facility = ExplanationFacility()
roadmap_generator = RoadmapGenerator()


# ---------------------------------------------------------------------------
# PAGE ROUTES
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    """Landing page showcasing AIES architecture, project goals, and team information."""
    return render_template(
        "index.html",
        careers=CAREERS,
        total_rules=len(PRODUCTION_RULES),
        total_skills=len(SKILLS_METADATA),
        total_careers=len(CAREERS),
        active_tab="home"
    )


@app.route("/assessment")
def assessment():
    """Interactive assessment questionnaire."""
    # Organize skills by category for intuitive UX
    categories = {}
    for skill_id, meta in SKILLS_METADATA.items():
        cat = meta.get("category", "General")
        if cat not in categories:
            categories[cat] = []
        categories[cat].append({
            "id": skill_id,
            "name": meta["name"],
            "desc": meta["desc"]
        })

    return render_template(
        "assessment.html",
        skill_categories=categories,
        interests=INTERESTS_METADATA,
        subjects=SUBJECTS_METADATA,
        work_styles=WORK_STYLES_METADATA,
        presets=PRESET_PROFILES,
        active_tab="assessment"
    )


@app.route("/results")
def results():
    """Displays comprehensive recommendations, charts, and explanations."""
    sid = session.get("sid")
    assessment_data = ASSESSMENT_CACHE.get(sid) or ASSESSMENT_CACHE.get("latest")
    if not assessment_data:
        # If no assessment yet, redirect to assessment with message
        return redirect(url_for("assessment"))

    return render_template(
        "results.html",
        results=assessment_data["results"],
        student_name=assessment_data.get("student_name", "Student Candidate"),
        active_tab="results"
    )


@app.route("/backward-chain")
def backward_chain_page():
    """Goal-Driven Diagnostic interface."""
    return render_template(
        "backward_chain.html",
        careers=CAREERS,
        presets=PRESET_PROFILES,
        active_tab="backward_chain"
    )


@app.route("/what-if")
def what_if_page():
    """Real-Time What-If Analysis Simulator."""
    # Pass skills and interests metadata
    return render_template(
        "what_if.html",
        skills=SKILLS_METADATA,
        interests=INTERESTS_METADATA,
        presets=PRESET_PROFILES,
        active_tab="what_if"
    )


@app.route("/kb-explorer")
def kb_explorer():
    """Knowledge Base Inspector for college evaluators and viva examiners."""
    return render_template(
        "kb_explorer.html",
        rules=PRODUCTION_RULES,
        careers=CAREERS,
        skills=SKILLS_METADATA,
        interests=INTERESTS_METADATA,
        subjects=SUBJECTS_METADATA,
        active_tab="kb_explorer"
    )


@app.route("/printable-report")
def printable_report():
    """Render print-ready career guidance report."""
    sid = session.get("sid")
    assessment_data = ASSESSMENT_CACHE.get(sid) or ASSESSMENT_CACHE.get("latest")
    if not assessment_data:
        return redirect(url_for("assessment"))

    return render_template(
        "report_template.html",
        results=assessment_data["results"],
        student_name=assessment_data.get("student_name", "Student Candidate"),
        student_facts=assessment_data.get("student_facts", {})
    )


# ---------------------------------------------------------------------------
# REST API ENDPOINTS
# ---------------------------------------------------------------------------

@app.route("/api/assess", methods=["POST"])
def api_assess():
    """
    Main evaluation endpoint.
    Accepts student facts -> executes forward chaining -> attaches explanations and roadmaps.
    """
    data = request.get_json() or {}
    student_name = data.get("student_name", "Student Candidate")
    skills = data.get("skills", {})
    interests = data.get("interests", [])
    subjects = data.get("subjects", {})
    work_style = data.get("work_style", {})

    # Ensure integer values for skills
    cleaned_skills = {k: int(v) for k, v in skills.items()}

    student_facts = {
        "skills": cleaned_skills,
        "interests": interests,
        "subjects": subjects,
        "work_style": work_style
    }

    # 1. RUN FORWARD CHAINING INFERENCE
    inference_result = forward_engine.run_inference(student_facts)
    top_careers = inference_result["top_recommendations"]
    all_careers = inference_result["all_careers"]
    other_careers = inference_result["other_careers"]

    # 2. GENERATE EXPLANATIONS FOR TOP 3
    detailed_recommendations = []
    for rank, career_eval in enumerate(top_careers, 1):
        why_exp = explanation_facility.generate_why_explanation(career_eval, inference_result, student_facts)
        how_exp = explanation_facility.generate_how_explanation(career_eval, inference_result)
        roadmap = roadmap_generator.generate_roadmap_for_career(career_eval["career_id"], student_facts)

        detailed_recommendations.append({
            "rank": rank,
            "evaluation": career_eval,
            "why_explanation": why_exp,
            "how_explanation": how_exp,
            "roadmap": roadmap
        })

    # 3. GENERATE WHY NOT EXPLANATIONS FOR OTHER CAREERS
    why_not_list = []
    if top_careers:
        top_1 = top_careers[0]
        for oc in other_careers[:3]: # top 3 alternatives
            why_not_list.append(explanation_facility.generate_why_not_explanation(oc, top_1, student_facts))

    # 4. PREPARE CHART.JS DATA
    chart_data = explanation_facility.format_chart_data(top_careers, all_careers, student_facts)

    full_payload = {
        "top_recommendations": detailed_recommendations,
        "all_careers": all_careers,
        "why_not_explanations": why_not_list,
        "trace": inference_result["trace"],
        "student_summary": inference_result["student_summary"],
        "chart_data": chart_data
    }

    # Store in memory cache for results and print pages
    sid = session.get("sid")
    if not sid:
        sid = str(uuid.uuid4())
        session["sid"] = sid

    cached_entry = {
        "student_name": student_name,
        "student_facts": student_facts,
        "results": full_payload
    }
    ASSESSMENT_CACHE[sid] = cached_entry
    ASSESSMENT_CACHE["latest"] = cached_entry

    return jsonify({"success": True, "results": full_payload})


@app.route("/api/backward-chain", methods=["POST"])
def api_backward_chain():
    """
    Goal-driven evaluation endpoint.
    Accepts target_career_id and student facts -> runs backward chainer.
    """
    data = request.get_json() or {}
    target_career_id = data.get("target_career_id", "ai_ml_engineer")
    skills = data.get("skills", {})
    interests = data.get("interests", [])
    subjects = data.get("subjects", {})
    work_style = data.get("work_style", {})

    cleaned_skills = {k: int(v) for k, v in skills.items()}

    student_facts = {
        "skills": cleaned_skills,
        "interests": interests,
        "subjects": subjects,
        "work_style": work_style
    }

    diagnosis = backward_engine.diagnose_career_goal(target_career_id, student_facts)
    return jsonify({"success": True, "diagnosis": diagnosis})


@app.route("/api/presets", methods=["GET"])
def api_presets():
    """Returns preset test profiles for 1-click viva demonstrations."""
    return jsonify(PRESET_PROFILES)


@app.route("/api/preset/<profile_key>", methods=["GET"])
def api_get_preset(profile_key):
    """Retrieve a specific profile."""
    if profile_key in PRESET_PROFILES:
        return jsonify({"success": True, "profile": PRESET_PROFILES[profile_key]})
    return jsonify({"success": False, "error": "Profile not found"}), 404


@app.route("/api/what-if-simulate", methods=["POST"])
def api_what_if_simulate():
    """
    Fast simulation endpoint for real-time slider adjustments.
    """
    data = request.get_json() or {}
    skills = data.get("skills", {})
    interests = data.get("interests", [])
    subjects = data.get("subjects", {})
    work_style = data.get("work_style", {})

    cleaned_skills = {k: int(v) for k, v in skills.items()}
    student_facts = {
        "skills": cleaned_skills,
        "interests": interests,
        "subjects": subjects,
        "work_style": work_style
    }

    inference = forward_engine.run_inference(student_facts)
    return jsonify({
        "success": True,
        "top_3": inference["top_recommendations"],
        "all_careers": inference["all_careers"]
    })



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))

    print("============================================================")
    print("CareerWise AI: Intelligent  Guidance Expert System")
    print("Subject: Artificial Intelligence & Expert Systems (AIES)")
    print(f"Server launching on port: {port}")
    print("============================================================")

    app.run(host="0.0.0.0", port=port, debug=False)

    
