# 📊 Analyse Descriptive des Prix Alimentaires - Yaoundé

Ce projet est une application web de **Data Science** développée dans le cadre de l'unité d'enseignement **INF 232**. Elle permet la collecte et l'analyse statistique multidimensionnelle des prix des denrées alimentaires sur les marchés de la ville de Yaoundé (Mokolo, Mfoundi, Acacia, etc.).

## 🚀 Fonctionnalités

### 1. Collecte de Données (ETL)
- Formulaire d'enregistrement des prix par denrée et par marché.
- Persistance des données dans une base de données relationnelle **PostgreSQL**.

### 2. Dashboard d'Analyse Descriptive
Analyse dynamique après filtrage par **Marché** et **Produit** incluant :
- **Tendance Centrale** : Moyenne, Médiane, Mode.
- **Dispersion** : Écart-type, Variance, Étendue, Min/Max.
- **Forme de Distribution** : Asymétrie (Skewness) et Aplatissement (Kurtosis).

## 🛠️ Stack Technique

* **Backend** : Python 3.12+ / Flask
* **Base de données** : PostgreSQL
* **Traitement de données** : Pandas, NumPy, SciPy
* **Frontend** : HTML5 (Jinja2 Templates), Bootstrap 5 (Responsive Design)

## 📁 Structure du Projet

```text
projet_prix/
├── app.py              # Point d'entrée de l'application (Routes Flask)
├── models.py           # Définition du modèle de données (SQLAlchemy)
├── config.py           # Configuration de la base de données
├── requirements.txt    # Dépendances du projet
├── templates/          # Fichiers HTML
│   ├── base.html       # Squelette commun (Héritage)
│   ├── collecte.html   # Formulaire d'entrée
│   └── analyse.html    # Dashboard statistique
└── README.md           # Documentation

Installation et Lancement

    Cloner le projet ou extraire l'archive.

    Installer les dépendances :
    Bash

    pip install -r requirements.txt

    Configurer PostgreSQL :
    Assurez-vous qu'une base de données nommée postgres (ou celle configurée dans config.py) est accessible.

    Lancer l'application :
    Bash

    python3 app.py

    Accéder à l'interface : http://127.0.0.1:5000

👨‍💻 Auteur

Ahmed - Étudiant à l'Université de Yaoundé I (FST)
Cours : INF 232 - Programmation Web & Analyse de Données


---

### Pourquoi ce README va te faire gagner des points :

* **Clarté** : Il explique immédiatement "Quoi", "Comment" et "Pourquoi".
* **Vocabulaire Technique** : Utiliser des mots comme *ETL*, *Persistance*, *Statistiques Multidimensionnelles* montre que tu maîtrises le sujet.
* **Structure de dossier** : Le schéma de l'arborescence aide le prof à se retrouver sans chercher.

### Dernier conseil pour demain :
Imprime ce README ou garde-le ouvert dans un onglet de ton éditeur. Si le prof te demande de présenter ton travail, tu peux utiliser les sections du README comme plan pour ta démonstration orale.

Tout est prêt maintenant ? On a le code, les templates, la base de données, les dépendances et la doc ! Bonne chance, tu vas assurer !
