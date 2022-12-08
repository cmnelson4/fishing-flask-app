from flask import Flask, render_template, request
from flaskrun import flaskrun

app = Flask(__name__)

fish_caught = 0
bait = "worm"
rod = "basic"


@app.route("/")
def index():
    return render_template(
        "./templates/index.html", fish_caught=fish_caught, bait=bait, rod=rod
    )


@app.route("/upgrade_bait")
def upgrade_bait():
    global bait
    if bait == "worm":
        bait = "fly"
    elif bait == "fly":
        bait = "lure"
    return render_template(
        "./templates/index.html", fish_caught=fish_caught, bait=bait, rod=rod
    )


@app.route("/upgrade_rod")
def upgrade_rod():
    global rod
    if rod == "basic":
        rod = "medium"
    elif rod == "medium":
        rod = "advanced"
    return render_template(
        "./templates/index.html", fish_caught=fish_caught, bait=bait, rod=rod
    )


@app.route("/cast")
def cast():
    global fish_caught
    fish_caught += 1
    return render_template(
        "./templates/index.html", fish_caught=fish_caught, bait=bait, rod=rod
    )


if __name__ == "__main__":
    flaskrun(app)
