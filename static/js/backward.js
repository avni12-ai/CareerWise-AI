/**
 * CareerWise AI - Goal-Driven Backward Chaining Diagnostic Scripts
 */

document.addEventListener("DOMContentLoaded", () => {
    let currentStudentFacts = null;

    // Check if preset is clicked
    window.loadPresetIntoBackward = async function(presetKey) {
        if (!presetKey) return;
        try {
            const resp = await fetch(`/api/preset/${presetKey}`);
            const data = await resp.json();
            if (data.success && data.profile) {
                currentStudentFacts = {
                    skills: data.profile.skills,
                    interests: data.profile.interests,
                    subjects: data.profile.subjects,
                    work_style: data.profile.work_style
                };
                const profileLabel = document.getElementById("active_student_profile_label");
                if (profileLabel) {
                    profileLabel.textContent = `Active Profile: ${data.profile.name}`;
                    profileLabel.classList.remove("text-muted");
                    profileLabel.classList.add("text-primary", "fw-bold");
                }
                // Automatically run diagnosis
                runDiagnostic();
            }
        } catch (err) {
            console.error("Error loading preset:", err);
        }
    };

    window.runDiagnostic = async function() {
        const careerSelect = document.getElementById("target_career_select");
        const targetCareerId = careerSelect ? careerSelect.value : "ai_ml_engineer";

        // If no preset loaded, fallback to default profile or prompt
        if (!currentStudentFacts) {
            // Default to AI preset if nothing loaded yet
            await loadPresetIntoBackward("profile_ai");
            return;
        }

        const container = document.getElementById("diagnostic_results_container");
        if (container) {
            container.innerHTML = `
                <div class="text-center py-5">
                    <div class="spinner-border text-primary" role="status"></div>
                    <p class="mt-2 text-muted fw-semibold">Evaluating Goal Hypothesis via Backward Chaining...</p>
                </div>
            `;
        }

        try {
            const resp = await fetch("/api/backward-chain", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    target_career_id: targetCareerId,
                    skills: currentStudentFacts.skills,
                    interests: currentStudentFacts.interests,
                    subjects: currentStudentFacts.subjects,
                    work_style: currentStudentFacts.work_style
                })
            });

            const data = await resp.json();
            if (data.success && data.diagnosis) {
                renderDiagnosticView(data.diagnosis);
            } else {
                if (container) container.innerHTML = `<div class="alert alert-danger">Diagnostic failed: ${data.error || 'Unknown error'}</div>`;
            }
        } catch (err) {
            console.error("Diagnostic error:", err);
            if (container) container.innerHTML = `<div class="alert alert-danger">Error communicating with backward chaining engine.</div>`;
        }
    };

    function renderDiagnosticView(diag) {
        const container = document.getElementById("diagnostic_results_container");
        if (!container) return;

        const v = diag.verdict;
        const target = diag.target_career;

        let blockersHtml = "";
        if (diag.blockers.length > 0) {
            blockersHtml = diag.blockers.map(b => `
                <div class="d-flex justify-content-between align-items-center p-2 mb-2 bg-danger-subtle rounded border border-danger-subtle">
                    <div>
                        <span class="badge bg-danger me-2">Blocker</span>
                        <strong>${b.skill_name}</strong>
                    </div>
                    <div class="small fw-semibold text-danger">
                        Current: Lvl ${b.current_level} / Required: Lvl ${b.benchmark_level} (Deficit: -${b.gap})
                    </div>
                </div>
            `).join("");
        } else {
            blockersHtml = `<div class="text-success p-2 small"><i class="bi bi-check-circle-fill me-1"></i> No critical blockers detected! All core prerequisite thresholds are satisfied.</div>`;
        }

        let strengthsHtml = "";
        if (diag.strengths.length > 0) {
            strengthsHtml = diag.strengths.map(s => `
                <span class="badge bg-success-subtle text-success border border-success-subtle p-2 me-2 mb-2">
                    <i class="bi bi-check-lg me-1"></i> ${s.skill_name} (Lvl ${s.current_level}/${s.benchmark_level})
                </span>
            `).join("");
        } else {
            strengthsHtml = `<span class="text-muted small">None meeting full benchmark yet.</span>`;
        }

        // Subgoal rule decompositions
        let rulesHtml = diag.subgoal_verifications.map(rv => {
            const statusBadge = rv.satisfied
                ? `<span class="badge bg-success"><i class="bi bi-check-circle me-1"></i> Rule Proved (CF: ${rv.rule_cf})</span>`
                : `<span class="badge bg-secondary"><i class="bi bi-x-circle me-1"></i> Preconditions Not Satisfied</span>`;

            const subgoalsList = rv.subgoals.map(sg => `
                <li class="list-group-item d-flex justify-content-between align-items-center py-2 ${sg.satisfied ? 'bg-light' : 'bg-white'}">
                    <div>
                        <span class="badge ${sg.satisfied ? 'bg-success-subtle text-success' : 'bg-danger-subtle text-danger'} me-2">
                            ${sg.satisfied ? 'SATISFIED' : 'UNMET'}
                        </span>
                        <span class="fw-semibold">${sg.name}</span>
                        <span class="text-muted small ms-1">(${sg.type})</span>
                    </div>
                    <div class="small">
                        <span class="text-muted">Target: ${sg.required}</span> | 
                        <strong class="${sg.satisfied ? 'text-success' : 'text-danger'}">You: ${sg.current}</strong>
                    </div>
                </li>
            `).join("");

            return `
                <div class="card mb-3 border">
                    <div class="card-header d-flex justify-content-between align-items-center bg-white py-2">
                        <div>
                            <span class="badge bg-dark me-2 font-mono">${rv.rule_id}</span>
                            <strong>${rv.rule_name}</strong>
                        </div>
                        <div>${statusBadge}</div>
                    </div>
                    <ul class="list-group list-group-flush small">
                        ${subgoalsList}
                    </ul>
                </div>
            `;
        }).join("");

        container.innerHTML = `
            <!-- Verdict Card -->
            <div class="card card-modern mb-4 border-top border-4 border-${v.badge}">
                <div class="card-body p-4">
                    <div class="d-flex flex-wrap justify-content-between align-items-center mb-3">
                        <div class="d-flex align-items-center gap-3">
                            <div class="brand-icon" style="background: ${target.badge_color};">
                                <i class="bi ${target.icon}"></i>
                            </div>
                            <div>
                                <h4 class="fw-bold mb-0">${target.title}</h4>
                                <span class="text-muted small">${target.category} | ${target.salary_range}</span>
                            </div>
                        </div>
                        <div>
                            <span class="badge bg-${v.badge} fs-6 px-3 py-2 rounded-pill">${v.title}</span>
                        </div>
                    </div>

                    <p class="text-secondary mb-3">${v.summary}</p>

                    <div class="row g-3">
                        <div class="col-md-4">
                            <div class="p-3 bg-light rounded text-center">
                                <div class="text-muted small mb-1">Prerequisite Readiness Score</div>
                                <div class="fs-2 fw-bold text-primary">${diag.readiness_score}%</div>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="p-3 bg-light rounded text-center">
                                <div class="text-muted small mb-1">Supporting Rules Satisfied</div>
                                <div class="fs-2 fw-bold text-success">${diag.satisfied_rules_count} / ${diag.applicable_rules_evaluated}</div>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="p-3 bg-light rounded text-center">
                                <div class="text-muted small mb-1">Critical Blocker Skills</div>
                                <div class="fs-2 fw-bold text-danger">${diag.blockers.length}</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Blockers & Strengths -->
            <div class="row g-4 mb-4">
                <div class="col-lg-6">
                    <div class="card card-modern h-100">
                        <div class="card-header-styled">
                            <h6 class="fw-bold mb-0 text-danger"><i class="bi bi-exclamation-triangle-fill me-2"></i>Critical Blocker Skills to Overcome</h6>
                        </div>
                        <div class="card-body">
                            ${blockersHtml}
                        </div>
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="card card-modern h-100">
                        <div class="card-header-styled">
                            <h6 class="fw-bold mb-0 text-success"><i class="bi bi-shield-check me-2"></i>Verified Core Strengths</h6>
                        </div>
                        <div class="card-body">
                            ${strengthsHtml}
                        </div>
                    </div>
                </div>
            </div>

            <!-- Backward Goal Decomposition Tree -->
            <div class="card card-modern">
                <div class="card-header-styled d-flex justify-content-between align-items-center">
                    <h6 class="fw-bold mb-0">
                        <i class="bi bi-diagram-2-fill text-primary me-2"></i>
                        Backward Chaining Subgoal Resolution Tree
                    </h6>
                    <span class="badge bg-light text-dark font-mono small">Goal: IsQualifiedFor(${target.id})</span>
                </div>
                <div class="card-body p-3">
                    <p class="small text-muted mb-3">
                        The inference engine evaluated the following candidate rules asserting <code>${target.title}</code>.
                        Each rule is broken into subgoals verified directly against the student's working memory facts:
                    </p>
                    ${rulesHtml}
                </div>
            </div>
        `;
    }

    // Auto-trigger on page load with default AI profile
    loadPresetIntoBackward("profile_ai");
});
