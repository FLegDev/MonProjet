from django.test import TestCase, Client
from django.urls import reverse
from .utils.pdf_generator import generate_chart, render_pdf
from io import BytesIO
import base64
import os

class PDFReportsTest(TestCase):
    def setUp(self):
        """ Configuration avant chaque test """
        self.client = Client()
        self.generate_invoice_url = reverse('generate_invoice')

    def test_generate_chart(self):
        """ Test de la génération du graphique en base64 """
        chart_base64 = generate_chart()
        self.assertIsInstance(chart_base64, str)  # Vérifie que la sortie est une chaîne
        self.assertTrue(chart_base64.startswith("iVBOR"))  # Vérifie le début d'une image encodée base64

    def test_render_pdf(self):
        """ Test de la génération d'un fichier PDF """
        context = {
            'title': 'Test PDF',
            'summary': 'Ceci est un résumé de test.',
            'table_headers': ['Colonne 1', 'Colonne 2'],
            'table_data': [['Valeur 1', 'Valeur 2']],
            'chart': generate_chart(),
            'footer': 'Test Footer',
            'lang': 'fr',
            'css_url': '/static/css/invoice_styles.css'
        }
        template_name = 'pdf_templates/invoice_template.html'
        pdf_file = render_pdf(template_name, context)
        
        # Vérifie que la sortie est un fichier PDF valide
        self.assertIsInstance(pdf_file, BytesIO)
        self.assertGreater(len(pdf_file.read()), 1000)  # Vérifie que le PDF contient du contenu
        pdf_file.seek(0)

        def test_generate_invoice_view(self):
            """ Test de la vue qui génère le PDF """
        response = self.client.get(self.generate_invoice_url)

        # Vérifie que la réponse est réussie
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')

        # Lire le contenu de streaming_content
        pdf_content = b"".join(response.streaming_content)

        # Vérifie que la taille du PDF est raisonnable
        content_length = len(pdf_content)
        self.assertGreater(content_length, 1000)

