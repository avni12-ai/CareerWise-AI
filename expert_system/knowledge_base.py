"""
CareerWise AI - Knowledge Base Module
Contains declarative domain knowledge:
- Career profiles with benchmark competencies
- Skill taxonomy and definitions
- Production rules (IF-THEN rules with Certainty Factors)
- Academic subject relevance mappings
- Work style and personality preference factors
"""

# ---------------------------------------------------------------------------
# 1. CAREER TAXONOMY & PROFILES
# ---------------------------------------------------------------------------
CAREERS = {
    "software_developer": {
        "id": "software_developer",
        "title": "Software Developer / Full Stack Engineer",
        "category": "Software Engineering",
        "description": "Designs, develops, tests, and maintains robust software systems, enterprise applications, and full-stack web platforms.",
        "icon": "bi-code-slash",
        "badge_color": "#2563eb",
        "core_skills": {
            "python": 3,
            "cpp": 4,
            "java": 3,
            "dsa": 4,
            "dbms": 3,
            "web_dev": 3,
            "os": 3,
            "git": 4
        },
        "critical_skills": ["dsa", "cpp", "python", "dbms"],
        "recommended_interests": ["programming", "problem_solving", "web_development"],
        "ideal_work_style": ["collaborative", "structured", "engineering"],
        "salary_range": "$75,000 - $140,000 / ₹7 - ₹24 LPA",
        "industry_demand": "Very High (Consistent global requirement across all sectors)"
    },
    "data_analyst": {
        "id": "data_analyst",
        "title": "Data Analyst",
        "category": "Data & Analytics",
        "description": "Transforms raw complex datasets into actionable business insights, visual dashboards, and statistical reports to drive strategic decisions.",
        "icon": "bi-bar-chart-line-fill",
        "badge_color": "#059669",
        "core_skills": {
            "python": 3,
            "sql": 5,
            "data_viz": 4,
            "statistics": 4,
            "dbms": 4,
            "excel_sheets": 4
        },
        "critical_skills": ["sql", "data_viz", "statistics", "python"],
        "recommended_interests": ["data_analysis", "mathematics", "business_insights"],
        "ideal_work_style": ["analytical", "communicative", "detail_oriented"],
        "salary_range": "$65,000 - $115,000 / ₹6 - ₹18 LPA",
        "industry_demand": "High (Surging demand in FinTech, Retail, Healthcare, and SaaS)"
    },
    "ai_ml_engineer": {
        "id": "ai_ml_engineer",
        "title": "AI / Machine Learning Engineer",
        "category": "Artificial Intelligence",
        "description": "Researches, architectures, and trains predictive machine learning models, neural networks, and generative AI pipelines deployed at scale.",
        "icon": "bi-cpu-fill",
        "badge_color": "#7c3aed",
        "core_skills": {
            "python": 5,
            "ml_dl": 4,
            "statistics": 5,
            "linear_algebra": 4,
            "dsa": 4,
            "sql": 3,
            "cloud": 3
        },
        "critical_skills": ["python", "ml_dl", "statistics", "linear_algebra"],
        "recommended_interests": ["ai_ml", "mathematics", "research", "neural_networks"],
        "ideal_work_style": ["research_oriented", "experimental", "analytical"],
        "salary_range": "$90,000 - $170,000 / ₹10 - ₹35 LPA",
        "industry_demand": "Extremely High (Highest growth sector driven by GenAI & Automation)"
    },
    "cybersecurity_analyst": {
        "id": "cybersecurity_analyst",
        "title": "Cybersecurity Analyst",
        "category": "Information Security",
        "description": "Protects organizational computer systems, networks, and confidential data against cyber threats, vulnerabilities, intrusions, and breaches.",
        "icon": "bi-shield-lock-fill",
        "badge_color": "#dc2626",
        "core_skills": {
            "networking": 5,
            "os": 4,
            "security_cryptography": 4,
            "bash_scripting": 3,
            "python": 3,
            "cloud": 3
        },
        "critical_skills": ["networking", "os", "security_cryptography"],
        "recommended_interests": ["cybersecurity", "ethical_hacking", "network_defense"],
        "ideal_work_style": ["vigilant", "investigative", "risk_mitigation"],
        "salary_range": "$78,000 - $145,000 / ₹8 - ₹26 LPA",
        "industry_demand": "Critical (Severe global talent shortage across defense and banking)"
    },
    "cloud_engineer": {
        "id": "cloud_engineer",
        "title": "Cloud & DevOps Engineer",
        "category": "Infrastructure & Operations",
        "description": "Architects resilient multi-cloud infrastructure, manages continuous integration/deployment (CI/CD) pipelines, and automates server fleets.",
        "icon": "bi-cloud-check-fill",
        "badge_color": "#0284c7",
        "core_skills": {
            "cloud": 5,
            "docker_k8s": 4,
            "networking": 4,
            "os": 4,
            "bash_scripting": 4,
            "python": 3,
            "git": 4
        },
        "critical_skills": ["cloud", "docker_k8s", "networking", "os"],
        "recommended_interests": ["cloud_infrastructure", "automation", "systems_architecture"],
        "ideal_work_style": ["automation_first", "systematic", "high_availability"],
        "salary_range": "$85,000 - $155,000 / ₹8 - ₹28 LPA",
        "industry_demand": "Very High (Standard infrastructure model across modern enterprises)"
    },
    "data_engineer": {
        "id": "data_engineer",
        "title": "Data Engineer",
        "category": "Data Infrastructure",
        "description": "Builds high-volume distributed data pipelines, ETL architectures, and data warehouses powering analytics and machine learning systems.",
        "icon": "bi-diagram-3-fill",
        "badge_color": "#ea580c",
        "core_skills": {
            "python": 4,
            "sql": 5,
            "distributed_systems": 4,
            "dbms": 5,
            "cloud": 4,
            "docker_k8s": 3
        },
        "critical_skills": ["sql", "python", "dbms", "distributed_systems"],
        "recommended_interests": ["data_pipelines", "big_data", "system_architecture"],
        "ideal_work_style": ["structural", "performance_driven", "scalable"],
        "salary_range": "$82,000 - $150,000 / ₹9 - ₹30 LPA",
        "industry_demand": "Very High (Foundation for all enterprise AI and analytics programs)"
    },
    "ui_ux_frontend_engineer": {
        "id": "ui_ux_frontend_engineer",
        "title": "UI/UX & Frontend Engineer",
        "category": "Design & Frontend Engineering",
        "description": "Bridges visual design and client-side engineering to create responsive, accessible, high-performance web and mobile application interfaces.",
        "icon": "bi-palette-fill",
        "badge_color": "#d946ef",
        "core_skills": {
            "web_dev": 5,
            "javascript": 5,
            "ui_ux_design": 4,
            "git": 3,
            "dbms": 2
        },
        "critical_skills": ["web_dev", "javascript", "ui_ux_design"],
        "recommended_interests": ["user_interfaces", "creative_design", "web_development"],
        "ideal_work_style": ["creative", "user_centric", "visual"],
        "salary_range": "$70,000 - $130,000 / ₹6 - ₹20 LPA",
        "industry_demand": "Steady & High (Vital for customer-facing digital applications)"
    },
    "systems_embedded_engineer": {
        "id": "systems_embedded_engineer",
        "title": "Systems & Embedded Engineer",
        "category": "Low-Level & Hardware Systems",
        "description": "Develops firmware, device drivers, real-time operating systems (RTOS), and IoT systems running directly on resource-constrained hardware.",
        "icon": "bi-motherboard-fill",
        "badge_color": "#475569",
        "core_skills": {
            "cpp": 5,
            "c_lang": 5,
            "os": 5,
            "embedded_iot": 4,
            "computer_architecture": 4,
            "networking": 3
        },
        "critical_skills": ["c_lang", "cpp", "os", "computer_architecture"],
        "recommended_interests": ["hardware_software", "embedded_systems", "low_level_programming"],
        "ideal_work_style": ["precision_focused", "hardware_integrated", "low_level"],
        "salary_range": "$80,000 - $145,000 / ₹7 - ₹25 LPA",
        "industry_demand": "High (Autonomous vehicles, robotics, IoT devices, edge computing)"
    }
}

