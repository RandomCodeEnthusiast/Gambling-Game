document.addEventListener('DOMContentLoaded', function() {
    loadBalance();
    loadStoneCount();
});

window.addEventListener('beforeunload', () => {
  removeEventListener('DOMContentLoaded')
  removeEventListener('beforeunload')
});

async function apiCall(endpoint, method = 'GET', data = null) {
    try {
        const options = {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            }
        };
                
        if (data) {
            options.body = JSON.stringify(data);
        }
                
        const response = await fetch(endpoint, options);
        const result = await response.json();
                
        if (!response.ok) {
            throw new Error(result.error || 'API call failed');
        }
        return result;
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

async function loadBalance() {
    try {
        const result = await apiCall('/api/balance');
        let currentBalance = result.balance;
        const balanceEl = document.getElementById('balance');
        balanceEl.textContent = `${currentBalance} Chips`;
    } catch (error) {
        document.getElementById('balance').textContent = 'Error loading balance';
    }
}

async function loadStoneCount() {
    try {
        const result = await apiCall('/api/stonecount');
        let currentStoneCount = result.stonecount;
        const stonecountEl = document.getElementById('stonecount');
        stonecountEl.textContent = `${currentStoneCount} Stones`;
    } catch (error) {
        document.getElementById('stonecount').textContent = 'Error loading stonecount';
    }
}

async function BuyStone(amount = 1) {

    const result = await apiCall('/api/stonebuy');
    let successful = result.buysuccess;
    
    if (successful) {
        alert('Process successful')
    }
    else{
        alert('Process unsuccessful')
    }
    loadBalance()
    loadStoneCount()

}