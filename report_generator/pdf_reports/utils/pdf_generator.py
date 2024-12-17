import base64
from io import BytesIO
import matplotlib.pyplot as plt
from django.template.loader import render_to_string
from weasyprint import HTML

def generate_chart():
    """Génère un graphique matplotlib et retourne son encodage base64."""
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30])  # Exemple de données
    ax.set_title('Exemple de Graphique')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    chart_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    plt.close(fig)
    return chart_base64

def render_pdf(template_name, context):
    """Rend un modèle HTML en PDF."""
    html_string = render_to_string(template_name, context)
    pdf_file = BytesIO()
    HTML(string=html_string).write_pdf(pdf_file)
    pdf_file.seek(0)
    return pdf_file
