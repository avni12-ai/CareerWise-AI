"""
CareerWise AI - Backward Chaining Inference Engine
Implements goal-driven reasoning for career eligibility & gap diagnosis:
1. Target Hypothesis formulation (Goal: "Student is qualified for Career X")
2. Rule decomposition into subgoals (Skills, Academics, Interests)
3. Subgoal verification against Working Memory (Leaf facts)
4. Detection of prerequisite deficits & critical blockers
5. Diagnostic verdict with remediation priorities
"""

from typing import Dict, List, Any
from expert_system.knowledge_base import (
    CAREERS,
    SKILLS_METADATA,
    INTERESTS_METADATA,
    SUBJECTS_METADATA,
    PRODUCTION_RULES
)
from expert_system.forward_chaining import GRADE_NUMERIC


class BackwardChainingEngine:
    def __init__(self):
        self.rules = PRODUCTION_RULES
        self.careers = CAREERS

    def diagnose_career_goal(self, target_career_id: str, student_facts: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes Goal-Driven Backward Chaining to evaluate student readiness for a specific career.
        """
        if target_career_id not in self.careers:
            return {"error": f"Career ID '{target_career_id}' not found in Knowledge Base"}

        target_profile = self.careers[target_career_id]
        target_title = target_profile["title"]
        core_skills = target_profile["core_skills"]
        critical_skills = set(target_profile.get("critical_skills", []))

        working_memory = student_facts.copy()
        student_skills = working_memory.get("skills", {})
        student_interests = set(working_memory.get("interests", []))
        student_subjects = working_memory.get("subjects", {})

        # 1. RETRIEVE ALL RULES WHOSE CONSEQUENT ASSERTS THIS TARGET CAREER
        applicable_rules = [
            rule for rule in self.rules
            if target_career_id in rule["consequent"]
        ]

        subgoal_verifications = []
        satisfied_rules_count = 0

        # Evaluate each supporting rule through backward decomposition
        for rule in applicable_rules:
            rule_id = rule["id"]
            rule_name = rule["name"]
            conditions = rule["conditions"]
            rule_cf = rule["consequent"][target_career_id]

            rule_subgoals = []
            rule_satisfied = True

            # Check Skill Antecedents
            if "skills" in conditions:
                for sk_id, (op, req_level) in conditions["skills"].items():
                    curr_level = student_skills.get(sk_id, 1)
                    sk_name = SKILLS_METADATA.get(sk_id, {}).get("name", sk_id)
                    is_met = curr_level >= req_level if op == ">=" else curr_level > req_level
                    if not is_met:
                        rule_satisfied = False
                    rule_subgoals.append({
                        "type": "Skill Prerequisite",
                        "name": sk_name,
                        "required": f">= Level {req_level}",
                        "current": f"Level {curr_level}",
                        "satisfied": is_met,
                        "gap": max(0, req_level - curr_level),
                        "is_critical": sk_id in critical_skills
                    })

            # Check Interest Antecedents
            if "interests" in conditions:
                for int_id in conditions["interests"]:
                    int_name = INTERESTS_METADATA.get(int_id, {}).get("name", int_id)
                    is_met = int_id in student_interests
                    if not is_met:
                        rule_satisfied = False
                    rule_subgoals.append({
                        "type": "Domain Interest",
                        "name": int_name,
                        "required": "Interested",
                        "current": "Interested" if is_met else "Not Selected",
                        "satisfied": is_met,
                        "gap": 0 if is_met else 1,
                        "is_critical": False
                    })

            # Check Subject Antecedents
            if "subjects" in conditions:
                for sub_id, (op, min_grade) in conditions["subjects"].items():
                    sub_name = SUBJECTS_METADATA.get(sub_id, {}).get("name", sub_id)
                    actual_grade = student_subjects.get(sub_id, "C")
                    actual_num = GRADE_NUMERIC.get(actual_grade, 1.5)
                    req_num = GRADE_NUMERIC.get(min_grade, 3.5)
                    is_met = actual_num >= req_num
                    if not is_met:
                        rule_satisfied = False
                    rule_subgoals.append({
                        "type": "Academic Subject",
                        "name": sub_name,
                        "required": f">= {min_grade}",
                        "current": actual_grade,
                        "satisfied": is_met,
                        "gap": 0 if is_met else 1,
                        "is_critical": False
                    })

            if rule_satisfied:
                satisfied_rules_count += 1

            subgoal_verifications.append({
                "rule_id": rule_id,
                "rule_name": rule_name,
                "rule_cf": rule_cf,
                "satisfied": rule_satisfied,
                "subgoals": rule_subgoals
            })

        # 2. COMPREHENSIVE SKILL GAP ANALYSIS AGAINST CAREER BENCHMARK
        skill_analysis = []
        blockers = []
        strengths = []
        total_benchmark_points = 0
        total_student_points = 0

        for sk_id, benchmark in core_skills.items():
            curr_lvl = student_skills.get(sk_id, 1)
            sk_name = SKILLS_METADATA.get(sk_id, {}).get("name", sk_id)
            is_crit = sk_id in critical_skills
            gap = max(0, benchmark - curr_lvl)

            total_benchmark_points += benchmark
            total_student_points += min(curr_lvl, benchmark)

            item = {
                "skill_id": sk_id,
                "skill_name": sk_name,
                "current_level": curr_lvl,
                "benchmark_level": benchmark,
                "gap": gap,
                "is_critical": is_crit,
                "status": "Mastered" if curr_lvl >= benchmark else ("Minor Gap" if gap == 1 else "Major Deficit")
            }
            skill_analysis.append(item)

            if gap > 0 and is_crit:
                blockers.append(item)
            elif curr_lvl >= benchmark:
                strengths.append(item)

        overall_readiness_pct = round((total_student_points / total_benchmark_points) * 100, 1) if total_benchmark_points > 0 else 0

        # 3. DIAGNOSTIC VERDICT FORMULATION
        if overall_readiness_pct >= 85 and len(blockers) == 0:
            verdict_code = "READY"
            verdict_badge = "success"
            verdict_title = "Placement Ready / Highly Qualified"
            verdict_summary = f"You possess strong alignment with {target_title}. All critical prerequisites are fulfilled."
        elif overall_readiness_pct >= 65 and len(blockers) <= 1:
            verdict_code = "FEASIBLE"
            verdict_badge = "warning"
            verdict_title = "Feasible with Targeted Preparation"
            verdict_summary = f"You have solid foundational competence for {target_title}, but need focused upskilling in {len(blockers)} key area(s)."
        else:
            verdict_code = "NOT_RECOMMENDED"
            verdict_badge = "danger"
            verdict_title = "Significant Prerequisites Missing"
            verdict_summary = f"Several foundational prerequisites for {target_title} are currently unsatisfied. Substantial bridge learning is needed."

        return {
            "target_career": {
                "id": target_career_id,
                "title": target_title,
                "category": target_profile["category"],
                "icon": target_profile["icon"],
                "badge_color": target_profile["badge_color"],
                "salary_range": target_profile["salary_range"]
            },
            "readiness_score": overall_readiness_pct,
            "verdict": {
                "code": verdict_code,
                "badge": verdict_badge,
                "title": verdict_title,
                "summary": verdict_summary
            },
            "applicable_rules_evaluated": len(applicable_rules),
            "satisfied_rules_count": satisfied_rules_count,
            "subgoal_verifications": subgoal_verifications,
            "skill_analysis": skill_analysis,
            "blockers": blockers,
            "strengths": strengths
        }
