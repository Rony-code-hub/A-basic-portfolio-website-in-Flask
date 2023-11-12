from flask import Flask, render_template, abort

app = Flask(__name__)

projects = [
    {
        "name": "Habit tracking app with flask and mongodb",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "Mongodb"],
        "slug": "habit-tracking",
        "prod": "http://udemy.com",
    },
    {
        "name": "Personal finance tracking app with react",
        "thumb": "img/personal-finance.png",
        "hero": "img/personal-finance.png",
        "categories": ["Javascript", "React"],
        "slug": "personal-finance",
    },
    {
        "name": "Rest API Documentation with postman and swagger",
        "thumb": "img/rest-api-docs.png",
        "hero": "img/rest-api-docs.png",
        "categories": ["Writing", "Automation"],
        "slug": "API-docs",
    },
]

slug_to_project = {project["slug"]: project for project in projects}


@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# @app.route("/project/<string:slug>")
# def project(slug):
#     if slug not in slug_to_project:
#         abort(404)
#     return render_template(f"project_{slug}.html", project=slug_to_project[slug])


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(error):
    return render_template("error_500.html"), 500
