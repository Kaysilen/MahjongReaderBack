from flask import Flask, request, jsonify
from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter
from mahjong.hand_calculating.hand_config import HandConfig
from mahjong.meld import Meld

calculator = HandCalculator()

app = Flask(__name__)

@app.route('/')
def hello_world():
    tiles = TilesConverter.string_to_136_array(man='22444', pin='333567', sou='444')
    win_tile = TilesConverter.string_to_136_array(sou='4')[0]

    result = calculator.estimate_hand_value(tiles, win_tile)
    return str(result.han) + ' ' + str(result.fu)

@app.route('/analysisMahjongCard', methods = ['POST'])
def mahjongCard():
    mahjongSet = request.get_json();

    tiles = TilesConverter.string_to_136_array(man=mahjongSet['man'], pin=mahjongSet['pin'], sou=mahjongSet['sou'], honors=mahjongSet['honors']);

    winTileInfo = mahjongSet['winTile']

    if winTileInfo['type'] == "man":
        winTile = TilesConverter.string_to_136_array(man = winTileInfo['value'])[0]
    elif winTileInfo['type'] == "pin":
        winTile = TilesConverter.string_to_136_array(pin = winTileInfo['value'])[0]
    elif winTileInfo['type'] == "sou":
        winTile = TilesConverter.string_to_136_array(sou = winTileInfo['value'])[0]
    elif winTileInfo['type'] == "honors":
        winTile = TilesConverter.string_to_136_array(honors = winTileInfo['value'])[0]
    
    result = calculator.estimate_hand_value(tiles, winTile)

    return jsonify({
        "han":result.han,
        "fu":result.fu,
        "cost":result.cost['main'],
        "yaku":str(result.yaku)
    });


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')