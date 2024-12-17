1. Présentation du projet
Nom du projet : Générateur de rapports PDF avec Django et WeasyPrint
Objectif :
Cette application permet de générer des fichiers PDF contenant des informations telles que des résumés, des tableaux de données et des graphiques générés dynamiquement.

Technologies utilisées :

Django (Framework web Python)
WeasyPrint (Génération de PDF à partir de templates HTML/CSS)
Matplotlib (Génération de graphiques dynamiques)
Bootstrap (optionnel pour styliser les templates HTML)

2. Prérequis
Avant de commencer, assurez-vous que vous disposez des éléments suivants :

Python 3.8+ installé.
Pip (gestionnaire de paquets Python).
Virtualenv pour isoler l’environnement.

Les dépendances requises :
Django
WeasyPrint
Matplotlib
GTK (pour Windows)

3. Installation de l’application
Étape 1 : Cloner le projet
Récupérez le projet depuis le dépôt Git :
git clone <URL_DU_REPOSITORY>
cd report_generator

Étape 2 : Créer et activer un environnement virtuel

Sur Windows :
python -m venv venv
venv\Scripts\activate

Sur Linux/macOS :
python3 -m venv venv
source venv/bin/activate


Étape 3 : Installer les dépendances
Installez les dépendances nécessaires avec pip :
pip install -r requirements.txt
Note : Assurez-vous d’ajouter les bibliothèques GTK, Cairo et Pango pour Windows.

Étape 4 : Appliquer les migrations
Créez la base de données avec les migrations :
python manage.py makemigrations
python manage.py migrate


Étape 5 : Créer un superutilisateur
Pour accéder à l’interface d’administration, créez un superutilisateur :
python manage.py createsuperuser

Étape 6 : Lancer le serveur
Démarrez le serveur Django avec :
python manage.py runserver
Accédez à l’application sur :
http://127.0.0.1:8000/

4. Configuration des URLS
URL pour générer un rapport PDF
Vous pouvez accéder à la vue générant un PDF avec l’URL suivante :
http://127.0.0.1:8000/pdf/generate-invoice/

5. Structure du projet
Voici l’arborescence de l’application :

report_generator/
│
├── manage.py                         # Commande principale Django
├── report_generator/                 # Configuration principale Django
│   ├── settings.py                   # Paramètres Django
│   ├── urls.py                       # Routes principales
│   └── ...
│
├── pdf_reports/                      # Application principale
│   ├── views.py                      # Logique métier pour générer le PDF
│   ├── urls.py                       # Routes de l'application
│   ├── templates/                    # Templates HTML
│   │   └── pdf_templates/            # Fichiers HTML pour le PDF
│   │       └── invoice_template.html
│   ├── static/                       # Fichiers CSS pour les styles
│   │   └── css/
│   │       └── invoice_styles.css
│   ├── utils/                        # Outils utilitaires
│   │   └── pdf_generator.py          # Logique pour générer PDF et graphiques
│   └── __init__.py
│
├── venv/                             # Environnement virtuel
└── db.sqlite3                        # Base de données SQLite

6. Fonctionnement de l’application
   6.1 Génération du PDF
Le template HTML (situé dans templates/pdf_templates/invoice_template.html) est utilisé pour structurer le contenu du PDF.
Les données dynamiques (titre, tableau, graphique, résumé) sont injectées dans le template via la vue generate_invoice dans views.py.
Un graphique est généré dynamiquement grâce à Matplotlib et encodé en base64 pour être intégré au HTML.
WeasyPrint convertit le HTML/CSS en fichier PDF.

   6.2 Explications des fichiers clés
views.py :
Contient la vue generate_invoice qui assemble les données pour générer le PDF.

pdf_generator.py :
Contient les fonctions utilitaires pour :

Générer le graphique avec Matplotlib.
Convertir le template HTML en PDF avec WeasyPrint.
invoice_template.html :
Template HTML utilisé pour le rendu du PDF.

invoice_styles.css :
Feuille de style pour le PDF.

7. Test et déploiement
   7.1 Test de l'application en local
Accédez à :
http://127.0.0.1:8000/pdf/generate-invoice/
Le PDF devrait être généré et proposé en téléchargement.

8. Problèmes courants et solutions
WeasyPrint ne fonctionne pas sur Windows :
Installez les bibliothèques GTK, Cairo et Pango.

Graphique non visible :
Assurez-vous que Matplotlib est installé correctement.

9. Licence
Ce projet est distribué sous la licence MIT. Vous pouvez le réutiliser librement.

10. Contact
Pour toute question ou amélioration, contactez :
Email : flegdev.fr@gmail.com
