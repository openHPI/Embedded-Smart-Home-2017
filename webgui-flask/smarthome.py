from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

from tiles import SimpleTile, TileManager
from helper import PageContext

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def main():
    tiles = [
        SimpleTile("Licht", "#EEEE00", "light/"),
        SimpleTile("Heizung", "#FF0000", "heaters/"),
        SimpleTile("Sicherheit", "#30FF00", "security/"),
        SimpleTile("Wasser", "#0000FF", "water/"),
        SimpleTile("Extrapunkt 1", "#00FFFF", "/"),
        SimpleTile("Extrapunkt 2", "#FF00FF", "/"),
        SimpleTile("Extrapunkt 3", "#A0FFA0", "/"),
        SimpleTile("Extrapunkt 4", "#00A0FF", "/"),
    ]

    manager = TileManager(tiles)
    context = PageContext("Smarthome Projekt", "Home")
    return render_template("main.html", tilerows=manager, context=context)

@app.route('/light/')
def light():
    living_room = True
    sleeping_room = False

    if("living_room" in request.args):
        living_room = True if request.args["living_room"] == "on" else False

    if("sleeping_room" in request.args):
        sleeping_room = True if request.args["sleeping_room"] == "on" else False

    tiles=[]

    tile = SimpleTile("Wohnzimmer: ", "", "?living_room=")
    tile.items[0].text += "an" if living_room else "aus"
    tile.link += "off" if living_room else "on"
    tile.bg = "#AAFF00" if living_room else "#338800"
    tiles.append(tile)

    tile = SimpleTile("Schlafzimmer: ", "", "?sleeping_room=")
    tile.items[0].text += "an" if sleeping_room else "aus"
    tile.link += "off" if sleeping_room else "on"
    tile.bg = "#6666BB" if sleeping_room else "#333388"
    tiles.append(tile)

    manager = TileManager(tiles)
    context = PageContext("Smarthome Projekt", "Licht", [["/", "Home"]])
    return render_template("main.html", tilerows=manager, context=context)
