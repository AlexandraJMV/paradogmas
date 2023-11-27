function updateChart2() {
    let selectedData = document.getElementById('dataSelect2').value;

    // Make an asynchronous request to the Flask route to get data
    fetch(`/get_data2/${selectedData}`)
        .then(response => response.json())
        .then(data => { 

            if (charty) {
                charty.destroy(); // Corrected variable name here
            }

            // Create a new chart with the received data
            let ctx = document.getElementById('charty').getContext('2d');
            charty = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: data.index,
                    datasets: [{
                        label: document.getElementById('dataSelect2').value,
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
            charty.update(); // Corrected method name here
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

let ctx2 = document.getElementById('charty').getContext('2d');
let charty = new Chart(ctx2, {
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