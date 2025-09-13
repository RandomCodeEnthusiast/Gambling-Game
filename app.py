from flask import Flask,render_template

from Data.InventoryManagement.MoneyManagement.money import Money
from Data.InventoryManagement.MoneyManagement.Daily import Daily,DailyTimeCheck
from Data.InventoryManagement.StoneManagement.Stone import StoneCheck,StoneBuy
from Games.Roulette.RouletteGame import Roulette_Game

app = Flask('gambling')

@app.route('/')
def MainPage():
    return Flask.redirect(self=Flask,location='/home',code=302)

@app.route('/api/balance', methods=['GET'])
def get_balance():
    balance = Money(Player=1)
    return {"balance": balance}

@app.route('/api/stonecount', methods=['GET'])
def get_stonecount():
    stonecount = StoneCheck()
    return{"stonecount" : stonecount}

@app.route('/api/stonebuy', methods=['GET'])
def buy_Stones():
    successful = StoneBuy()
    return{"buysuccess" : successful}

@app.route('/api/daily_timecheck', methods=['GET'])
def DailyTimeCheck_API():
    time = DailyTimeCheck()['MissingTime']

    #converting time to a string to jsonify it and for appeareance purposes
    if time == 0 :
        time = 'You can claim your daily loggin bonus NOW !'

    else :

        seconds = time.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        time = f"{hours} Hours {minutes} minutes {seconds} seconds"

    return{"daily_timeremaining" : time} 

@app.route('/api/daily', methods=['GET'])
def Daily_API():

    successful = Daily()['successful']

    return {"successful" : successful}


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/Daily')
def Daily_Page():

    return render_template('Daily.html')

@app.route('/Roulette')
def roulette():
    return render_template('roulette.html',Play = False)

@app.route('/Roulette_setup')
def roulette_setup():
    balance = Money(Player=1)
    return render_template('roulette.html',Play = False, Setup = True, Funds = balance)

@app.route('/Roulette_play')
def roulette_play():
    RouletteGame_Data : dict = Roulette_Game(Player=1)
    result : tuple = RouletteGame_Data['Result']
    WinStatus = RouletteGame_Data['Win']
    Reward = RouletteGame_Data['Reward']
    return render_template('roulette.html',Play = True, Number = result[0], Color = result[1],GameWon = WinStatus,GameReward = Reward)


@app.route('/Balance')
def balance():
    #funds = Money(Player=1)
    return render_template('balance.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/Others')
def others():
    return render_template('Others.html')

if __name__ == '__main__':
    app.run(debug=True)