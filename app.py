from flask import Flask, render_template
import wikipedia as wiki
import random
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def show_wiki():
    title, summary = random_wiki()
    return render_template("main.html", title=title, summary=summary, template_folder="templates")

def random_wiki():
    title = wiki.random()
    summary = wiki.summary(title)
    return title, summary

if __name__=="__main__":
    app.run(debug=True)

"""flask run --debugger --reload"""
