/**
 * CareerWise AI - What-If Scenario Simulator Client Script
 * Provides live real-time slider updates and dynamic recalculation of predictions.
 */

document.addEventListener("DOMContentLoaded", () => {
    let debounceTimer = null;

    // Attach input listeners to all range sliders
    const sliders = document.querySelectorAll(".what-if-slider");
    sliders.forEach(slider => {
        slider.addEventListener("input", () => {
            const valDisplay = document.getElementById(`val_${slider.id}`);
            if (valDisplay) valDisplay.textContent = slider.value;
            triggerSimulationDebounced();
        });
    });

    // Attach change listeners to all interest checkboxes
    const checkboxes = document.querySelectorAll(".what-if-checkbox");
    checkboxes.forEach(cb => {
        cb.addEventListener("change", () => {
            triggerSimulationDebounced();
        });
    });

    function triggerSimulationDebounced() {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(runSimulation, 250);
    }

    window.runSimulation = async function() {
        // Collect current state from sliders & inputs
        const skills = {};
        document.querySelectorAll(".what-if-slider").forEach(sl => {
            skills[sl.dataset.skill] = parseInt(sl.value, 10);
        });

        const interests = [];
        document.querySelectorAll(".what-if-checkbox:checked").forEach(cb => {
            interests.push(cb.value);
        });

        // Use standard academic subjects
        const subjects = {
            "dsa_sub": "A",
            "dbms_sub": "A",
            "os_sub": "B",
            "cn_sub": "B",
            "ai_sub": "B",
            "stats_math_sub": "B",
            "security_sub": "B",
            "cloud_sub": "B",
            "web_sub": "B",
            "microprocessor_sub": "C"
        };

        const workStyle = {
            work_preference: document.getElementById("whatif_work_pref")?.value || "building",
            organization_type: "enterprise"
        };

        const statusIndicator = document.getElementById("simulation_status_indicator");
        if (statusIndicator) statusIndicator.innerHTML = '<span class="spinner-border spinner-border-sm text-primary me-1"></span> Recalculating...';

        try {
            const resp = await fetch("/api/what-if-simulate", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    skills: skills,
                    interests: interests,
                    subjects: subjects,
                    work_style: workStyle
                })
            });

            const data = await resp.json();
            if (data.success) {
                renderSimulationResults(data.top_3, data.all_careers);
                if (statusIndicator) statusIndicator.innerHTML = '<span class="badge bg-success-subtle text-success"><i class="bi bi-check-circle me-1"></i> Live Inferred</span>';
            }
        } catch (err) {
            console.error("Simulation error:", err);
            if (statusIndicator) statusIndicator.innerHTML = '<span class="badge bg-danger">Simulation Error</span>';
        }
    };

    function renderSimulationResults(top3, allCareers) {
        const topContainer = document.getElementById("simulation_top_container");
        if (!topContainer) return;

        topContainer.innerHTML = top3.map((c, idx) => {
            const rank = idx + 1;
            const rankColors = ["#2563eb", "#7c3aed", "#059669"];
            const borderColor = rankColors[idx] || "#64748b";

            return `
                <div class="card card-modern mb-3 p-3 position-relative" style="border-left: 5px solid ${borderColor};">
                    <div class="d-flex justify-content-between align-items-center mb-2">
                        <div class="d-flex align-items-center gap-2">
                            <span class="badge rounded-pill" style="background-color: ${borderColor};">Rank #${rank}</span>
                            <strong class="fs-6">${c.title}</strong>
                        </div>
                        <div class="text-end">
                            <span class="fs-4 fw-bold" style="color: ${borderColor};">${c.composite_score}%</span>
                        </div>
                    </div>
                    <div class="progress mb-2" style="height: 6px;">
                        <div class="progress-bar" style="width: ${c.composite_score}%; background-color: ${borderColor};"></div>
                    </div>
                    <div class="d-flex justify-content-between text-muted small">
                        <span>Certainty Factor: <strong>${c.certainty_factor}</strong> (${c.certainty_pct}%)</span>
                        <span>Skill Match: <strong>${c.skill_match_pct}%</strong></span>
                    </div>
                </div>
            `;
        }).join("");

        // Update comparison table
        const tableBody = document.getElementById("simulation_table_body");
        if (tableBody) {
            tableBody.innerHTML = allCareers.map((c, idx) => `
                <tr>
                    <td class="fw-bold text-muted">${idx + 1}</td>
                    <td><strong>${c.title}</strong></td>
                    <td><span class="badge bg-light text-dark font-mono">${c.certainty_factor}</span></td>
                    <td>${c.skill_match_pct}%</td>
                    <td>
                        <div class="d-flex align-items-center gap-2">
                            <div class="progress flex-grow-1" style="height: 8px;">
                                <div class="progress-bar bg-primary" style="width: ${c.composite_score}%;"></div>
                            </div>
                            <span class="fw-bold small">${c.composite_score}%</span>
                        </div>
                    </td>
                </tr>
            `).join("");
        }
    }

    // Preset quick-loader on what-if page
    window.loadPresetIntoWhatIf = async function(presetKey) {
        if (!presetKey) return;
        try {
            const resp = await fetch(`/api/preset/${presetKey}`);
            const data = await resp.json();
            if (data.success && data.profile) {
                const p = data.profile;
                if (p.skills) {
                    for (const [sk, val] of Object.entries(p.skills)) {
                        const slider = document.getElementById(`whatif_skill_${sk}`);
                        const valDisplay = document.getElementById(`val_whatif_skill_${sk}`);
                        if (slider) {
                            slider.value = val;
                            if (valDisplay) valDisplay.textContent = val;
                        }
                    }
                }
                if (p.interests) {
                    document.querySelectorAll(".what-if-checkbox").forEach(cb => {
                        cb.checked = p.interests.includes(cb.value);
                    });
                }
                runSimulation();
            }
        } catch (err) {
            console.error("Error setting what-if preset:", err);
        }
    };

    // Run initial simulation
    runSimulation();
});