# ---------------------------------------------------------------------------
# 2. TAXONOMY: SKILLS, INTERESTS, SUBJECTS, WORK STYLES
# ---------------------------------------------------------------------------

SKILLS_METADATA = {
    "cpp": {"name": "C / C++", "category": "Programming Languages", "desc": "Object-oriented, memory management, pointers, and performance-critical systems."},
    "python": {"name": "Python", "category": "Programming Languages", "desc": "General purpose scripting, data science libraries, automation, and backend."},
    "java": {"name": "Java", "category": "Programming Languages", "desc": "Enterprise OOP, Spring framework, multithreading, and platform independence."},
    "javascript": {"name": "JavaScript / TypeScript", "category": "Programming Languages", "desc": "Modern async ES6+, React/Node ecosystem, browser DOM manipulation."},
    "sql": {"name": "SQL & Relational DBs", "category": "Databases & Data", "desc": "Complex queries, joins, indexes, normalization, schema design, and stored procedures."},
    "dsa": {"name": "Data Structures & Algorithms", "category": "Core Computer Science", "desc": "Trees, graphs, dynamic programming, time/space complexity, sorting/searching."},
    "os": {"name": "Operating Systems", "category": "Core Computer Science", "desc": "Processes, threads, synchronization, virtual memory, scheduling, and system calls."},
    "networking": {"name": "Computer Networks", "category": "Core Computer Science", "desc": "TCP/IP, OSI model, routing, DNS, HTTP/HTTPS, firewalls, and sockets."},
    "dbms": {"name": "DBMS Concepts", "category": "Databases & Data", "desc": "ACID properties, transactions, concurrency control, NoSQL vs SQL architectures."},
    "cloud": {"name": "Cloud Computing (AWS/GCP/Azure)", "category": "Infrastructure", "desc": "EC2/Compute, S3/Storage, IAM, VPC, serverless functions, cloud architectures."},
    "docker_k8s": {"name": "Docker & Kubernetes", "category": "Infrastructure", "desc": "Containerization, Dockerfiles, pod orchestration, deployments, service discovery."},
    "ml_dl": {"name": "Machine Learning & Deep Learning", "category": "Artificial Intelligence", "desc": "Supervised/unsupervised learning, scikit-learn, PyTorch, CNNs, transformers."},
    "statistics": {"name": "Statistics & Probability", "category": "Mathematics & Data", "desc": "Hypothesis testing, distributions, regression, Bayes theorem, variance/covariance."},
    "linear_algebra": {"name": "Linear Algebra & Calculus", "category": "Mathematics & Data", "desc": "Matrix operations, eigenvalues, vector spaces, gradient descent optimization."},
    "data_viz": {"name": "Data Visualization & BI", "category": "Databases & Data", "desc": "Tableau, PowerBI, Matplotlib, Seaborn, interactive dashboards."},
    "security_cryptography": {"name": "Security & Cryptography", "category": "Information Security", "desc": "Symmetric/asymmetric crypto, hashing, penetration testing, threat modeling."},
    "bash_scripting": {"name": "Linux / Bash Shell", "category": "Infrastructure", "desc": "CLI navigation, shell scripting, sed/awk, permissions, process monitoring."},
    "web_dev": {"name": "Web Technologies (HTML/CSS/UI)", "category": "Design & Frontend", "desc": "Responsive web layouts, flexbox/grid, CSS animations, REST APIs."},
    "ui_ux_design": {"name": "UI/UX Design Principles", "category": "Design & Frontend", "desc": "Wireframing, Figma, user research, typography, usability heuristics."},
    "c_lang": {"name": "C Programming", "category": "Low-Level & Hardware Systems", "desc": "Pointers, memory allocation, bit manipulation, hardware registers."},
    "embedded_iot": {"name": "Embedded Systems & IoT", "category": "Low-Level & Hardware Systems", "desc": "Microcontrollers (Arduino/ESP32/ARM), GPIO, I2C/SPI, sensors, RTOS."},
    "distributed_systems": {"name": "Distributed Systems", "category": "Infrastructure", "desc": "CAP theorem, consensus, Apache Kafka, Spark, partitioning, sharding."},
    "git": {"name": "Git & Version Control", "category": "Software Engineering", "desc": "Branching strategies, merge conflict resolution, CI/CD integrations, pull requests."}
}

