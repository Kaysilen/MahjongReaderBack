from flask import Flask
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

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')