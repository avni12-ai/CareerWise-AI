"""
CareerWise AI - Roadmap & Action Plan Generator
Generates personalized, phased learning roadmaps to bridge skill gaps:
1. Phase 1: Foundational Bridge (0-2 Months)
2. Phase 2: Intermediate Specialization & Mini-Projects (3-4 Months)
3. Phase 3: Advanced Capstone & Industry Certifications (5-6 Months)
"""

from typing import Dict, List, Any
from expert_system.knowledge_base import SKILLS_METADATA

ROADMAP_DATABASE = {
    "software_developer": {
        "title": "Software Developer / Full Stack Roadmap",
        "phase_1": {
            "title": "Phase 1: Advanced Algorithms & System Foundations",
            "duration": "Months 1 - 2",
            "goals": [
                "Master Advanced Data Structures (Graphs, Tries, Segment Trees, Dynamic Programming).",
                "Deepen Object-Oriented Design (SOLID principles, Factory, Strategy, Observer patterns).",
                "Build proficiency in Git workflow (rebasing, interactive staging, branching models)."
            ],
            "resources": [
                {"name": "NeetCode 150 / LeetCode DSA Patterns", "type": "Interactive Problem Solving"},
                {"name": "Refactoring.Guru: Design Patterns in Depth", "type": "Free Architecture Guide"},
                {"name": "Full Stack Open (University of Helsinki)", "type": "Open Source Course"}
            ]
        },
        "phase_2": {
            "title": "Phase 2: Full-Stack Architecture & API Design",
            "duration": "Months 3 - 4",
            "goals": [
                "Develop RESTful & GraphQL microservices with JWT authentication & rate limiting.",
                "Design optimized relational schemas with PostgreSQL, indexing, and connection pooling.",
                "Implement automated testing suites (Unit, Integration, and Mocking)."
            ],
            "resources": [
                {"name": "Designing Data-Intensive Applications (M. Kleppmann)", "type": "Book"},
                {"name": "Docker & Container Basics on Play-with-Docker", "type": "Hands-on Lab"}
            ]
        },
        "phase_3": {
            "title": "Phase 3: High-Performance Capstone & Placement Prep",
            "duration": "Months 5 - 6",
            "goals": [
                "Build and deploy a scalable microservices platform with Redis caching and CI/CD.",
                "Practice mock technical interviews and system design rounds.",
                "Contribute meaningful PRs to an active open-source GitHub repository."
            ],
            "capstone_project": "Scalable Real-Time Collaborative Workspace with WebSockets, Redis pub/sub, and PostgreSQL.",
            "certifications": [
                "AWS Certified Developer - Associate",
                "Meta Front-End / Back-End Professional Certificate"
            ]
        }
    },
    "data_analyst": {
        "title": "Data Analyst Career Acceleration Roadmap",
        "phase_1": {
            "title": "Phase 1: Advanced SQL & Data Manipulation",
            "duration": "Months 1 - 2",
            "goals": [
                "Master complex SQL queries: Window Functions, CTEs, self-joins, and query execution plans.",
                "Learn Python data cleaning libraries: Pandas dataframes, NumPy arrays, handling missing values.",
                "Understand statistical significance, hypothesis testing (p-values, z-scores, ANOVA)."
            ],
            "resources": [
                {"name": "Mode Analytics SQL Tutorial for Data Analysis", "type": "Free Tutorial"},
                {"name": "Python for Data Analysis (Wes McKinney)", "type": "Book"},
                {"name": "Khan Academy: Statistics and Probability", "type": "Video Course"}
            ]
        },
        "phase_2": {
            "title": "Phase 2: Visual Storytelling & BI Dashboards",
            "duration": "Months 3 - 4",
            "goals": [
                "Create production-ready interactive dashboards using Power BI or Tableau.",
                "Master DAX measures, data modeling, star schemas, and dashboard UX principles.",
                "Perform exploratory data analysis (EDA) using Seaborn and Plotly."
            ],
            "resources": [
                {"name": "Microsoft Power BI Guided Learning", "type": "Official Microsoft Docs"},
                {"name": "Kaggle Micro-courses: Data Visualization", "type": "Hands-on Interactive"}
            ]
        },
        "phase_3": {
            "title": "Phase 3: Executive Reporting & Business Case Studies",
            "duration": "Months 5 - 6",
            "goals": [
                "Analyze real-world business datasets (Churn Prediction, E-commerce Retention, Financial KPI tracking).",
                "Formulate executive memos translating complex metrics into actionable revenue insights.",
                "Publish an interactive portfolio on GitHub and NovyPro / Tableau Public."
            ],
            "capstone_project": "End-to-End Enterprise Sales & Churn Analytics Dashboard with Automated ETL and Power BI.",
            "certifications": [
                "Microsoft Certified: Power BI Data Analyst Associate (PL-300)",
                "Google Data Analytics Professional Certificate"
            ]
        }
    },
    "ai_ml_engineer": {
        "title": "AI & Machine Learning Engineer Mastery Roadmap",
        "phase_1": {
            "title": "Phase 1: Mathematical Foundations & Classical ML",
            "duration": "Months 1 - 2",
            "goals": [
                "Deep dive into Linear Algebra (Eigenvectors, SVD, Matrix decomposition) and Multivariate Calculus.",
                "Implement classical ML algorithms from scratch: Gradient Descent, Logistic Regression, Random Forests, SVMs.",
                "Master Scikit-learn pipelines, cross-validation strategies, and hyperparameter tuning."
            ],
            "resources": [
                {"name": "Mathematics for Machine Learning (Deisenroth et al.)", "type": "Free PDF Book"},
                {"name": "Andrew Ng's Machine Learning Specialization (Coursera/DeepLearning.AI)", "type": "Course"},
                {"name": "Fast.ai: Practical Deep Learning for Coders", "type": "Hands-on Course"}
            ]
        },
        "phase_2": {
            "title": "Phase 2: Deep Learning & Modern Frameworks",
            "duration": "Months 3 - 4",
            "goals": [
                "Master PyTorch: Tensors, autograd, custom Dataset/DataLoader, and nn.Module architectures.",
                "Train Convolutional Networks (CNNs) for Computer Vision and Transformers for NLP.",
                "Understand Attention Mechanisms, Hugging Face Transformers, and LoRA/Fine-Tuning techniques."
            ],
            "resources": [
                {"name": "Hugging Face NLP Course", "type": "Interactive Tutorials"},
                {"name": "Stanford CS231n / CS224n Lecture Series", "type": "University Lectures"}
            ]
        },
        "phase_3": {
            "title": "Phase 3: MLOps & Production AI Deployment",
            "duration": "Months 5 - 6",
            "goals": [
                "Deploy trained models as low-latency microservices with FastAPI, ONNX Runtime, and Docker.",
                "Implement experiment tracking with MLflow/Weights & Biases and model drift monitoring.",
                "Build and deploy an LLM RAG (Retrieval Augmented Generation) system with vector databases."
            ],
            "capstone_project": "Domain-Specific Agentic RAG Pipeline with Vector Search, LangChain/LlamaIndex, and Fast Inference API.",
            "certifications": [
                "TensorFlow Developer Certificate / DeepLearning.AI Specialization",
                "AWS Certified Machine Learning - Specialty"
            ]
        }
    },
    "cybersecurity_analyst": {
        "title": "Cybersecurity Analyst & Defense Roadmap",
        "phase_1": {
            "title": "Phase 1: Network Protocols & Linux Hardening",
            "duration": "Months 1 - 2",
            "goals": [
                "Analyze network packets at byte-level using Wireshark and tcpdump (TCP handshakes, DNS leaks, TLS handshakes).",
                "Master Linux CLI administration, user privilege management, iptables firewalls, and SSH key policies.",
                "Understand cryptography: AES symmetric encryption, RSA/ECC public key cryptography, SHA-256 hashing."
            ],
            "resources": [
                {"name": "TryHackMe: Complete Beginner & Pre-Security Paths", "type": "Interactive Labs"},
                {"name": "OverTheWire: Bandit Wargame (Linux Shell)", "type": "Gamified Security Lab"},
                {"name": "Professor Messer's CompTIA Network+ Series", "type": "Free Video Training"}
            ]
        },
        "phase_2": {
            "title": "Phase 2: Vulnerability Assessment & SIEM Monitoring",
            "duration": "Months 3 - 4",
            "goals": [
                "Configure and monitor Security Information and Event Management (SIEM) tools (Splunk, Elastic SIEM).",
                "Perform web security testing against OWASP Top 10 vulnerabilities (SQLi, XSS, CSRF, IDOR).",
                "Conduct automated vulnerability scans using Nmap, Nessus, and Burp Suite Community."
            ],
            "resources": [
                {"name": "PortSwigger Web Security Academy", "type": "Industry Benchmark Labs"},
                {"name": "Splunk Free Fundamentals Training", "type": "Official Vendor Course"}
            ]
        },
        "phase_3": {
            "title": "Phase 3: Threat Hunting, Incident Response & Certifications",
            "duration": "Months 5 - 6",
            "goals": [
                "Construct incident response playbooks for ransomware containment and phishing analysis.",
                "Participate in CTF (Capture The Flag) competitions on HackTheBox.",
                "Earn an entry-level professional cyber credential."
            ],
            "capstone_project": "Isolated Cloud Honeypot & SIEM Monitoring Lab with Real-Time Intrusion Alerting and Automated Forensic Logging.",
            "certifications": [
                "CompTIA Security+ (SY0-701)",
                "Certified in Cybersecurity (ISC2 CC)"
            ]
        }
    },
    "cloud_engineer": {
        "title": "Cloud & DevOps Engineering Roadmap",
        "phase_1": {
            "title": "Phase 1: Cloud Core & Linux Automation",
            "duration": "Months 1 - 2",
            "goals": [
                "Master fundamental cloud architecture (VPCs, Subnets, Routing tables, Security Groups, IAM roles).",
                "Automate system administration with Bash and Python boto3 scripts.",
                "Learn Git branch management and GitHub Actions automated workflow syntax."
            ],
            "resources": [
                {"name": "AWS Skill Builder Free Digital Training", "type": "Official Vendor Labs"},
                {"name": "Linux Journey (linuxjourney.com)", "type": "Interactive Learning"}
            ]
        },
        "phase_2": {
            "title": "Phase 2: Containers & Infrastructure as Code (IaC)",
            "duration": "Months 3 - 4",
            "goals": [
                "Write multi-stage optimized Dockerfiles and orchestrate multi-container stacks with Docker Compose.",
                "Provision cloud infrastructure declaratively using Terraform (HCL, state management, modules).",
                "Deploy and manage Kubernetes clusters (Pods, Services, Deployments, ConfigMaps, Ingress)."
            ],
            "resources": [
                {"name": "Learn Terraform by HashiCorp", "type": "Official Tutorial"},
                {"name": "Kubernetes the Hard Way (Kelsey Hightower)", "type": "Deep Dive Guide"}
            ]
        },
        "phase_3": {
            "title": "Phase 3: Production CI/CD & Observability",
            "duration": "Months 5 - 6",
            "goals": [
                "Build robust CI/CD pipelines deploying containerized apps with zero downtime (Blue/Green, Canary).",
                "Implement monitoring, metrics, and alerting using Prometheus and Grafana dashboards.",
                "Prepare for industry cloud certification exams."
            ],
            "capstone_project": "End-to-End GitOps Multi-Cloud Infrastructure with Terraform, Kubernetes, Helm, ArgoCD, and Prometheus.",
            "certifications": [
                "AWS Certified Solutions Architect - Associate (SAA-C03)",
                "Certified Kubernetes Administrator (CKA)"
            ]
        }
    },
    "data_engineer": {
        "title": "Data Engineering & Big Data Roadmap",
        "phase_1": {
            "title": "Phase 1: Advanced Relational Modeling & Python ETL",
            "duration": "Months 1 - 2",
            "goals": [
                "Design optimized dimensional data models (Star and Snowflake schemas).",
                "Write robust Python data ingestion scripts handling REST APIs, JSON, and Parquet columnar formats.",
                "Understand database indexing, partition pruning, and execution plans in PostgreSQL."
            ],
            "resources": [
                {"name": "The Data Engineering Cookbook (Andreas Kretz)", "type": "Free GitHub Repository"},
                {"name": "DataCamp: Data Engineering Track", "type": "Interactive Course"}
            ]
        },
        "phase_2": {
            "title": "Phase 2: Distributed Data Processing with Spark",
            "duration": "Months 3 - 4",
            "goals": [
                "Process multi-gigabyte datasets using PySpark DataFrames, partitions, and broadcast joins.",
                "Implement orchestrated pipeline workflows with Apache Airflow (DAGs, operators, sensors).",
                "Work with Modern Data Stack tools (dbt for transformation, Snowflake / BigQuery)."
            ],
            "resources": [
                {"name": "Spark: The Definitive Guide (Chambers & Zaharia)", "type": "Book"},
                {"name": "Astronomer Airflow Tutorials", "type": "Hands-on Guide"}
            ]
        },
        "phase_3": {
            "title": "Phase 3: Real-Time Event Streaming & Data Lakehouses",
            "duration": "Months 5 - 6",
            "goals": [
                "Build real-time streaming pipelines using Apache Kafka producers, consumers, and Kafka Connect.",
                "Architect Delta Lake / Apache Iceberg ACID lakehouse tables.",
                "Deploy and schedule pipelines on cloud infrastructure."
            ],
            "capstone_project": "Real-Time Financial Fraud Detection Streaming Pipeline with Kafka, Spark Streaming, Delta Lake, and Airflow.",
            "certifications": [
                "Databricks Certified Associate Developer for Apache Spark",
                "AWS Certified Data Engineer - Associate"
            ]
        }
    },
    "ui_ux_frontend_engineer": {
        "title": "UI/UX & Modern Frontend Roadmap",
        "phase_1": {
            "title": "Phase 1: Modern JavaScript & Component Architecture",
            "duration": "Months 1 - 2",
            "goals": [
                "Master modern ES6+ JS, Promises, async/await, DOM APIs, and closures.",
                "Build accessible, semantic HTML5, CSS Flexbox/Grid, and responsive Tailwind layouts.",
                "Learn UI prototyping, wireframing, and interactive design systems in Figma."
            ],
            "resources": [
                {"name": "JavaScript.info (The Modern JavaScript Tutorial)", "type": "Interactive Guide"},
                {"name": "Figma for Developers (Official Tutorials)", "type": "Video Labs"}
            ]
        },
        "phase_2": {
            "title": "Phase 2: React Framework & State Management",
            "duration": "Months 3 - 4",
            "goals": [
                "Develop single page apps using React, custom hooks, context, and Next.js server components.",
                "Integrate global state management (Zustand / Redux Toolkit) and server state caching (React Query).",
                "Implement responsive animations using Framer Motion."
            ],
            "resources": [
                {"name": "React Official Documentation (react.dev)", "type": "Interactive Docs"},
                {"name": "Epic React by Kent C. Dodds", "type": "Course"}
            ]
        },
        "phase_3": {
            "title": "Phase 3: Performance, Accessibility & Design Systems",
            "duration": "Months 5 - 6",
            "goals": [
                "Optimize Core Web Vitals (LCP, FID, CLS), code-splitting, lazy-loading, and image optimization.",
                "Ensure WCAG 2.1 AA accessibility compliance across all components.",
                "Publish a comprehensive personal design system and interactive component storybook."
            ],
            "capstone_project": "Full-Featured SaaS Dashboard Design System with Next.js, TypeScript, Tailwind, Figma tokens, and 100% Lighthouse score.",
            "certifications": [
                "Meta Front-End Developer Professional Certificate",
                "Google UX Design Professional Certificate"
            ]
        }
    },
    "systems_embedded_engineer": {
        "title": "Systems & Embedded Engineering Roadmap",
        "phase_1": {
            "title": "Phase 1: C/C++ Systems Programming & Memory",
            "duration": "Months 1 - 2",
            "goals": [
                "Master low-level pointers, dynamic memory allocation, bitwise masking, and structs.",
                "Understand POSIX system calls: fork(), exec(), pipes, shared memory, and pthreads.",
                "Learn GDB debugging, Valgrind memory leak inspection, and Makefile builds."
            ],
            "resources": [
                {"name": "Computer Systems: A Programmer's Perspective (CS:APP)", "type": "Book"},
                {"name": "Beej's Guide to Network Programming / IPC", "type": "Free Guide"}
            ]
        },
        "phase_2": {
            "title": "Phase 2: Microcontroller Architectures & Protocols",
            "duration": "Months 3 - 4",
            "goals": [
                "Program bare-metal ARM Cortex-M or ESP32 microcontrollers using FreeRTOS.",
                "Interface hardware buses: UART, SPI, I2C, CAN, and ADC analog-to-digital converters.",
                "Work with hardware interrupts, timers, and pulse width modulation (PWM)."
            ],
            "resources": [
                {"name": "Embedded Systems Programming Course (Miro Samek / YouTube)", "type": "Video Lectures"},
                {"name": "ESP-IDF Programming Guide (Espressif Docs)", "type": "Official Documentation"}
            ]
        },
        "phase_3": {
            "title": "Phase 3: Real-Time OS & IoT Edge Capstone",
            "duration": "Months 5 - 6",
            "goals": [
                "Build deterministic hard real-time tasks with task scheduling, semaphores, and queue synchronization.",
                "Implement secure IoT telemetry with MQTT over TLS and low-power sleep states.",
                "Design and simulate schematics with KiCad EDA."
            ],
            "capstone_project": "Industrial IoT Sensor Gateway with FreeRTOS, ESP32, CAN bus telemetry, encrypted MQTT, and over-the-air (OTA) updates.",
            "certifications": [
                "ARM Accredited Engineer / Embedded Systems Certification",
                "Linux Foundation Certified System Administrator (LFCS)"
            ]
        }
    }
}


class RoadmapGenerator:
    def __init__(self):
        self.roadmaps = ROADMAP_DATABASE

    def generate_roadmap_for_career(self, career_id: str, student_facts: Dict[str, Any]) -> Dict[str, Any]:
        """
        Retrieves the structured 3-phase roadmap and dynamically annotates it with student-specific skill gaps.
        """
        base_roadmap = self.roadmaps.get(career_id, self.roadmaps["software_developer"])
        student_skills = student_facts.get("skills", {})

        # Find specific skill gaps for this student
        identified_gaps = []
        for sk_id, sk_meta in SKILLS_METADATA.items():
            lvl = student_skills.get(sk_id, 1)
            if lvl <= 2:
                identified_gaps.append(sk_meta["name"])

        return {
            "career_id": career_id,
            "title": base_roadmap["title"],
            "phase_1": base_roadmap["phase_1"],
            "phase_2": base_roadmap["phase_2"],
            "phase_3": base_roadmap["phase_3"],
            "personalized_focus_areas": identified_gaps[:4],
            "capstone_project": base_roadmap["phase_3"].get("capstone_project"),
            "certifications": base_roadmap["phase_3"].get("certifications", [])
        }
