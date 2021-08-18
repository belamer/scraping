from flask import Flask, render_template
import json

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

def show_response():
    with open ('animal_scraping/spiders/animals.json', 'r') as file:
        animal = json.load(file)
    jsonResponse = animal
    return jsonResponse

@app.route("/")
def start():
    return ('<a class="button" href="/response">Получить данные</a>')

@app.route("/response")
def render_response():
    response = json.dumps(show_response(), ensure_ascii=False, indent=4)
    return render_template("render-response.html", response=response)

if __name__ == '__main__':
    app.run(debug=True)

