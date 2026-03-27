document.addEventListener('DOMContentLoaded', function() {
    loadUI(false)
});

window.addEventListener('beforeunload', () => {
  removeEventListener('DOMContentLoaded')
  removeEventListener('beforeunload')
});

function loadUI(Betting = false,Results = false, Bet = 'none') {
    const PlayButton = document.getElementById('PlayButton')
    const BettingUI = document.getElementById('BettingUI')
    const BetNumberForm = document.getElementById('number-guess')
    const BetButtons = document.getElementById('bet-buttons')
    const ReturnButton = document.getElementById('return-button')
    const gameresultElement = document.getElementById('roulette-result');

    gameresultElement.style.visibility = 'hidden' ; gameresultElement.style.display = 'none'
    if (Betting) {
        
        PlayButton.style.visibility = 'hidden' ; PlayButton.style.display = 'none'
        BettingUI.style.visibility = 'visible'; BettingUI.style.display = 'block'

        if (Bet === 'number') {
            BetNumberForm.style.visibility = 'visible' ; BetNumberForm.style.display = 'block'
            BetButtons.style.visibility = 'hidden' ; BetButtons.style.display = 'none'
            ReturnButton.style.visibility = 'visible' ; ReturnButton.style.display = 'block'
            
        }
        else{
            BetButtons.style.visibility = 'visible' ; BetButtons.style.display = 'block'
            BetNumberForm.style.visibility = 'hidden' ; BetNumberForm.style.display = 'none'
        }
    }
    else if (Results) {
        BetNumberForm.style.visibility = 'hidden' ; BetNumberForm.style.display = 'none'
        BettingUI.style.visibility = 'hidden'; BettingUI.style.display = 'none';
        PlayButton.style.visibility = 'visible'; ; PlayButton.style.display = 'block'
        gameresultElement.style.visibility = 'visible' ; gameresultElement.style.display = 'block'
    }
    else {
        BetNumberForm.style.visibility = 'hidden' ; BetNumberForm.style.display = 'none'
        BettingUI.style.visibility = 'hidden'; BettingUI.style.display = 'none';
        PlayButton.style.visibility = 'visible'; PlayButton.style.display = 'block' 
    }
}
function GetBettingInfo() {
    const BetAmount = document.getElementById('roulette-bet-amount');
    if (BetType[0] === 'number') {
        const BetNumber = document.getElementById('roulette-bet-number');
        var msg  = 'You are betting ' + BetAmount.value + ' chips on : '+ BetNumber.value + ' !'
        var Bet = [BetType[0],BetNumber.value]
    }
    else if (BetType[0] === 'color') {
        var Bet = BetType
        var msg  = 'You are betting ' + BetAmount.value + ' chips on '+ BetType[1] + ' !'
    }
    else {
        var Bet = BetType
        var msg  = 'You are betting ' + BetAmount.value + ' chips on : '+ BetType[0] + ' !' 
    }
    alert(msg)

    return {
        'BetAmount' : BetAmount.value,
        'BetType' : Bet
    }
};
function Roulette (){
    var xml = new XMLHttpRequest();
    xml.open("POST","/Roulette_play",true)
    xml.setRequestHeader("Content-type","application/json");
    xml.onload = function(){
        var dataReply = JSON.parse(this.responseText);
        if (dataReply.Win) {
            var msg = 'You just won ' + dataReply.Reward + ' chips !' 
        }
        else {
            var msg = 'You just lost ' + BetInfo.BetAmount + ' chips...'
        }
        const msgElement = document.getElementById('win-message');
        const ballElement = document.getElementById('result-color&number');
        msgElement.textContent = `${msg}`;
        ballElement.textContent = `The ball just landed on ${dataReply.Result[0]} : ${dataReply.Result[1]}`
        loadUI(Betting = false,Results = true)
        
    };//endfunction
    var BetInfo = GetBettingInfo()
    dataSend= JSON.stringify({
        'BetType': BetInfo.BetType,
        'BetAmount' : BetInfo.BetAmount
    });
    xml.send(dataSend);
}
function selectBetType(type, precision='none') {
    BetType = [type,precision]
}