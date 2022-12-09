from flask import Flask, render_template
from flaskrun import flaskrun
import random

app = Flask(__name__)

# define a variable to keep track of the player's money
money = 0

# define a variable to keep track of the player's fishing skill
skill = 1

# define a list of fish with their corresponding values
fish = [
    {"name": "Goldfish", "value": 1},
    {"name": "Salmon", "value": 5},
    {"name": "Tuna", "value": 10},
    {"name": "Shark", "value": 50},
]

# define a list of upgrades that the player can buy
upgrades = [
    {"name": "Better bait", "price": 5, "increase": 2},
    {"name": "Faster boat", "price": 10, "increase": 5},
    {"name": "Sonar", "price": 20, "increase": 10},
]

# define a route for the homepage
@app.route("/", methods=["POST", "GET"])
def index():
    global money
    global skill
    return render_template(
        "index.html", money=money, skill=skill, fish=fish, upgrades=upgrades
    )


# define a route for the fishing action
@app.route("/fish", methods=["POST", "GET"])
def go_fish():
    global money
    global skill

    # determine which fish the player catches
    caught_fish = fish[
        random.randint(0, 3)
    ]  # for now, always catch the first fish in the list

    # increase the player's money by the value of the caught fish
    money += caught_fish["value"] * skill

    return render_template(
        "index.html", money=money, skill=skill, fish=fish, upgrades=upgrades
    )


# define a route for buying upgrades
@app.route("/buy/<upgrade_name>", methods=["POST", "GET"])
def buy(upgrade_name):
    global money
    global skill
    global upgrades
    # find the upgrade that the player is trying to buy
    upgrade = None
    for u in upgrades:
        if u["name"] == upgrade_name:
            upgrade = u
            break

    # make sure the upgrade exists
    if upgrade:
        # make sure the player has enough money to buy the upgrade
        if money >= upgrade["price"]:
            # decrease the player's money by the price of the upgrade
            money -= upgrade["price"]

            # increase the player's fishing skill by the increase of the upgrade
            skill += upgrade["increase"]

    upgrades = [
        {"name": "Better bait", "price": skill * 5, "increase": 2},
        {"name": "Faster boat", "price": skill * 10, "increase": 5},
        {"name": "Sonar", "price": skill * 20, "increase": 10},
    ]

    return render_template(
        "index.html", money=money, skill=skill, fish=fish, upgrades=upgrades
    )


if __name__ == "__main__":
    flaskrun(app)
