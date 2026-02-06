#!/usr/bin/env python3
"""Generate a professional PDF resume for Wendeel Marinho."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from datetime import datetime

# Create PDF
pdf_path = "assets/Wendeel-Marinho-CTO-Resume.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
styles = getSampleStyleSheet()
story = []

# Custom styles
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#1f6feb'),
    spaceAfter=6,
    alignment=1,  # Center
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=12,
    textColor=colors.HexColor('#1f6feb'),
    spaceAfter=8,
    spaceBefore=10,
    fontName='Helvetica-Bold'
)

job_title_style = ParagraphStyle(
    'JobTitle',
    parent=styles['Normal'],
    fontSize=11,
    textColor=colors.black,
    fontName='Helvetica-Bold',
    spaceAfter=2
)

job_meta_style = ParagraphStyle(
    'JobMeta',
    parent=styles['Normal'],
    fontSize=9,
    textColor=colors.HexColor('#445566'),
    spaceAfter=4,
    fontName='Helvetica-Oblique'
)

bullet_style = ParagraphStyle(
    'Bullet',
    parent=styles['Normal'],
    fontSize=9,
    textColor=colors.black,
    spaceAfter=3,
    leftIndent=20
)

# Title
story.append(Paragraph("Wendeel Marinho", title_style))
story.append(Paragraph("CTO / Product &amp; Engineering Lead / Tech Lead", styles['Normal']))
story.append(Spacer(1, 0.1*inch))

# Contact
contact_text = "São Paulo, Brazil (Remote/Hybrid) | (11) 91124-2062 | wendeelmarinho@gmail.com | linkedin.com/in/wendeelm/"
story.append(Paragraph(contact_text, styles['Normal']))
story.append(Spacer(1, 0.15*inch))

# Summary
story.append(Paragraph("PROFESSIONAL SUMMARY", heading_style))
summary = (
    "10+ years building systems end-to-end (product, architecture, implementation, delivery). "
    "Currently CTO at Scalegrid and Founder/Lead at RemédiosJÁ. Specializing in multi-tenant SaaS, "
    "marketplaces, event-driven integrations, RBAC, tenant isolation, and engineering governance. "
    "Proven track record architecting resilient platforms, leading teams, and establishing production-grade practices."
)
story.append(Paragraph(summary, styles['Normal']))
story.append(Spacer(1, 0.1*inch))

# Experience
story.append(Paragraph("PROFESSIONAL EXPERIENCE", heading_style))

experiences = [
    {
        "title": "Scalegrid — Chief Technology Officer | Tech Lead / Senior Engineer",
        "period": "Feb 2025 — Present",
        "location": "São Paulo, Brazil (Remote)",
        "bullets": [
            "Built a modular, multi-tenant B2B management SaaS end-to-end as an add-on marketplace with plan-based module activation.",
            "Architected the platform core: tenant isolation, RBAC/permissions, audit trail, settings, and admin governance.",
            "Implemented an event-driven integrations layer (webhooks + connectors) to synchronize external systems.",
            "Delivered business-critical modules: Projects/Tasks/Bugs, CRM, Accounting, HRM, POS, Products &amp; Services.",
            "Built real-time communication features (direct + group messaging) with attachment handling.",
            "Designed subscription &amp; billing flows enabling modular monetization by plan tier.",
            "Established production-grade engineering practices: CI/CD, code review, structured logging, and observability."
        ]
    },
    {
        "title": "RemédiosJÁ — Founder &amp; CTO",
        "period": "Mar 2023 — Present",
        "location": "São Paulo, Brazil (Remote)",
        "bullets": [
            "Architected and developed end-to-end pharmacy delivery marketplace: Laravel backend, Vue.js admin, Flutter mobile (iOS/Android).",
            "Delivered 3 applications (Customer, Store, Courier) + admin panels: catalog, checkout, payments, delivery routing, refunds.",
            "Integrated payment gateways (Mercado Pago, Asaas), Firebase (Auth/FCM/Analytics), geolocation, zone pricing.",
            "Structured multi-zone operations (city/region) with availability rules, promotions, inventory governance.",
            "Built operations ecosystem: pharmacy onboarding, SLA, coupons/campaigns, push notifications, acquisition/retention metrics.",
        ]
    },
    {
        "title": "Seara — Tech Lead",
        "period": "Jun 2024 — Mar 2025",
        "location": "São Paulo, Brazil (Hybrid)",
        "bullets": [
            "Led architecture and sustainability of digital ecosystem: seara.com.br (hub), Seara Gourmet, Seara Internacional.",
            "Developed fully custom WordPress (e-commerce + portals) without themes/plugins: proprietary architecture, reusable components.",
            "Optimized for performance: Core Web Vitals, multi-layer caching, payload reduction, technical SEO.",
            "Designed integrations via REST APIs with internal catalog, campaigns, and content services.",
            "Established engineering standards: code review, testing, documentation, team mentoring."
        ]
    },
    {
        "title": "Ambar — Tech Lead",
        "period": "Apr 2025 — Oct 2025",
        "location": "Hybrid (AUTODOC)",
        "bullets": [
            "Led technical leadership of strategic projects with PHP (Laravel) and Python.",
            "Coordinated development team: promoted best practices, code review, standardization, DevOps culture.",
            "Managed and implemented REST API integrations between platforms.",
            "Continuous improvements in legacy and new solutions with focus on quality and efficiency."
        ]
    },
    {
        "title": "WAY.AG — Senior Full Stack Developer",
        "period": "Dec 2023 — Jan 2025",
        "location": "São Paulo, Brazil (Hybrid)",
        "bullets": [
            "Backend: REST/GraphQL APIs, database optimization, microservices, scalable architecture.",
            "Frontend: responsive interfaces, API integration, performance optimization.",
            "AI/ML: machine learning models, predictive analysis, AI agents for automation.",
            "DevOps: cloud deployment (AWS/Azure/GCP), CI/CD pipelines, monitoring."
        ]
    }
]

for exp in experiences:
    story.append(Paragraph(exp['title'], job_title_style))
    meta = f"{exp['period']} | {exp['location']}"
    story.append(Paragraph(meta, job_meta_style))
    for bullet in exp['bullets']:
        story.append(Paragraph(f"• {bullet}", bullet_style))
    story.append(Spacer(1, 0.05*inch))

story.append(PageBreak())

# Skills
story.append(Paragraph("TECHNICAL SKILLS", heading_style))

skills = [
    ("Backend &amp; APIs", "PHP/Laravel, Python (FastAPI, Django), Node.js (Express, NestJS), REST/GraphQL APIs, Microservices"),
    ("Frontend &amp; Mobile", "Vue.js, Flutter (iOS/Android), Angular, TypeScript, Responsive Design"),
    ("Cloud &amp; DevOps", "AWS (EC2, S3, Lambda, RDS), Docker, Kubernetes, CI/CD, GitHub Actions, Observability"),
    ("Databases", "PostgreSQL, MySQL, MongoDB, Redis, Database optimization &amp; modeling"),
    ("Data &amp; AI", "Python data science, Machine learning pipelines, MLOps, Kafka, Real-time processing"),
    ("Integrations", "Payment gateways (Mercado Pago, Asaas), Firebase, Webhooks, Third-party APIs, ERP systems"),
    ("Architecture", "Domain-driven design (DDD), SOLID principles, Multi-tenant isolation, RBAC, Audit trails"),
]

for skill_cat, skill_list in skills:
    story.append(Paragraph(f"<b>{skill_cat}:</b> {skill_list}", styles['Normal']))
    story.append(Spacer(1, 0.05*inch))

story.append(Spacer(1, 0.1*inch))

# Education
story.append(Paragraph("EDUCATION &amp; CERTIFICATIONS", heading_style))

education = [
    ("UniNorte (Centro Universitário do Norte)", "Analysis and Systems Development", "2018"),
    ("FIAP", "Postgraduate in AI Engineering / MLOps", "Nov 2025 – Dec 2026"),
    ("Alura", "Data Science", "2024-2025"),
    ("Data Science Academy", "Python for Data Science 4.0", "2024-2025"),
    ("Alura", "Java with Spring Boot 3", "2025"),
    ("Alura", "Angular: Front-End with TypeScript", "2025"),
    ("Alura", "Software Architecture with Node.js", "2024"),
    ("Udemy", "Complete Docker and Kubernetes", "2024"),
    ("Udemy", "Apache Kafka: Messaging for Distributed Systems", "2025"),
    ("Coursera / DeepLearning.ai", "Machine Learning for Developers (Andrew Ng)", "2024"),
    ("AWS", "AWS Cloud Practitioner Essentials", "2024"),
]

for school, program, period in education:
    story.append(Paragraph(f"<b>{school}</b> — {program} ({period})", styles['Normal']))
    story.append(Spacer(1, 0.03*inch))

story.append(Spacer(1, 0.1*inch))

# Core Projects
story.append(Paragraph("KEY PROJECTS", heading_style))

projects = [
    ("Scalegrid", "Multi-tenant SaaS with modular architecture, RBAC, integrations, and subscription management."),
    ("RemédiosJÁ", "Pharmacy delivery marketplace with 3-app ecosystem, payments, and multi-zone operations."),
    ("Seara Digital Ecosystem", "Custom WordPress e-commerce and portal ecosystem across multiple properties."),
]

for proj_name, proj_desc in projects:
    story.append(Paragraph(f"<b>{proj_name}:</b> {proj_desc}", styles['Normal']))
    story.append(Spacer(1, 0.04*inch))

# Build PDF
doc.build(story)
print(f"✅ PDF gerado com sucesso: {pdf_path}")