INTERESTS_METADATA = {
    "programming": {"name": "Algorithmic Coding & Software Construction", "desc": "Writing clean, maintainable code to solve algorithmic and business problems."},
    "mathematics": {"name": "Mathematics & Theoretical Foundations", "desc": "Enjoying proofs, matrix transformations, calculus, and statistical formulas."},
    "ai_ml": {"name": "Artificial Intelligence & Autonomous Systems", "desc": "Building systems that learn patterns from data and mimic cognitive functions."},
    "cybersecurity": {"name": "Cyber Defense, Ethical Hacking & Forensics", "desc": "Investigating exploits, securing infrastructures, and analyzing vulnerabilities."},
    "cloud_infrastructure": {"name": "Cloud Architecture & Scalability", "desc": "Configuring distributed cloud servers, autoscaling, and zero-downtime platforms."},
    "data_analysis": {"name": "Exploratory Data Analysis & Business Insights", "desc": "Finding hidden stories, trends, and actionable metrics in messy datasets."},
    "user_interfaces": {"name": "Interactive UI/UX & Visual Aesthetics", "desc": "Crafting intuitive user interfaces, pleasant micro-interactions, and visual designs."},
    "hardware_software": {"name": "Hardware Interfacing & Microcontrollers", "desc": "Tinkering with physical microchips, sensors, robotics, and low-level drivers."},
    "automation": {"name": "DevOps, CI/CD & Workflow Automation", "desc": "Eliminating repetitive manual engineering tasks with scripts and automated pipelines."},
    "data_pipelines": {"name": "Big Data Engineering & Streaming Architecture", "desc": "Designing high-throughput streaming systems, Kafka, and big data transformations."}
}

