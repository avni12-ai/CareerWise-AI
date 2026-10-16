# CareerWise AI — Intelligent Career Guidance Expert System

[![Subject](https://img.shields.io/badge/Subject-Artificial%20Intelligence%20%26%20Expert%20Systems%20(AIES)-blue.svg)]()
[![Course](https://img.shields.io/badge/Engineering-TE%20Computer%20Engineering-darkgreen.svg)]()
[![Stack](https://img.shields.io/badge/Stack-Python%20%7C%20Flask%20%7C%20Chart.js-orange.svg)]()
[![Status](https://img.shields.io/badge/Status-Viva%20%26%20Evaluation%20Ready-brightgreen.svg)]()

> A full-featured, production-grade academic expert system designed for the **Artificial Intelligence & Expert Systems (AIES)** curriculum. Implements **Forward Chaining**, **Backward Chaining**, **MYCIN Certainty Factors**, **Explanation Facilities (Why/How/Why Not)**, and interactive **Skill Gap Visualizations**.

---

## 1. Project Overview & Motivation

In traditional engineering education, career counseling is either arbitrary or relies on black-box predictive algorithms. In educational guidance, **transparency, accountability, and explainability** are paramount. A student cannot act on a recommendation unless they understand **why** it was made, **how** the conclusion was derived, and **what specific prerequisites they are missing**.

**CareerWise AI** addresses this challenge by implementing a classic **Rule-Based Expert System (ES)** architecture that models the reasoning of human technical career counselors:
- **Zero Paid APIs or External Keys:** Runs entirely offline and locally.
- **Zero Mandatory Databases:** Uses structured, declarative Python dictionaries and JSON structures for total transparency and portability.
- **Dual Inference Paradigms:** Features both **Data-Driven (Forward Chaining)** career recommendations and **Goal-Driven (Backward Chaining)** eligibility diagnostics.
- **Inexact Reasoning:** Incorporates Shortliffe's classical **MYCIN Certainty Factor (CF) algebra** to calculate confidence levels under incomplete knowledge.
- **Explanation Facility:** Answers *Why* a career was selected, *How* the certainty factor was mathematically accumulated, and *Why Not* for lower-ranked careers.

---

## 2. AIES Theoretical Foundations

```
+-----------------------------------------------------------------------------------+
|                                 USER INTERFACE                                    |
|   (Interactive Questionnaire | What-If Simulator | Goal Diagnostic | KB Browser)  |
+-----------------------------------------------------------------------------------+
                                         |  Assert Facts / Query Goal
                                         v
+-----------------------------------------------------------------------------------+
|                                WORKING MEMORY                                     |
|   - Technical Skills (Levels 1-5 across 23 competencies)                          |
|   - Domain Interests & Passions (AI, Security, Cloud, Web, Hardware, etc.)        |
|   - Academic University Coursework Grades (DSA, DBMS, OS, Networks, Math, etc.)   |
|   - Work Style & Environmental Preferences (Research, Building, Defense, etc.)    |
+-----------------------------------------------------------------------------------+
             ^                                           ^
             | Pattern Match Antecedents                 | Goal Decomposition
             v                                           v
+-----------------------------------------+ +---------------------------------------+
|        FORWARD CHAINING ENGINE          | |       BACKWARD CHAINING ENGINE        |
|  - Match-Resolve-Act Cycle              | |  - Goal Hypothesis: IsQualified(X)   |
|  - Production Rules Evaluation          | |  - Decompose Antecedents to Subgoals  |
|  - Conflict Resolution (Specificity)    | |  - Verify against Leaf Facts in WM    |
|  - MYCIN Certainty Factor Propagation   | |  - Critical Blocker & Gap Diagnostic  |
|  - Multi-Criteria Decision Analysis     | |                                       |
+-----------------------------------------+ +---------------------------------------+
                     \                                   /
                      \                                 /
                       v                               v
+-----------------------------------------------------------------------------------+
|                              KNOWLEDGE BASE (KB)                                  |
|   - Production Rules (IF-THEN Production Rules with Certainty Factors)            |
|   - Career Competency Benchmark Profiles (8 Core Engineering Domains)             |
|   - Skill Taxonomies, Critical Prerequisites, and Curated Roadmaps                |
+-----------------------------------------------------------------------------------+
                                         |
                                         v
+-----------------------------------------------------------------------------------+
|                              EXPLANATION FACILITY                                 |
|   - "WHY": Positive evidence, fired rules, and standout candidate strengths       |
|   - "HOW": Step-by-step MYCIN Shortliffe formula derivation and score breakdown   |
|   - "WHY NOT": Explanations for lower ranks, prerequisite deficits & gaps         |
|   - Visual Radar Charts (Assessed vs Benchmark) & Comparative Bar Charts          |
+-----------------------------------------------------------------------------------+
```

### Key Expert System Concepts Demonstrated:

1. **Declarative Knowledge Representation:**
   Domain heuristics are decoupled from inference algorithms. Rules are expressed in standard production format:
   $$\text{IF } \langle \text{Antecedent}_1 \land \text{Antecedent}_2 \land \dots \rangle \text{ THEN } \langle \text{Consequent} \rangle \text{ WITH CF} = \alpha$$

2. **Forward Chaining (Data-Driven Deduction):**
   - **Input:** Student's evaluated technical skills, interests, and academic grades.
   - **Process:** Matches preconditions against the Knowledge Base, fires triggered rules, updates hypothesis Certainty Factors, and resolves conflicts to rank top careers.

3. **Backward Chaining (Goal-Driven Diagnosis):**
   - **Input:** Target Career Goal (e.g., *"Can I become an AI/ML Engineer?"*).
   - **Process:** Examines candidate rules that conclude the target goal, breaks them down into subgoals, traces leaf facts in Working Memory, and identifies exact missing prerequisites and critical blocker skills.

4. **Certainty Factor Algebra (MYCIN Formula):**
   When multiple rules $R_1, R_2, \dots$ provide independent positive evidence for a career hypothesis $H$:
   $$\text{CF}_{\text{combined}} = \text{CF}_{\text{prior}} + \text{CF}_{\text{rule}} \times (1 - \text{CF}_{\text{prior}})$$
   This mirrors human expert judgment: subsequent corroborating evidence increases confidence asymptotically toward $1.0$ (100% certainty).

5. **Multi-Criteria Decision Analysis (MCDA):**
   The final composite suitability score harmonizes:
   $$\text{Composite Score} = 0.40 \times \text{CF}_{\text{rules}}\% + 0.35 \times \text{SkillMatch}\% + 0.15 \times \text{Academics}\% + 0.10 \times \text{Interest}\%$$
   *Critical skills have a $1.5\times$ weight to penalize deficit in non-negotiable fundamentals.*

---

## 3. Supported Career Trajectories

The system evaluates and provides guidance for **8 modern technology career tracks**:
1. **Software Developer / Full Stack Engineer**
2. **Data Analyst**
3. **AI / Machine Learning Engineer**
4. **Cybersecurity Analyst**
5. **Cloud & DevOps Engineer**
6. **Data Engineer**
7. **UI/UX & Frontend Engineer**
8. **Systems & Embedded Engineer**

---

## 4. Technology Stack

- **AI & Expert System Logic:** Python 3 (Pure standard library, zero external AI APIs, zero black boxes).
- **Backend Framework:** Flask 3 (Lightweight REST API and Jinja2 server-side rendering).
- **Frontend Architecture:** Modern HTML5, Responsive CSS3, Vanilla JavaScript (ES6+).
- **Visual Analytics:** Chart.js 4 (Radar Skill Gap charts and comparative horizontal bar charts).
- **Knowledge Base Storage:** Declarative Python structures and JSON (Instant loading, transparent inspectability).
- **Print & Export:** Native browser print stylesheets with official academic sign-off blocks.

---

## 5. Project Directory Structure

```
careerwise_ai/
├── app.py                      # Flask application entry point, routing & REST APIs
├── requirements.txt            # Minimal dependencies (Flask)
├── README.md                   # Comprehensive documentation & Viva guide
│
├── expert_system/
│   ├── __init__.py             # Package exports
│   ├── knowledge_base.py       # Declarative rules, career profiles, taxonomies & presets
│   ├── forward_chaining.py     # Forward Chaining Engine with MYCIN CF propagation
│   ├── backward_chaining.py    # Goal-driven Backward Chaining & blocker diagnostics
│   ├── explanation.py          # Explanation Facility (Why, How, Why Not, Chart data)
│   └── roadmap_generator.py    # 3-Phase upskilling roadmaps, projects & certifications
│
├── static/
│   ├── css/
│   │   └── style.css           # Custom modern responsive styling & print stylesheet
│   └── js/
│       ├── app.js              # Assessment interactions, 1-click presets & AJAX forms
│       ├── charts.js           # Chart.js radar and comparison bar charts
│       ├── backward.js         # Backward chaining goal diagnostic UI
│       └── what_if.js          # Real-time reactive slider simulator
│
└── templates/
    ├── base.html               # Master layout with navbar and footer
    ├── index.html              # Landing page, architecture breakdown & viva launchpad
    ├── assessment.html         # Interactive questionnaire (23 skills, interests, grades)
    ├── results.html            # Top 3 recommendations, charts, explanations & roadmap
    ├── backward_chain.html     # Goal-Driven Diagnostic page
    ├── what_if.html            # Real-Time What-If Scenario Simulator
    ├── kb_explorer.html        # Interactive Knowledge Base & Production Rules browser
    └── report_template.html    # Printable Official Career Advisory Report
```

---

## 6. How to Run the Project Locally

### Step 1: Open Terminal / PowerShell
Navigate to the project directory:
```bash
cd "C:\Users\AVNI\.gemini\antigravity\scratch\careerwise_ai"
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Launch the Flask Server
```bash
python app.py
```

### Step 4: Access in Web Browser
Open your browser and navigate to:
```
http://127.0.0.1:5050
```

---

## 7. Viva Demonstration Walkthrough (For Examiners & Evaluators)

During your college viva or project presentation, follow this 4-step demonstration flow:

### Demo 1: One-Click Assessment with Live Presets
1. On the home page (`/`) or assessment page (`/assessment`), locate the **"Live Viva Quick Demo Launchpad"**.
2. Select **"Aarav Sharma (AI & Data Science Enthusiast)"** or **"Neha Patel (Cyber Defense Specialist)"**.
3. Point out to the examiner that all 23 skills, domain interests, university grades, and work preferences populate automatically.
4. Click **"Run Expert System Inference"**.

### Demo 2: The Recommendation Dashboard & Explanation Facility
1. View the **Top 3 Recommended Careers** with their **Certainty Factors** and **Composite Scores**.
2. Show the **Chart.js Radar Chart**: Highlight the student's evaluated levels versus the industry benchmark.
3. Open the **Explanation Facility Tabs**:
   - **Why This Career:** Show the exact production rules that fired (e.g. `RULE_AIML_01`, `RULE_AIML_02`).
   - **How Inferred:** Walk the examiner through the step-by-step **MYCIN Certainty Factor table** ($CF_{\text{prior}} \to CF_{\text{posterior}}$) and the 40/35/15/10 weighting breakdown.
   - **Why Not Others:** Show the examiner why lower-ranked careers failed (e.g., missing critical prerequisites like Networking or Low Certainty Factor).
   - **Rule Firing Trace:** Show the complete audit log of evaluated, fired, and rejected rules.

### Demo 3: Goal-Driven Backward Chaining Diagnostic
1. Click **"Goal Diagnostic"** in the navbar (`/backward-chain`).
2. Select target goal: *"AI / Machine Learning Engineer"*.
3. Click preset **"Neha (Cyber)"**.
4. Observe the verdict: **"Significant Prerequisites Missing"**. The backward chainer decomposes the rules into subgoals and highlights **Python, ML/DL, and Linear Algebra as critical blockers**!

### Demo 4: Real-Time "What-If" Analysis Simulator
1. Navigate to **"What-If Simulator"** (`/what-if`).
2. Move the **Python** and **Machine Learning** sliders from 1 to 5, and check the **AI / ML** interest box.
3. Watch the right-hand panel **instantly recalculate predictions in real-time** without reloading the page!

### Demo 5: Knowledge Base Transparency & Print Report
1. Click **"Knowledge Base"** (`/kb-explorer`) to show the examiner the structured rule base and search filter.
2. Click **"Print / Export Report"** (`/printable-report`) to show the official academic advisory report ready for PDF export.

---

## 8. Common Viva Questions & Model Answers

### Q1: What makes this an "Expert System" and not just a conventional program or ML model?
> **Answer:** An expert system separates the **Knowledge Base (declarative rules and domain facts)** from the **Inference Engine (procedural logic)**. Unlike machine learning, which requires massive training datasets and generates black-box predictions, our expert system provides deterministic, fully transparent reasoning, handles uncertainty using Certainty Factors, and includes an Explanation Facility that can explain *Why* and *How* conclusions were reached.

### Q2: Explain how Forward Chaining works in your system.
> **Answer:** Forward Chaining is data-driven. The student's assessment facts are loaded into **Working Memory**. The engine executes a **Match-Resolve-Act** cycle:
> 1. **Match:** Evaluates the antecedents (conditions) of all production rules in the Knowledge Base against facts in Working Memory.
> 2. **Resolve:** When multiple rules match, conflict resolution is handled by calculating cumulative Certainty Factors.
> 3. **Act:** Fired rules assert evidence for specific career hypotheses and update their cumulative CF using the MYCIN combination algebra.

### Q3: Explain how Backward Chaining works in your system.
> **Answer:** Backward Chaining is goal-driven. It starts with a hypothetical conclusion (e.g., *"Is candidate eligible for Cloud & DevOps Engineer?"*). The engine locates all production rules whose consequent asserts that career, breaks their antecedents into subgoals (skills, interests, subject grades), and checks if those subgoals are satisfied in the student's working memory (leaf facts). If any subgoals fail, the system pinpoints the exact deficiency.

### Q4: How is uncertainty represented and combined in your system?
> **Answer:** We use the classical **MYCIN Certainty Factor (CF)** formula developed by Shortliffe and Buchanan:
> $$CF_{\text{combined}} = CF_{\text{prior}} + CF_{\text{rule}} \times (1 - CF_{\text{prior}})$$
> When multiple rules provide independent evidence for a career, the confidence asymptotically approaches $1.0$ (100% certainty).

### Q5: Can new rules or careers be added without rewriting the inference engine?
> **Answer:** Yes. Because of the separation of concerns between the Knowledge Base (`expert_system/knowledge_base.py`) and the Inference Engines (`forward_chaining.py` and `backward_chaining.py`), any educator or domain expert can add new production rules or career profiles to the knowledge base dictionary, and the inference engine will immediately parse and evaluate them without modifying a single line of inference code.

---

## 9. Team Members & Contributions (Project Group: 3–4 Members)

| Member Name | Role / Focus Area | Key Modules Developed |
|---|---|---|
| **Member 1 (Lead)** | Knowledge Engineering & Architecture | Rule Base formulation, Career taxonomy, Domain heuristics |
| **Member 2** | AI Inference & Reasoning Engines | Forward & Backward Chaining engines, MYCIN CF propagation |
| **Member 3** | Explanation Facility & Roadmaps | Justification engine (Why/How/Why Not), Action plans |
| **Member 4** | Web Backend & Visual Analytics | Flask server, Chart.js visualizations, What-If simulator |

---
*Developed for AIES (Artificial Intelligence & Expert Systems) — Third Year Computer Engineering.*
