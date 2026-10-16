"""
CareerWise AI - Explanation Facility Module
Provides deep, transparent reasoning justifications:
1. "WHY": Justifies top recommended career paths
2. "HOW": Exposes exact inference execution steps and Certainty Factor accumulation
3. "WHY NOT": Explains why unrecommended careers failed or ranked lower
4. Prepares Chart.js data structures for radar and comparative bar charts
"""

from typing import Dict, List, Any
from expert_system.knowledge_base import (
    CAREERS,
    SKILLS_METADATA,
    INTERESTS_METADATA,
    SUBJECTS_METADATA
)


class ExplanationFacility:
    def __init__(self):
        self.careers = CAREERS

    def generate_why_explanation(self, career_eval: Dict[str, Any], inference_result: Dict[str, Any], student_facts: Dict[str, Any]) -> Dict[str, Any]:
        """
        Answers: 'WHY is this career recommended?'
        Identifies positive evidence, activated rules, and strongest skills.
        """
        cid = career_eval["career_id"]
        profile = self.careers[cid]
        student_skills = student_facts.get("skills", {})
        student_interests = set(student_facts.get("interests", []))

        # 1. Find all rules that fired in support of this career
        fired_rules_for_career = []
        for rule_trace in inference_result["trace"]["fired_rules"]:
            for aff in rule_trace["affected_careers"]:
                if aff["career_id"] == cid:
                    fired_rules_for_career.append({
                        "rule_id": rule_trace["rule_id"],
                        "rule_name": rule_trace["rule_name"],
                        "category": rule_trace["category"],
                        "rule_cf": aff["rule_cf"],
                        "explanation": rule_trace["explanation"]
                    })

        # 2. Key contributing strengths
        strong_skills = []
        for sk_id, benchmark in profile["core_skills"].items():
            lvl = student_skills.get(sk_id, 1)
            if lvl >= benchmark or lvl >= 4:
                strong_skills.append({
                    "skill_name": SKILLS_METADATA.get(sk_id, {}).get("name", sk_id),
                    "level": lvl,
                    "benchmark": benchmark
                })

        # 3. Matching interests
        matching_interests = [
            INTERESTS_METADATA.get(i, {}).get("name", i)
            for i in profile.get("recommended_interests", [])
            if i in student_interests
        ]

        # 4. Synthesize natural language justification
        summary_points = [
            f"Achieved a composite suitability score of {career_eval['composite_score']}% with a Certainty Factor of {career_eval['certainty_factor']} ({career_eval['certainty_pct']}%).",
            f"Fired {len(fired_rules_for_career)} production rules validating theoretical and practical competency.",
            f"Demonstrated {career_eval['skill_match_pct']}% alignment with industry-standard core skills, with standout mastery in {', '.join([s['skill_name'] for s in strong_skills[:3]]) if strong_skills else 'general technical areas'}."
        ]
        if matching_interests:
            summary_points.append(f"Strongly aligns with student's stated passion in: {', '.join(matching_interests)}.")

        return {
            "career_id": cid,
            "career_title": career_eval["title"],
            "summary_points": summary_points,
            "supporting_rules": fired_rules_for_career,
            "demonstrated_strengths": strong_skills,
            "matching_interests": matching_interests
        }

    def generate_how_explanation(self, career_eval: Dict[str, Any], inference_result: Dict[str, Any]) -> Dict[str, Any]:
        """
        Answers: 'HOW was this conclusion derived?'
        Exposes the exact mathematical and logical derivation steps.
        """
        cid = career_eval["career_id"]
        
        # Step-by-step CF updates
        derivation_steps = []
        running_cf = 0.0

        for r in inference_result["trace"]["fired_rules"]:
            for aff in r["affected_careers"]:
                if aff["career_id"] == cid:
                    rule_cf = aff["rule_cf"]
                    prior_cf = running_cf
                    running_cf = prior_cf + rule_cf * (1.0 - prior_cf)
                    derivation_steps.append({
                        "step": len(derivation_steps) + 1,
                        "rule_id": r["rule_id"],
                        "rule_name": r["rule_name"],
                        "formula": f"{prior_cf:.3f} + {rule_cf:.2f} * (1 - {prior_cf:.3f}) = {running_cf:.3f}",
                        "prior_cf": round(prior_cf, 3),
                        "rule_cf": rule_cf,
                        "posterior_cf": round(running_cf, 3)
                    })

        # Score composition breakdown
        score_breakdown = {
            "rules_contribution": round(0.40 * career_eval["certainty_pct"], 2),
            "skills_contribution": round(0.35 * career_eval["skill_match_pct"], 2),
            "academics_contribution": round(0.15 * career_eval["academic_match_pct"], 2),
            "interest_contribution": round(0.10 * career_eval["interest_match_pct"], 2),
            "total_composite_score": career_eval["composite_score"]
        }

        return {
            "career_id": cid,
            "derivation_steps": derivation_steps,
            "score_breakdown": score_breakdown
        }

    def generate_why_not_explanation(self, non_top_career: Dict[str, Any], top_career: Dict[str, Any], student_facts: Dict[str, Any]) -> Dict[str, Any]:
        """
        Answers: 'WHY was this career NOT ranked in the top 3?'
        Analyzes skill deficiencies, missing interests, and failed rules.
        """
        cid = non_top_career["career_id"]
        profile = self.careers[cid]
        student_skills = student_facts.get("skills", {})
        student_interests = set(student_facts.get("interests", []))

        # Deficits in core and critical skills
        deficits = []
        for sk_id, benchmark in profile["core_skills"].items():
            lvl = student_skills.get(sk_id, 1)
            if lvl < benchmark:
                gap = benchmark - lvl
                deficits.append({
                    "skill_name": SKILLS_METADATA.get(sk_id, {}).get("name", sk_id),
                    "current": lvl,
                    "benchmark": benchmark,
                    "gap": gap,
                    "is_critical": sk_id in profile.get("critical_skills", [])
                })

        # Unmatched interests
        missing_interests = [
            INTERESTS_METADATA.get(i, {}).get("name", i)
            for i in profile.get("recommended_interests", [])
            if i not in student_interests
        ]

        reasons = []
        critical_deficits = [d for d in deficits if d["is_critical"]]
        if critical_deficits:
            crit_names = [f"{d['skill_name']} (Lvl {d['current']}/{d['benchmark']})" for d in critical_deficits]
            reasons.append(f"Critical prerequisites below threshold: {', '.join(crit_names)}.")
        
        if non_top_career["certainty_pct"] < 50:
            reasons.append(f"Insufficient production rule activation (Certainty Factor was only {non_top_career['certainty_pct']}%).")
        
        if missing_interests:
            reasons.append(f"Lacked alignment with key interest areas: {', '.join(missing_interests[:2])}.")

        score_difference = round(top_career["composite_score"] - non_top_career["composite_score"], 1)

        return {
            "career_id": cid,
            "title": non_top_career["title"],
            "composite_score": non_top_career["composite_score"],
            "score_difference_from_rank_1": score_difference,
            "reasons": reasons,
            "top_deficits": sorted(deficits, key=lambda x: (x["is_critical"], x["gap"]), reverse=True)[:4],
            "missing_interests": missing_interests
        }

    def format_chart_data(self, top_careers: List[Dict[str, Any]], all_careers: List[Dict[str, Any]], student_facts: Dict[str, Any]) -> Dict[str, Any]:
        """
        Formats visual data arrays for Chart.js:
        1. Radar Chart: Student vs Benchmark for Top 1 Career
        2. Comparison Bar Chart: All Careers Composite vs CF
        """
        student_skills = student_facts.get("skills", {})
        top_1 = top_careers[0] if top_careers else None

        radar_data = None
        if top_1:
            cid = top_1["career_id"]
            core_skills = self.careers[cid]["core_skills"]
            labels = [SKILLS_METADATA.get(s, {}).get("name", s) for s in core_skills.keys()]
            student_vals = [student_skills.get(s, 1) for s in core_skills.keys()]
            benchmark_vals = [benchmark for benchmark in core_skills.values()]

            radar_data = {
                "labels": labels,
                "datasets": [
                    {
                        "label": "Your Assessed Level",
                        "data": student_vals,
                        "backgroundColor": "rgba(37, 99, 235, 0.25)",
                        "borderColor": "#2563eb",
                        "pointBackgroundColor": "#2563eb",
                        "borderWidth": 2
                    },
                    {
                        "label": f"{top_1['title']} Benchmark",
                        "data": benchmark_vals,
                        "backgroundColor": "rgba(220, 38, 38, 0.15)",
                        "borderColor": "#dc2626",
                        "pointBackgroundColor": "#dc2626",
                        "borderDash": [4, 4],
                        "borderWidth": 2
                    }
                ]
            }

        # Bar chart comparison of all careers
        bar_labels = [c["title"].split("/")[0].strip() for c in all_careers]
        composite_scores = [c["composite_score"] for c in all_careers]
        cf_percentages = [c["certainty_pct"] for c in all_careers]
        skill_percentages = [c["skill_match_pct"] for c in all_careers]

        bar_data = {
            "labels": bar_labels,
            "datasets": [
                {
                    "label": "Composite Suitability Score (%)",
                    "data": composite_scores,
                    "backgroundColor": "#2563eb",
                    "borderRadius": 6
                },
                {
                    "label": "Rule Certainty Factor (%)",
                    "data": cf_percentages,
                    "backgroundColor": "#7c3aed",
                    "borderRadius": 6
                },
                {
                    "label": "Skill Benchmark Match (%)",
                    "data": skill_percentages,
                    "backgroundColor": "#059669",
                    "borderRadius": 6
                }
            ]
        }

        return {
            "radar_top_1": radar_data,
            "bar_comparison": bar_data
        }
