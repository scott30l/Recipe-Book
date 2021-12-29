from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<query>')
def user(query):
    with open(f'data/{query}.json') as file:
        print(file)
        data = json.load(file)
        name = data['name']
        cooktime = data['cooktime']
        ingredients = data['ingredients']
    return render_template('recipe.html', name=name, cooktime=cooktime, ingredients=ingredients)


if __name__ == "__main__":
    app.run(debug=True)