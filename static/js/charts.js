// static/js/script.js

document.addEventListener('DOMContentLoaded', function() {
    // On vérifie si les données stats existent dans la page
    // On récupère les éléments canvas
    const barCanvas = document.getElementById('barChart');
    const dispersionCanvas = document.getElementById('dispersionChart');
    const shapeCanvas = document.getElementById('shapeChart');
    const pieCanvas = document.getElementById('pieChart');

    if (barCanvas) {
        // Les données sont injectées via des attributs data dans le HTML ou récupérées globalement
        // Pour plus de simplicité, on utilise les variables globales définies dans le HTML
        
        // 1. Bar Chart (Tendances)
        new Chart(barCanvas, {
            type: 'bar',
            data: {
                labels: ['Moyenne', 'Médiane', 'Mode'],
                datasets: [{
                    label: 'Prix (FCFA)',
                    data: [statsData.mean, statsData.median, statsData.mode],
                    backgroundColor: ['#3498db', '#1abc9c', '#f1c40f']
                }]
            }
        });

        // 2. Dispersion (Polar Area)
        new Chart(dispersionCanvas, {
            type: 'polarArea',
            data: {
                labels: ['Écart-type', 'Variation'],
                datasets: [{
                    data: [statsData.std, Math.sqrt(statsData.var)],
                    backgroundColor: ['rgba(231, 76, 60, 0.6)', 'rgba(155, 89, 182, 0.6)']
                }]
            }
        });

        // 3. Forme (Radar)
        new Chart(shapeCanvas, {
            type: 'radar',
            data: {
                labels: ['Asymétrie (Skew)', 'Aplatissement (Kurt)'],
                datasets: [{
                    label: 'Profil de Distribution',
                    data: [statsData.skew, statsData.kurt],
                    backgroundColor: 'rgba(52, 73, 94, 0.2)',
                    borderColor: '#34495e'
                }]
            }
        });

        // 4. Pie Chart
        new Chart(pieCanvas, {
            type: 'pie',
            data: {
                labels: ['Moyenne', 'Médiane', 'Mode'],
                datasets: [{
                    data: [statsData.mean, statsData.median, statsData.mode],
                    backgroundColor: ['#3498db', '#1abc9c', '#f1c40f']
                }]
            }
        });
    }
});