SUBJECTS_METADATA = {
    "dsa_sub": {"name": "Data Structures & Algorithms", "key_for": ["software_developer", "ai_ml_engineer"]},
    "dbms_sub": {"name": "Database Management Systems", "key_for": ["data_analyst", "data_engineer", "software_developer"]},
    "os_sub": {"name": "Operating Systems", "key_for": ["cybersecurity_analyst", "systems_embedded_engineer", "cloud_engineer"]},
    "cn_sub": {"name": "Computer Networks", "key_for": ["cybersecurity_analyst", "cloud_engineer"]},
    "ai_sub": {"name": "Artificial Intelligence / ML", "key_for": ["ai_ml_engineer"]},
    "stats_math_sub": {"name": "Applied Statistics & Linear Algebra", "key_for": ["ai_ml_engineer", "data_analyst"]},
    "security_sub": {"name": "Information & Cyber Security", "key_for": ["cybersecurity_analyst"]},
    "cloud_sub": {"name": "Cloud Computing & Virtualization", "key_for": ["cloud_engineer", "data_engineer"]},
    "web_sub": {"name": "Web Technology & Full Stack", "key_for": ["ui_ux_frontend_engineer", "software_developer"]},
    "microprocessor_sub": {"name": "Microprocessors & Comp. Architecture", "key_for": ["systems_embedded_engineer"]}
}

WORK_STYLES_METADATA = {
    "work_preference": {
        "title": "Preferred Work Mode",
        "options": [
            {"id": "research", "label": "Research & Mathematical Exploration (Deep experimentation, papers, theory)"},
            {"id": "building", "label": "Engineering & Product Construction (Writing production code, shipping features)"},
            {"id": "investigation", "label": "Investigation & System Defense (Auditing, threat detection, problem diagnosis)"},
            {"id": "visual_design", "label": "Creative & Human-Centered Design (User empathy, prototyping, styling)"},
            {"id": "infrastructure", "label": "Operational Excellence & Automation (Reliability, uptime, pipelines)"}
        ]
    },
    "organization_type": {
        "title": "Preferred Environment",
        "options": [
            {"id": "fast_startup", "label": "Fast-Paced Startup (High ownership, broad multi-hat responsibilities)"},
            {"id": "enterprise", "label": "Global Tech Enterprise (Specialized domain, high scale, structured process)"},
            {"id": "research_lab", "label": "R&D Lab / Higher Academia (Cutting-edge frontier tech exploration)"}
        ]
    }
}

