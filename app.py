from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Denree
from config import Config
import pandas as pd
import os

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Création des tables au démarrage (Auto-migration)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('collecte.html')

@app.route('/ajouter', methods=['POST'])
def ajouter():
    try:
        nom = request.form.get('produit')
        lieu = request.form.get('marche')
        montant = request.form.get('prix')
        # On récupère la catégorie si elle est dans le formulaire, sinon "Divers"
        cat = request.form.get('categorie', 'Divers')
        
        if nom and lieu and montant:
            nouvelle_donnee = Denree(
                produit=nom, 
                marche=lieu, 
                prix=float(montant),
                categorie=cat # Ajout de la catégorie pour matcher ton models.py
            )
            db.session.add(nouvelle_donnee)
            db.session.commit()
            flash("Donnée ajoutée avec succès !", "success")
        return redirect(url_for('index'))
    except Exception as e:
        db.session.rollback() # Annule en cas d'erreur
        return f"Erreur lors de l'enregistrement : {e}"

@app.route('/analyse')
def analyse():
    marche_sel = request.args.get('marche')
    aliment_sel = request.args.get('aliment')
    
    # 1. Récupération efficace des données
    toutes_donnees = Denree.query.all()
    if not toutes_donnees:
        return render_template('analyse.html', marches=[], aliments=[], stats=None)

    # 2. Préparation des listes pour les menus déroulants
    # Utilisation d'un set pour la rapidité
    marches = sorted(list(set(d.marche for d in toutes_donnees)))
    aliments = sorted(list(set(d.produit for d in toutes_donnees)))
    
    stats = None
    donnees_brutes = []

    # 3. Calculs Statistiques avec Pandas
    if marche_sel and aliment_sel:
        # Filtrage direct en SQL pour le tableau (plus léger)
        donnees_brutes = Denree.query.filter_by(marche=marche_sel, produit=aliment_sel).all()
        
        if donnees_brutes:
            # Transformation en Series Pandas pour les calculs
            p = pd.Series([d.prix for d in donnees_brutes])
            
            stats = {
                'marche': marche_sel,
                'produit': aliment_sel,
                'mean': round(float(p.mean()), 2),
                'median': float(p.median()),
                'mode': float(p.mode()[0]) if not p.mode().empty else 0,
                'std': round(float(p.std()), 2) if len(p) > 1 else 0,
                'var': round(float(p.var()), 2) if len(p) > 1 else 0,
                'skew': round(float(p.skew()), 2) if len(p) > 2 else 0,
                'kurt': round(float(p.kurtosis()), 2) if len(p) > 3 else 0,
                'count': int(len(p))
            }

    return render_template('analyse.html', 
                           marches=marches, 
                           aliments=aliments, 
                           stats=stats,
                           donnees=donnees_brutes, 
                           sel_m=marche_sel, 
                           sel_a=aliment_sel)

@app.route('/supprimer/<int:id>', methods=['POST'])
def supprimer(id):
    item = Denree.query.get_or_404(id)
    m_back = request.form.get('marche')
    a_back = request.form.get('aliment')
    
    try:
        db.session.delete(item)
        db.session.commit()
        # On repart sur la page analyse en gardant les filtres actifs
        return redirect(url_for('analyse', marche=m_back, aliment=a_back))
    except Exception as e:
        db.session.rollback()
        return f"Erreur de suppression : {e}"

# Configuration spécifique pour Render
if __name__ == '__main__':
    # Récupération du port dynamique (obligatoire sur Render)
    port = int(os.environ.get("PORT", 5000))
    # debug=False en production pour plus de sécurité
    app.run(host='0.0.0.0', port=port, debug=False)
