<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Analyse Descriptive - INF 232</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="container mt-5">
    <h2>Analyse des prix par Marché (Yaoundé)</h2>
    <hr>
    
    <div class="row">
        <div class="col-md-6">
            <h4>Moyennes calculées (Analyse Descriptive)</h4>
            <table class="table table-striped">
                <thead>
                    <tr>
                        <th>Marché</th>
                        <th>Prix Moyen (FCFA)</th>
                    </tr>
                </thead>
                <tbody>
                    {% for marche, prix in moyennes.items() %}
                    <tr>
                        <td>{{ marche }}</td>
                        <td>{{ prix|round(2) }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>

    <a href="/" class="btn btn-secondary">Retour à la collecte</a>
</body>
</html>