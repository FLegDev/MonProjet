from django.http import FileResponse
from django.conf import settings
from .utils.pdf_generator import render_pdf, generate_chart

def generate_invoice(request):
    """Vue pour générer un PDF d'exemple."""
    table_headers = ['Produit', 'Quantité', 'Prix Unitaire', 'Total']
    table_data = [
        ['Produit A', 2, '15.00€', '30.00€'],
        ['Produit B', 1, '25.00€', '25.00€']
    ]

    context = {
        'title': 'Facture N°12345',
        'summary': 'Cette facture représente un exemple généré avec Django + WeasyPrint.',
        'table_headers': table_headers,
        'table_data': table_data,
        'chart': generate_chart(),
        'footer': 'Merci de votre confiance - Entreprise XYZ',
        'lang': 'fr',
        'css_url': settings.STATIC_URL + 'css/invoice_styles.css'
    }

    pdf_file = render_pdf('pdf_templates/invoice_template.html', context)
    return FileResponse(pdf_file, filename='facture.pdf')
