document.addEventListener('DOMContentLoaded', function() {
    loadBalance();
    loadDaily_timeremaining();
})

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

async function loadDaily_timeremaining() {
    try {
        const result = await apiCall('/api/daily_timecheck');
        let currentTime = result.daily_timeremaining;
        const TimeEl = document.getElementById('TimeDaily');
        TimeEl.textContent = `${currentTime}`;
    } catch (error) {
        document.getElementById('TimeDaily').textContent = 'Error loading time';
    }
}

async function Daily() {

    const result = await apiCall('/api/daily');
    let successful = result.successful;
    
    if (successful) {
        alert('Process successful')
    }
    else{
        alert('Process unsuccessful')
    }

}