# ---------------------------------------------------------------------------
# 3. PRODUCTION RULES (EXPERT SYSTEM RULE BASE)
# ---------------------------------------------------------------------------
# Each rule represents domain heuristic compiled from career guidance experts.
# Format:
# - id: Unique Rule identifier
# - name: Human-readable rule title
# - category: Core Competency / Academic / Interest / Heuristic
# - antecedents: Conditions that must evaluate to True (or threshold check)
# - consequent: Dict mapping career_id -> Certainty Factor (CF: 0.0 to 1.0)
# - explanation: Viva-ready rationale explaining why this rule fires.
# ---------------------------------------------------------------------------

PRODUCTION_RULES = [
    # --- AI & MACHINE LEARNING RULES ---
    {
        "id": "RULE_AIML_01",
        "name": "AI/ML Core Foundations Rule",
        "category": "Core Competency",
        "conditions": {
            "skills": {"python": (">=", 4), "ml_dl": (">=", 3)},
            "interests": ["ai_ml"]
        },
        "consequent": {"ai_ml_engineer": 0.88},
        "explanation": "High Python proficiency combined with machine learning competence and genuine AI interest strongly aligns with AI/ML engineering."
    },
    {
        "id": "RULE_AIML_02",
        "name": "Mathematical & Statistical Rigor for AI Rule",
        "category": "Academic Synergy",
        "conditions": {
            "skills": {"statistics": (">=", 4), "linear_algebra": (">=", 3)},
            "subjects": {"stats_math_sub": (">=", "A")}
        },
        "consequent": {"ai_ml_engineer": 0.75, "data_analyst": 0.55},
        "explanation": "Solid foundations in linear algebra, statistics, and university math courses are prerequisites for advanced ML algorithm development."
    },
    {
        "id": "RULE_AIML_03",
        "name": "Deep Learning & Research Orientation Rule",
        "category": "Interest Heuristic",
        "conditions": {
            "interests": ["ai_ml", "mathematics"],
            "work_style": {"work_preference": "research"}
        },
        "consequent": {"ai_ml_engineer": 0.80},
        "explanation": "Students preferring research and mathematical exploration are prime candidates for AI researcher or model architect roles."
    },

    # --- DATA ANALYST RULES ---
    {
        "id": "RULE_DA_01",
        "name": "Data Analytics Core Triad Rule",
        "category": "Core Competency",
        "conditions": {
            "skills": {"sql": (">=", 4), "data_viz": (">=", 3)},
            "interests": ["data_analysis"]
        },
        "consequent": {"data_analyst": 0.86},
        "explanation": "Expertise in SQL query optimization and dashboard visualization paired with an analytical mindset is the core requirement for Data Analysts."
    },
    {
        "id": "RULE_DA_02",
        "name": "Business Insight & Statistical Interpretation Rule",
        "category": "Skill Synergy",
        "conditions": {
            "skills": {"statistics": (">=", 3), "excel_sheets": (">=", 3), "python": (">=", 2)}
        },
        "consequent": {"data_analyst": 0.72},
        "explanation": "Statistical reasoning combined with tabular tooling (Excel/Sheets) and Python data processing indicates high data analysis capability."
    },
    {
        "id": "RULE_DA_03",
        "name": "DBMS Academic Mastery for Analytics Rule",
        "category": "Academic Synergy",
        "conditions": {
            "subjects": {"dbms_sub": (">=", "A")},
            "skills": {"sql": (">=", 3)}
        },
        "consequent": {"data_analyst": 0.65, "data_engineer": 0.50},
        "explanation": "Top academic marks in Database Management Systems provide the relational modeling foundation for analytical reporting."
    },

    # --- SOFTWARE DEVELOPER RULES ---
    {
        "id": "RULE_SWE_01",
        "name": "Algorithmic & Engineering Core Rule",
        "category": "Core Competency",
        "conditions": {
            "skills": {"dsa": (">=", 4), "git": (">=", 3)},
            "interests": ["programming"]
        },
        "consequent": {"software_developer": 0.90},
        "explanation": "Strong Data Structures & Algorithms proficiency, version control hygiene, and passion for software building are hallmark traits of Software Developers."
    },
    {
        "id": "RULE_SWE_02",
        "name": "Generalist Polyglot OOP Rule",
        "category": "Skill Synergy",
        "conditions": {
            "skills": {"cpp": (">=", 3), "java": (">=", 3), "dbms": (">=", 3)}
        },
        "consequent": {"software_developer": 0.78},
        "explanation": "Competence in compiled object-oriented languages (C++/Java) combined with database concepts indicates strong backend/enterprise software engineering aptitude."
    },
    {
        "id": "RULE_SWE_03",
        "name": "Product Construction Preference Rule",
        "category": "Interest Heuristic",
        "conditions": {
            "work_style": {"work_preference": "building"},
            "subjects": {"dsa_sub": (">=", "A")}
        },
        "consequent": {"software_developer": 0.75},
        "explanation": "Preference for shipping working code and high marks in university DSA coursework correlate strongly with career success as a software engineer."
    },

    # --- CYBERSECURITY ANALYST RULES ---
    {
        "id": "RULE_SEC_01",
        "name": "Cyber Defense & Network Security Rule",
        "category": "Core Competency",
        "conditions": {
            "skills": {"networking": (">=", 4), "security_cryptography": (">=", 3)},
            "interests": ["cybersecurity"]
        },
        "consequent": {"cybersecurity_analyst": 0.92},
        "explanation": "Deep computer networking expertise combined with cryptographic knowledge and interest in ethical hacking directly indicates a Cybersecurity Analyst profile."
    },
    {
        "id": "RULE_SEC_02",
        "name": "Operating System Internals & Bash Scripting Rule",
        "category": "Skill Synergy",
        "conditions": {
            "skills": {"os": (">=", 4), "bash_scripting": (">=", 3)}
        },
        "consequent": {"cybersecurity_analyst": 0.70, "cloud_engineer": 0.60, "systems_embedded_engineer": 0.50},
        "explanation": "Proficiency in operating system internals and shell scripting is essential for vulnerability discovery, digital forensics, and server hardening."
    },
    {
        "id": "RULE_SEC_03",
        "name": "Investigative Defensive Mindset Rule",
        "category": "Interest Heuristic",
        "conditions": {
            "work_style": {"work_preference": "investigation"},
            "subjects": {"cn_sub": (">=", "A"), "security_sub": (">=", "A")}
        },
        "consequent": {"cybersecurity_analyst": 0.85},
        "explanation": "Investigative psychological temperament backed by high marks in Computer Networks and Information Security is an ideal cybersecurity profile."
    },

    # --- CLOUD & DEVOPS ENGINEER RULES ---
    {
        "id": "RULE_CLOUD_01",
        "name": "Cloud Infrastructure & Containerization Rule",
        "category": "Core Competency",
        "conditions": {
            "skills": {"cloud": (">=", 4), "docker_k8s": (">=", 3)},
            "interests": ["cloud_infrastructure"]
        },
        "consequent": {"cloud_engineer": 0.90},
        "explanation": "Hands-on cloud architecture and container orchestration (Docker/K8s) coupled with infrastructure enthusiasm strongly indicates a Cloud/DevOps engineer."
    },
    {
        "id": "RULE_CLOUD_02",
        "name": "Automated Deployment & Reliability Rule",
        "category": "Skill Synergy",
        "conditions": {
            "skills": {"networking": (">=", 3), "bash_scripting": (">=", 3), "git": (">=", 3)},
            "interests": ["automation"]
        },
        "consequent": {"cloud_engineer": 0.80},
        "explanation": "Combining network routing knowledge with automation scripting and version control forms the bedrock of Site Reliability Engineering (SRE) and DevOps."
    },
    {
        "id": "RULE_CLOUD_03",
        "name": "Cloud Academic Alignment Rule",
        "category": "Academic Synergy",
        "conditions": {
            "subjects": {"cloud_sub": (">=", "A"), "os_sub": (">=", "B")}
        },
        "consequent": {"cloud_engineer": 0.68},
        "explanation": "Academic excellence in Cloud Computing and Virtualization subjects validates theoretical preparedness for cloud operations."
    },

    # --- DATA ENGINEER RULES ---
    {
        "id": "RULE_DE_01",
        "name": "Big Data Pipelines & Architecture Rule",
        "category": "Core Competency",
        "conditions": {
            "skills": {"sql": (">=", 4), "distributed_systems": (">=", 3), "python": (">=", 3)},
            "interests": ["data_pipelines"]
        },
        "consequent": {"data_engineer": 0.91},
        "explanation": "Advanced SQL, distributed computing systems knowledge, and data pipeline interest are the defining pillars of modern Data Engineering."
    },
    {
        "id": "RULE_DE_02",
        "name": "Data Storage Systems & Infrastructure Rule",
        "category": "Skill Synergy",
        "conditions": {
            "skills": {"dbms": (">=", 4), "cloud": (">=", 3)}
        },
        "consequent": {"data_engineer": 0.74, "cloud_engineer": 0.50},
        "explanation": "Strong knowledge of database engines, transaction locks, and cloud data warehousing provides the foundational capability for large data platform engineering."
    },

    # --- UI/UX FRONTEND ENGINEER RULES ---
    {
        "id": "RULE_UI_01",
        "name": "Client-Side Engineering & Visual Design Rule",
        "category": "Core Competency",
        "conditions": {
            "skills": {"web_dev": (">=", 4), "javascript": (">=", 4)},
            "interests": ["user_interfaces"]
        },
        "consequent": {"ui_ux_frontend_engineer": 0.93},
        "explanation": "Expert client-side web technology, modern JavaScript frameworks, and enthusiasm for user interfaces are the core drivers of Frontend engineering."
    },
    {
        "id": "RULE_UI_02",
        "name": "Human-Centered Design Preference Rule",
        "category": "Interest Heuristic",
        "conditions": {
            "skills": {"ui_ux_design": (">=", 3)},
            "work_style": {"work_preference": "visual_design"}
        },
        "consequent": {"ui_ux_frontend_engineer": 0.82},
        "explanation": "Aesthetic design sensibilities and user empathy paired with visual design tools differentiate premier frontend and UX designers."
    },

    # --- SYSTEMS & EMBEDDED ENGINEER RULES ---
    {
        "id": "RULE_EMBED_01",
        "name": "Low-Level Hardware & Embedded Systems Rule",
        "category": "Core Competency",
        "conditions": {
            "skills": {"c_lang": (">=", 4), "cpp": (">=", 4), "os": (">=", 4)},
            "interests": ["hardware_software"]
        },
        "consequent": {"systems_embedded_engineer": 0.94},
        "explanation": "High proficiency in C, C++, and operating system internals combined with low-level hardware curiosity is the exact formula for embedded engineering."
    },
    {
        "id": "RULE_EMBED_02",
        "name": "Microprocessor & IoT Architecture Rule",
        "category": "Academic Synergy",
        "conditions": {
            "skills": {"embedded_iot": (">=", 3), "computer_architecture": (">=", 3)},
            "subjects": {"microprocessor_sub": (">=", "A")}
        },
        "consequent": {"systems_embedded_engineer": 0.85},
        "explanation": "Academic mastery of microprocessors and computer architecture directly translates to firmware development and IoT device engineering."
    }
]

