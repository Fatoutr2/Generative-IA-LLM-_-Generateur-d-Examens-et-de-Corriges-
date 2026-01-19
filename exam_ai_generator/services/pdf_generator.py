from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
import html


def generate_pdf(text, output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    styles = getSampleStyleSheet()
    body_style = styles["Normal"]
    body_style.spaceAfter = 12

    elements = []

    for line in text.split("\n"):
        line = line.strip()

        if not line:
            elements.append(Spacer(1, 8))
            continue

        # 🔐 ÉCHAPPEMENT HTML (LA CLÉ)
        safe_line = html.escape(line)

        elements.append(Paragraph(safe_line, body_style))

    doc.build(elements)
