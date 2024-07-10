from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Create a list of wild life species

wildlife_species = [
    {
        'name': 'Elephant',
        'scientific_name': 'Loxodonta africana',
        'habitat': 'Africa',
        'population': 50000000,
        'diet': 'Herbivore',
        'conservation_status': 'Vulnerable',
        'lifespan': '60-70 years'
    },
    {
        'name': 'Giraffe',
        'scientific_name': 'Giraffa camelopardalis',
        'habitat': 'Africa',
        'population': 1500000,
        'diet': 'Herbivore',
        'conservation_status': 'Vulnerable',
        'lifespan': '25-30 years'
    },
    {
        'name': 'Lion',
        'scientific_name': 'Panthera leo',
        'habitat': 'Africa',
        'population': 2000000,
        'diet': 'Carnivore',
        'conservation_status': 'Vulnerable',
        'lifespan': '10-14 years'
    },
    {
        'name': 'Gorilla',
        'scientific_name': 'Gorilla beringei',
        'habitat': 'Africa',
        'population': 300000,
        'diet': 'Herbivore',
        'conservation_status': 'Endangered',
        'lifespan': '35-40 years'
    },
    {
        'name': 'Tiger',
        'scientific_name': 'Panthera tigris',
        'habitat': 'Asia',
        'population': 3900,
        'diet': 'Carnivore',
        'conservation_status': 'Endangered',
        'lifespan': '10-15 years'
    },
    {
        'name': 'Panda',
        'scientific_name': 'Ailuropoda melanoleuca',
        'habitat': 'Asia',
        'population': 1864,
        'diet': 'Herbivore',
        'conservation_status': 'Vulnerable',
        'lifespan': '20 years'
    }
]

# Route to display the wildlife list

@app.route('/')
def home():
    return render_template('index.html', wildlife_species=wildlife_species)

# Route to add species

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        scientific_name = request.form['scientific_name']
        habitat = request.form['habitat']
        population = request.form['population']
        diet = request.form['diet']
        conservation_status = request.form['conservation_status']
        lifespan = request.form['lifespan']
        wildlife_species.append({
            'name': name,
            'scientific_name': scientific_name,
            'habitat': habitat,
            'population': population,
            'diet': diet,
            'conservation_status': conservation_status,
            'lifespan': lifespan
        })
        return redirect(url_for('home'))
    return render_template('add_species.html')
