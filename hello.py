from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    first_name = "Rasmus"
    favorite_pizza = ["Kebab", "Vegan", "Vegetarisk", 41]
    stuff = "This is <strong>Bold</strong> text"
    return render_template("index.html", first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

@app.errorhandler(404)
def pege_not_found(e):
    return render_template("404.html"), 400

@app.errorhandler(500)
def pege_not_found(e):
    return render_template("500.html"), 500