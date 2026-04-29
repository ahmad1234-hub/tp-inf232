from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Denree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produit = db.Column(db.String(100), nullable=False)  # ex: Tomate, Riz
    categorie = db.Column(db.String(50))                 # ex: Féculent, Légume
    prix = db.Column(db.Float, nullable=False)           # Le prix en FCFA
    marche = db.Column(db.String(100), nullable=False)    # ex: Mokolo, Mfoundi
    date_collecte = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<Denree {self.produit} - {self.prix}>'
