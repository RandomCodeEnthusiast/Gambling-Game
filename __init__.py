from flask import Flask,render_template

from InventoryManagement.MoneyManagement.money import Money
from Roulette.RouletteGame import Roulette_Game

app = Flask('gambling')

@app.route('/')
def MainPage():
    return Flask.redirect(self=Flask,location='/home',code=302)

@app.route('/home')
def home():
    return render_template('home.html')

def GUI_Roulette() :
    @app.route('/Roulette')
    def roulette():
        result : tuple = Roulette_Game(Player=1)
        return render_template('roulette.html',Number = result[0], Color = result[1])

@app.route('/Balance')
def balance():
    funds = Money(Player=1)
    return render_template('balance.html', balance = str(funds))

@app.route('/Others')
def others():
    return render_template('Others.html')

if __name__ == '__main__':
    app.run(debug=True)