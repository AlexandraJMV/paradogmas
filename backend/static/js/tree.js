function updateChart3() {
    let selectedData = document.getElementById('dataSelect3').value;

    // Make an asynchronous request to the Flask route to get data
    fetch(`/get_data/${selectedData}`)
        .then(response => response.json())
        .then(data => { 

            if (charty) {
                charty.destroy(); // Corrected variable name here
            }

            // Create a new chart with the received data
            let ctx = document.getElementById('chartum').getContext('2d');
            chartum = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.index,
                    datasets: [{
                        label: document.getElementById('dataSelect3').value,
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
            chartum.update(); // Corrected method name here
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

let ctx3 = document.getElementById('chartum').getContext('2d');
let chartum = new Chart(ctx3, {
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