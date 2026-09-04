#!/usr/bin/env python3
"""Genera el CV en PDF (assets/CV-Cristiam-Sanchez-Zelaya.pdf) a partir del
mismo contenido que aparece en index.html, en español."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)

INK = colors.HexColor("#1c1f1c")
MUTED = colors.HexColor("#55605a")
ACCENT = colors.HexColor("#5c7a2a")
CORAL = colors.HexColor("#c9502f")
LINE = colors.HexColor("#d8ddd6")

styles = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=20,
                            textColor=INK, spaceAfter=2, leading=22),
    "subheading": ParagraphStyle("subheading", fontName="Helvetica-Bold",
                                  fontSize=9.5, textColor=ACCENT, spaceAfter=8,
                                  leading=12),
    "lead": ParagraphStyle("lead", fontName="Helvetica", fontSize=8.7,
                            textColor=MUTED, leading=12, spaceAfter=3),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12,
                          textColor=INK, spaceBefore=6, spaceAfter=5),
    "job_title": ParagraphStyle("job_title", fontName="Helvetica-Bold",
                                 fontSize=9.5, textColor=INK, leading=11.5),
    "company": ParagraphStyle("company", fontName="Helvetica-Bold",
                               fontSize=8.3, textColor=ACCENT, spaceAfter=1,
                               leading=10),
    "date": ParagraphStyle("date", fontName="Helvetica-Bold", fontSize=8,
                            textColor=colors.white, backColor=colors.HexColor("#385522"),
                            alignment=2, leading=10),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=8.3,
                            textColor=MUTED, leading=11, spaceAfter=4),
    "skill_head": ParagraphStyle("skill_head", fontName="Helvetica-Bold",
                                  fontSize=8.8, textColor=ACCENT, spaceBefore=3,
                                  spaceAfter=1),
    "skill_item": ParagraphStyle("skill_item", fontName="Helvetica",
                                  fontSize=8.3, textColor=MUTED, leading=11),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=8.3,
                               textColor=MUTED, leading=11),
}


def hr():
    return HRFlowable(width="100%", thickness=0.75, color=LINE, spaceBefore=2, spaceAfter=6)


def job(title, company, date, desc):
    row = Table(
        [[Paragraph(title, styles["job_title"]), Paragraph(date, styles["date"])]],
        colWidths=[130 * mm, 45 * mm],
    )
    row.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return [row, Paragraph(company, styles["company"]),
            Paragraph(desc, styles["body"])]


def skills_block(title, items):
    out = [Paragraph(title, styles["skill_head"])]
    out.append(Paragraph(" &nbsp;·&nbsp; ".join(items), styles["skill_item"]))
    return out


story = []

# --- Encabezado -----------------------------------------------------------
story.append(Paragraph("Cristiam J. Sanchez Zelaya", styles["name"]))
story.append(Paragraph(
    "Software Developer &middot; Backend .NET &middot; APIs &middot; SQL Server &middot; PostgreSQL",
    styles["subheading"]))
story.append(Paragraph(
    "Profesional de informática con más de 15 años de experiencia en desarrollo de software y "
    "análisis de sistemas. Experiencia principalmente con C#, ASP.NET, SQL Server y desarrollo de "
    "aplicaciones empresariales. Actualmente enfocado en fortalecer el desarrollo backend con "
    "ASP.NET Core, Web APIs, Entity Framework Core, arquitectura de software, Docker, pruebas "
    "automatizadas y prácticas CI/CD.",
    styles["lead"]))
story.append(Paragraph(
    "cristiam.sanchez204@gmail.com &nbsp;|&nbsp; github.com/CristiamSanchez &nbsp;|&nbsp; "
    "linkedin.com/in/cristiam-jose-sanchez-zelaya-898356198",
    styles["contact"]))
story.append(hr())

# --- Experiencia ------------------------------------------------------------
story.append(Paragraph("Experiencia Profesional", styles["h2"]))

experience = [
    ("Desarrollador de Software", "BANADESA", "Mayo 2023 - Actualidad",
     "Desarrollo y mantenimiento de aplicaciones internas utilizando C# y SQL Server. Desarrollo y "
     "validación de APIs REST con ASP.NET, incluyendo integración y pruebas de endpoints antes de los "
     "despliegues a producción. Participación directa en la estabilización de procesos internos "
     "críticos del banco, reduciendo incidencias reportadas por los usuarios."),
    ("Analista de Sistemas / Soporte Técnico", "IHSS", "Abril 2022 - Marzo 2023",
     "Desarrollo de aplicaciones web y soporte técnico a usuarios institucionales."),
    ("Desarrollador de Sistemas", "Espresso Americano", "Noviembre 2019 - Octubre 2020",
     "Desarrollo de sistemas de nómina utilizando C# y SQL Server. Desarrollo y consumo de servicios "
     "web utilizando JSON y VB."),
    ("Analista de Tecnología", "Banco de América Central", "Abril 2013 - Enero 2017",
     "Desarrollo y mantenimiento de sistemas con C# y SQL Server. Análisis, recopilación y "
     "preparación de información estadística."),
    ("Analista Programador", "Banco Lafise", "Agosto 2011 - Enero 2012",
     "Desarrollo de sistemas empresariales utilizando C# y SQL Server."),
]

for title, company, date, desc in experience:
    story.extend(job(title, company, date, desc))

story.append(hr())

# --- Educación --------------------------------------------------------------
story.append(Paragraph("Formación Académica", styles["h2"]))
story.extend(job(
    "CEUTEC - UNITEC", "", "2007 - 2014",
    "Ingeniería en Informática &middot; Técnico Universitario en Desarrollo de Sistemas de "
    "Información &middot; Ingeniería en Gestión Logística"))
story.extend(job(
    "Brigham Young University - BYU Pathway", "", "2021 - Actualidad",
    "Formación en tecnología y desarrollo. Cursos relacionados con programación, fundamentos web, "
    "frontend y bases de datos."))

story.append(hr())

# --- Habilidades técnicas ----------------------------------------------------
story.append(Paragraph("Habilidades Técnicas", styles["h2"]))
story.extend(skills_block("Desarrollo Backend", [
    "C# / .NET / ASP.NET Core", "REST APIs / Web APIs", "Entity Framework Core",
    "ASP.NET Web Forms", "Arquitectura por capas / Clean Architecture", "JWT"]))
story.extend(skills_block("Bases de Datos", [
    "SQL Server", "PostgreSQL", "MySQL", "Stored Procedures / SQL"]))
story.extend(skills_block("Frontend", [
    "HTML5 / CSS / JavaScript", "Bootstrap / jQuery", "Angular / React"]))
story.extend(skills_block("DevOps y herramientas", [
    "Git / GitHub", "Docker / Docker Compose", "CI/CD", "AWS (fundamentos)"]))
story.extend(skills_block("Calidad de Software", [
    "Pruebas unitarias e integración", "Pruebas de APIs",
    "Postman / Playwright / Selenium / JMeter / k6"]))

story.append(hr())

# --- Certificaciones ---------------------------------------------------------
story.append(Paragraph("Certificaciones y Formación Complementaria", styles["h2"]))
certs = [
    "AWS &ndash; AWS Academy Graduate - Cloud Foundations",
    "Udemy &ndash; QA Engineer Course",
    "CertiProf &ndash; Scrum Master Professional Certification",
    "CertiProf &ndash; Design Thinking Professional Certification",
    "Fortinet &ndash; Fortinet Certified Associate Cybersecurity",
    "Cisco/NetAcad &ndash; Ethical Hacking",
    "Cisco/NetAcad &ndash; Cyber Threat Management",
    "UNAH &ndash; CCNA2 Certificate",
    "Funiber &ndash; University Expert in ISO 9001",
    "UPNFM &ndash; English 2nd Language Certificate",
]
half = (len(certs) + 1) // 2
col1 = certs[:half]
col2 = certs[half:]
rows = []
for i in range(half):
    left = Paragraph("&bull; " + col1[i], styles["skill_item"])
    right = Paragraph("&bull; " + col2[i], styles["skill_item"]) if i < len(col2) else ""
    rows.append([left, right])

cert_table = Table(rows, colWidths=[87 * mm, 87 * mm])
cert_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 0),
    ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ("TOPPADDING", (0, 0), (-1, -1), 1),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
]))
story.append(cert_table)

doc = SimpleDocTemplate(
    "assets/CV-Cristiam-Sanchez-Zelaya.pdf",
    pagesize=letter,
    topMargin=14 * mm, bottomMargin=12 * mm,
    leftMargin=18 * mm, rightMargin=18 * mm,
    title="CV - Cristiam Sanchez Zelaya",
    author="Cristiam Sanchez Zelaya",
)
doc.build(story)
print("PDF generado correctamente.")
