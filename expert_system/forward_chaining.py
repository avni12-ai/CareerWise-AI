"""
CareerWise AI - Forward Chaining Inference Engine
Implements classical data-driven expert system reasoning:
1. Working Memory initialization from student facts
2. Pattern matching against Knowledge Base production rules
3. Certainty Factor (CF) propagation using MYCIN combination algebra
4. Multi-Criteria Decision Analysis (MCDA) integrating skills, academics, and interests
5. Conflict resolution and inference execution trace generation
"""

from typing import Dict, List, Any, Tuple
from expert_system.knowledge_base import (
    CAREERS,
    SKILLS_METADATA,
    INTERESTS_METADATA,
    SUBJECTS_METADATA,
    PRODUCTION_RULES
)

GRADE_NUMERIC = {
    "A+": 4.0,
    "A": 3.5,
    "B": 2.5,
    "C": 1.5,
    "F": 0.0
}


class ForwardChainingEngine:
    def __init__(self):
        self.rules = PRODUCTION_RULES
        self.careers = CAREERS

    def evaluate_condition(self, cond_type: str, condition: Any, working_memory: Dict[str, Any]) -> Tuple[bool, str]:
        """
        Evaluates a single antecedent condition against Working Memory.
        Returns (is_satisfied, justification_str)
        """
        if cond_type == "skills":
            # condition: dict of {skill_name: (operator, threshold)}
            for skill_id, (op, threshold) in condition.items():
                student_val = working_memory.get("skills", {}).get(skill_id, 1)
                skill_name = SKILLS_METADATA.get(skill_id, {}).get("name", skill_id)
                if op == ">=" and student_val < threshold:
                    return False, f"Skill '{skill_name}' is level {student_val}, required >= {threshold}"
                elif op == ">" and student_val <= threshold:
                    return False, f"Skill '{skill_name}' is level {student_val}, required > {threshold}"
                elif op == "==" and student_val != threshold:
                    return False, f"Skill '{skill_name}' is level {student_val}, required == {threshold}"
            return True, "Skill thresholds satisfied"

        elif cond_type == "interests":
            # condition: list of required interest_ids (at least one must match)
            student_interests = set(working_memory.get("interests", []))
            matched_interests = [i for i in condition if i in student_interests]
            if not matched_interests:
                req_names = [INTERESTS_METADATA.get(i, {}).get("name", i) for i in condition]
                return False, f"Lacks interest in: {', '.join(req_names)}"
            return True, f"Matched interest: {', '.join(matched_interests)}"

        elif cond_type == "subjects":
            # condition: dict of {subject_id: (operator, min_grade_str)}
            student_subjects = working_memory.get("subjects", {})
            for sub_id, (op, min_grade) in condition.items():
                actual_grade = student_subjects.get(sub_id, "C")
                actual_num = GRADE_NUMERIC.get(actual_grade, 1.5)
                min_num = GRADE_NUMERIC.get(min_grade, 3.5)
                sub_name = SUBJECTS_METADATA.get(sub_id, {}).get("name", sub_id)
                if actual_num < min_num:
                    return False, f"Grade in {sub_name} is {actual_grade}, required >= {min_grade}"
            return True, "Academic grade thresholds met"

        elif cond_type == "work_style":
            student_work_style = working_memory.get("work_style", {})
            for key, expected_val in condition.items():
                actual_val = student_work_style.get(key)
                if actual_val != expected_val:
                    return False, f"Work style '{key}' is '{actual_val}', expected '{expected_val}'"
            return True, "Work style preferences aligned"

        return False, "Unknown condition type"

    def run_inference(self, student_facts: Dict[str, Any]) -> Dict[str, Any]:
        """
        Executes Forward Chaining over student facts.
        Generates:
        - Career rankings with Certainty Factors & Match Percentages
        - Complete Rule Firing Trace (Every rule tested, outcome, and contribution)
        - Top 3 career recommendations
        """
        working_memory = student_facts.copy()
        
        # Track cumulative certainty factors per career
        career_cf: Dict[str, float] = {cid: 0.0 for cid in self.careers.keys()}
        fired_rules: List[Dict[str, Any]] = []
        rejected_rules: List[Dict[str, Any]] = []

        # 1. MATCH-RESOLVE-ACT CYCLE OVER PRODUCTION RULES
        for rule in self.rules:
            rule_id = rule["id"]
            rule_name = rule["name"]
            category = rule["category"]
            conditions = rule["conditions"]
            consequent = rule["consequent"]
            explanation = rule["explanation"]

            all_satisfied = True
            rejection_reasons = []

            for cond_type, cond_val in conditions.items():
                satisfied, reason = self.evaluate_condition(cond_type, cond_val, working_memory)
                if not satisfied:
                    all_satisfied = False
                    rejection_reasons.append(reason)
                    break

            if all_satisfied:
                # Fire Rule: apply Shortliffe / MYCIN certainty factor combination formula
                # CF_combined = CF_old + CF_rule * (1 - CF_old)
                affected_careers = []
                for career_id, rule_cf in consequent.items():
                    old_cf = career_cf.get(career_id, 0.0)
                    new_cf = old_cf + rule_cf * (1.0 - old_cf)
                    career_cf[career_id] = min(1.0, round(new_cf, 4))
                    affected_careers.append({
                        "career_id": career_id,
                        "career_title": self.careers[career_id]["title"],
                        "rule_cf": rule_cf,
                        "prior_cf": round(old_cf, 4),
                        "posterior_cf": round(new_cf, 4)
                    })

                fired_rules.append({
                    "rule_id": rule_id,
                    "rule_name": rule_name,
                    "category": category,
                    "explanation": explanation,
                    "affected_careers": affected_careers
                })
            else:
                rejected_rules.append({
                    "rule_id": rule_id,
                    "rule_name": rule_name,
                    "category": category,
                    "reason": "; ".join(rejection_reasons)
                })

        # 2. MULTI-CRITERIA EVALUATION (Skills Benchmark, Academics, Interests)
        career_evaluations = []
        for cid, profile in self.careers.items():
            # A. Skills Match (0 - 100)
            core_skills = profile["core_skills"]
            crit_skills = set(profile.get("critical_skills", []))
            total_skill_weight = 0.0
            earned_skill_weight = 0.0

            for sk_id, benchmark in core_skills.items():
                weight = 1.5 if sk_id in crit_skills else 1.0
                total_skill_weight += (benchmark * weight)
                
                student_lvl = working_memory.get("skills", {}).get(sk_id, 1)
                # Cap contribution at benchmark level
                effective_lvl = min(student_lvl, benchmark)
                earned_skill_weight += (effective_lvl * weight)

            skill_match_pct = round((earned_skill_weight / total_skill_weight) * 100, 1) if total_skill_weight > 0 else 0

            # B. Academic Alignment (0 - 100)
            relevant_subjects = [s_id for s_id, s_meta in SUBJECTS_METADATA.items() if cid in s_meta.get("key_for", [])]
            if relevant_subjects:
                earned_acad = sum(GRADE_NUMERIC.get(working_memory.get("subjects", {}).get(s, "C"), 1.5) for s in relevant_subjects)
                max_acad = 4.0 * len(relevant_subjects)
                acad_match_pct = round((earned_acad / max_acad) * 100, 1)
            else:
                acad_match_pct = 70.0

            # C. Interests & Work Style Alignment (0 - 100)
            student_interests = set(working_memory.get("interests", []))
            rec_interests = profile.get("recommended_interests", [])
            matched_int_count = sum(1 for i in rec_interests if i in student_interests)
            int_match_pct = round((matched_int_count / len(rec_interests)) * 100, 1) if rec_interests else 70.0

            # Work style alignment
            student_work_pref = working_memory.get("work_style", {}).get("work_preference")
            work_style_bonus = 10 if student_work_pref in profile.get("ideal_work_style", []) else 0

            # D. Certainty Factor Normalized (0 - 100)
            cf_val = career_cf.get(cid, 0.0)
            cf_pct = round(cf_val * 100, 1)

            # E. Composite Score Calculation (Weighted AIES Formula)
            # 40% Rule CF + 35% Skills Benchmark + 15% Academics + 10% Interests/WorkStyle
            composite_score = round(
                (0.40 * cf_pct) +
                (0.35 * skill_match_pct) +
                (0.15 * acad_match_pct) +
                (0.10 * min(100.0, int_match_pct + work_style_bonus)),
                1
            )

            career_evaluations.append({
                "career_id": cid,
                "title": profile["title"],
                "category": profile["category"],
                "description": profile["description"],
                "icon": profile["icon"],
                "badge_color": profile["badge_color"],
                "salary_range": profile["salary_range"],
                "industry_demand": profile["industry_demand"],
                "composite_score": composite_score,
                "certainty_factor": round(cf_val, 3),
                "certainty_pct": cf_pct,
                "skill_match_pct": skill_match_pct,
                "academic_match_pct": acad_match_pct,
                "interest_match_pct": int_match_pct,
                "core_skills": core_skills,
                "critical_skills": profile.get("critical_skills", []),
                "fired_rules_count": sum(1 for fr in fired_rules if any(ac["career_id"] == cid for ac in fr["affected_careers"]))
            })

        # 3. CONFLICT RESOLUTION & RANKING
        # Sort primarily by composite score, tie-breaker by certainty factor
        career_evaluations.sort(key=lambda x: (x["composite_score"], x["certainty_factor"]), reverse=True)

        top_3_recommendations = career_evaluations[:3]
        other_careers = career_evaluations[3:]

        return {
            "top_recommendations": top_3_recommendations,
            "all_careers": career_evaluations,
            "other_careers": other_careers,
            "trace": {
                "total_rules_evaluated": len(self.rules),
                "rules_fired_count": len(fired_rules),
                "rules_rejected_count": len(rejected_rules),
                "fired_rules": fired_rules,
                "rejected_rules": rejected_rules
            },
            "student_summary": {
                "total_skills_evaluated": len(working_memory.get("skills", {})),
                "interests_selected": len(working_memory.get("interests", [])),
                "subjects_evaluated": len(working_memory.get("subjects", {}))
            }
        }
