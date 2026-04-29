import os

# On définit le chemin de base du projet pour SQLite
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # --- LA MODIFICATION CRUCIALE ICI ---
    # On cherche d'abord une variable d'environnement 'DATABASE_URL' (fournie par Render)
    # Si elle n'existe pas, on utilise SQLite en local (le fichier database.db)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database.db')
    
    # Correction pour les versions récentes de SQLAlchemy sur Render
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'une-cle-tres-secrete-123'
