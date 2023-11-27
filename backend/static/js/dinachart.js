function updateChart() {
    let selectedData = document.getElementById('dataSelect').value;

    // Make an asynchronous request to the Flask route to get data
    fetch(`/get_data/${selectedData}`)
        .then(response => response.json())
        .then(data => { 

    if (myChart) {
        myChart.destroy();
    }

    // Create a new chart with the received data
    let ctx = document.getElementById('myChart').getContext('2d');
    myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.index,
            datasets: [{
                label: document.getElementById('dataSelect').value,
                data: data.data,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            // Configure chart options as needed
        }
    });
    myChart.update();
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}


let ctx = document.getElementById('myChart').getContext('2d');
let myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: 'Selected Data',
            data: [],
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    },
    options: {
        // Configure chart options as needed
    }
});
