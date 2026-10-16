/**
 * CareerWise AI - Main Application Client Scripts
 * Handles assessment questionnaire interactions, quick preset loaders, and AJAX submissions.
 */

document.addEventListener("DOMContentLoaded", () => {
    // 1. Skill Rating Button Click Handler
    const ratingGroups = document.querySelectorAll(".rating-button-group");
    const proficiencyLabels = {
        1: "1 - Novice / Conceptual",
        2: "2 - Elementary / Academic",
        3: "3 - Intermediate / Practical",
        4: "4 - Advanced / Project-Ready",
        5: "5 - Expert / Production-Level"
    };

    ratingGroups.forEach(group => {
        const skillKey = group.dataset.skill;
        const hiddenInput = document.getElementById(`input_skill_${skillKey}`);
        const labelDisplay = document.getElementById(`label_skill_${skillKey}`);
        const buttons = group.querySelectorAll(".rating-btn");

        buttons.forEach(btn => {
            btn.addEventListener("click", () => {
                const val = parseInt(btn.dataset.val, 10);
                hiddenInput.value = val;

                // Update UI state
                buttons.forEach(b => b.classList.remove("active"));
                btn.classList.add("active");

                if (labelDisplay) {
                    labelDisplay.textContent = proficiencyLabels[val] || `Level ${val}`;
                }
            });
        });
    });

    // 2. Interest Checkbox Card Toggle
    const interestCards = document.querySelectorAll(".interest-checkbox-card");
    interestCards.forEach(card => {
        const checkbox = card.querySelector("input[type='checkbox']");
        card.addEventListener("click", (e) => {
            if (e.target.tagName !== "INPUT") {
                checkbox.checked = !checkbox.checked;
            }
            if (checkbox.checked) {
                card.classList.add("selected");
            } else {
                card.classList.remove("selected");
            }
        });
    });

    // 3. Preset Profile Loader for College Viva / Live Demo
    window.loadPresetProfile = async function(profileKey) {
        if (!profileKey) return;
        try {
            const resp = await fetch(`/api/preset/${profileKey}`);
            const data = await resp.json();
            if (!data.success || !data.profile) {
                alert("Failed to load preset profile.");
                return;
            }

            const p = data.profile;
            // Fill student name
            const nameInput = document.getElementById("student_name_input");
            if (nameInput) nameInput.value = p.name;

            // Apply skills
            if (p.skills) {
                for (const [sk, val] of Object.entries(p.skills)) {
                    const hidden = document.getElementById(`input_skill_${sk}`);
                    const group = document.querySelector(`.rating-button-group[data-skill="${sk}"]`);
                    const label = document.getElementById(`label_skill_${sk}`);
                    if (hidden && group) {
                        hidden.value = val;
                        const btns = group.querySelectorAll(".rating-btn");
                        btns.forEach(b => {
                            if (parseInt(b.dataset.val, 10) === val) {
                                b.classList.add("active");
                            } else {
                                b.classList.remove("active");
                            }
                        });
                        if (label) label.textContent = proficiencyLabels[val] || `Level ${val}`;
                    }
                }
            }

            // Apply interests
            if (p.interests) {
                const interestCheckboxes = document.querySelectorAll("input[name='interests']");
                interestCheckboxes.forEach(cb => {
                    const shouldCheck = p.interests.includes(cb.value);
                    cb.checked = shouldCheck;
                    const card = cb.closest(".interest-checkbox-card");
                    if (card) {
                        if (shouldCheck) card.classList.add("selected");
                        else card.classList.remove("selected");
                    }
                });
            }

            // Apply subjects
            if (p.subjects) {
                for (const [sub, grade] of Object.entries(p.subjects)) {
                    const select = document.getElementById(`select_subject_${sub}`);
                    if (select) select.value = grade;
                }
            }

            // Apply work styles
            if (p.work_style) {
                const wp = document.getElementById("select_work_preference");
                if (wp && p.work_style.work_preference) wp.value = p.work_style.work_preference;
                const org = document.getElementById("select_org_type");
                if (org && p.work_style.organization_type) org.value = p.work_style.organization_type;
            }

            // Show confirmation toast
            const alertBox = document.getElementById("preset_alert");
            if (alertBox) {
                alertBox.textContent = `Loaded Preset: ${p.name}! Ready for inference.`;
                alertBox.classList.remove("d-none");
                setTimeout(() => alertBox.classList.add("d-none"), 4000);
            }
        } catch (err) {
            console.error("Error loading preset:", err);
        }
    };

    // 4. Form Submission Handler
    const assessmentForm = document.getElementById("assessment_form");
    if (assessmentForm) {
        assessmentForm.addEventListener("submit", async (e) => {
            e.preventDefault();

            const submitBtn = document.getElementById("submit_assessment_btn");
            const spinner = document.getElementById("submit_spinner");
            if (submitBtn) submitBtn.disabled = true;
            if (spinner) spinner.classList.remove("d-none");

            // Build payload
            const studentName = document.getElementById("student_name_input")?.value || "Student Candidate";

            // Extract skills
            const skills = {};
            document.querySelectorAll("input[name^='skill_']").forEach(inp => {
                const skKey = inp.name.replace("skill_", "");
                skills[skKey] = parseInt(inp.value, 10) || 1;
            });

            // Extract interests
            const interests = [];
            document.querySelectorAll("input[name='interests']:checked").forEach(cb => {
                interests.push(cb.value);
            });

            // Extract subjects
            const subjects = {};
            document.querySelectorAll("select[name^='subject_']").forEach(sel => {
                const subKey = sel.name.replace("subject_", "");
                subjects[subKey] = sel.value;
            });

            // Extract work style
            const workStyle = {
                work_preference: document.getElementById("select_work_preference")?.value || "building",
                organization_type: document.getElementById("select_org_type")?.value || "enterprise"
            };

            const payload = {
                student_name: studentName,
                skills: skills,
                interests: interests,
                subjects: subjects,
                work_style: workStyle
            };

            try {
                const response = await fetch("/api/assess", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify(payload)
                });

                const data = await response.json();
                if (data.success) {
                    window.location.href = "/results";
                } else {
                    alert("Assessment error: " + (data.error || "Inference failed"));
                    if (submitBtn) submitBtn.disabled = false;
                    if (spinner) spinner.classList.add("d-none");
                }
            } catch (err) {
                console.error("Error submitting assessment:", err);
                alert("Failed to submit assessment. Please check console.");
                if (submitBtn) submitBtn.disabled = false;
                if (spinner) spinner.classList.add("d-none");
            }
        });
    }
});