# ---------------------------------------------------------------------------
# 4. PRESET TEST PROFILES (FOR COLLEGE DEMONSTRATION & VIVA)
# ---------------------------------------------------------------------------
PRESET_PROFILES = {
    "profile_ai": {
        "name": "Aarav Sharma (AI & Data Science Enthusiast)",
        "desc": "Strong in Python, ML, Linear Algebra, and Statistics. Enjoys research and predictive modeling.",
        "skills": {
            "python": 5, "ml_dl": 4, "statistics": 5, "linear_algebra": 5,
            "dsa": 4, "sql": 3, "cloud": 3, "cpp": 3, "git": 4,
            "dbms": 3, "os": 3, "networking": 2, "security_cryptography": 2,
            "bash_scripting": 3, "web_dev": 2, "docker_k8s": 2, "c_lang": 2,
            "ui_ux_design": 1, "javascript": 2, "data_viz": 4, "excel_sheets": 3,
            "embedded_iot": 1, "computer_architecture": 2, "distributed_systems": 3
        },
        "interests": ["ai_ml", "mathematics", "data_analysis"],
        "subjects": {
            "ai_sub": "A+", "stats_math_sub": "A+", "dsa_sub": "A",
            "dbms_sub": "A", "cn_sub": "B", "os_sub": "B",
            "cloud_sub": "B", "security_sub": "C", "web_sub": "B", "microprocessor_sub": "C"
        },
        "work_style": {"work_preference": "research", "organization_type": "research_lab"}
    },
    "profile_cyber": {
        "name": "Neha Patel (Cyber Defense & Systems Specialist)",
        "desc": "Passionate about computer networks, OS security, cryptography, and penetration testing.",
        "skills": {
            "networking": 5, "os": 5, "security_cryptography": 4, "bash_scripting": 4,
            "python": 3, "c_lang": 4, "cpp": 3, "cloud": 3, "git": 3,
            "dsa": 3, "dbms": 3, "sql": 3, "docker_k8s": 3, "web_dev": 2,
            "javascript": 2, "data_viz": 2, "excel_sheets": 2, "statistics": 3,
            "linear_algebra": 2, "ml_dl": 1, "ui_ux_design": 1, "embedded_iot": 2,
            "computer_architecture": 4, "distributed_systems": 2
        },
        "interests": ["cybersecurity", "hardware_software"],
        "subjects": {
            "security_sub": "A+", "cn_sub": "A+", "os_sub": "A+",
            "microprocessor_sub": "A", "dsa_sub": "B", "cloud_sub": "B",
            "dbms_sub": "B", "stats_math_sub": "B", "ai_sub": "C", "web_sub": "C"
        },
        "work_style": {"work_preference": "investigation", "organization_type": "enterprise"}
    },
    "profile_cloud": {
        "name": "Rohan Verma (Cloud Architect & DevOps Builder)",
        "desc": "Hands-on with AWS/GCP, Docker, Kubernetes, Linux shell, and CI/CD automation pipelines.",
        "skills": {
            "cloud": 5, "docker_k8s": 5, "networking": 4, "os": 4, "bash_scripting": 5,
            "git": 4, "python": 3, "distributed_systems": 4, "dbms": 3, "sql": 3,
            "dsa": 3, "cpp": 2, "c_lang": 2, "web_dev": 2, "javascript": 2,
            "security_cryptography": 3, "statistics": 2, "linear_algebra": 2, "ml_dl": 1,
            "data_viz": 2, "excel_sheets": 2, "ui_ux_design": 1, "embedded_iot": 1,
            "computer_architecture": 2
        },
        "interests": ["cloud_infrastructure", "automation"],
        "subjects": {
            "cloud_sub": "A+", "os_sub": "A", "cn_sub": "A",
            "dbms_sub": "B", "dsa_sub": "B", "security_sub": "B",
            "web_sub": "B", "stats_math_sub": "C", "ai_sub": "C", "microprocessor_sub": "C"
        },
        "work_style": {"work_preference": "infrastructure", "organization_type": "fast_startup"}
    },
    "profile_swe": {
        "name": "Sneha Kulkarni (Full-Stack & Algorithms Enthusiast)",
        "desc": "Cracked DSA, strong in C++, Java, Web development, Git, and database normalization.",
        "skills": {
            "dsa": 5, "cpp": 4, "java": 4, "python": 4, "dbms": 4, "sql": 4,
            "web_dev": 4, "javascript": 4, "git": 5, "os": 3, "networking": 3,
            "cloud": 3, "docker_k8s": 3, "statistics": 3, "data_viz": 3,
            "bash_scripting": 3, "c_lang": 3, "linear_algebra": 3, "security_cryptography": 2,
            "ml_dl": 2, "ui_ux_design": 3, "distributed_systems": 3,
            "excel_sheets": 3, "embedded_iot": 1, "computer_architecture": 2
        },
        "interests": ["programming", "web_development"],
        "subjects": {
            "dsa_sub": "A+", "dbms_sub": "A+", "web_sub": "A+",
            "os_sub": "A", "cn_sub": "B", "cloud_sub": "B",
            "stats_math_sub": "B", "ai_sub": "B", "security_sub": "B", "microprocessor_sub": "C"
        },
        "work_style": {"work_preference": "building", "organization_type": "enterprise"}
    }
}
