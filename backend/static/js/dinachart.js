

function updateChart() {
    let selectedData = document.getElementById('dataSelect').value;

    // Make an asynchronous request to the Flask route to get data
    fetch(`/get_data/${selectedData}`)
        .then(response => response.json())
        .then(data => { 
    
    if (myChart) {
        myChart.destroy();
    }

    let colors = generateRandomColorsArray(data.data.length, function(){ 
        const hue = (Math.random() < 0.5 ? Math.random() * 20 : 320 + Math.random() * 60);

            const saturation = Math.floor(Math.random() * 70) + 40;
            const lightness = Math.floor(Math.random() * 50) + 20; // Adjust as needed for a darker or lighter appearance
      
            const pastelColor = `hsl(${hue}, ${saturation}%, ${lightness}%, 0.5)`;
          
            return pastelColor;
          })

    // Create a new chart with the received data
    let ctx = document.getElementById('myChart').getContext('2d');
    myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.index,
            datasets: [{
                label: document.getElementById('dataSelect').value,
                data: data.data,
                backgroundColor: colors,
                borderColor: 'rgba(120, 70, 70, 0.7)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                x: {
                    title:{
                        display : true,
                        text: 'Nombre de los artistas'
                    }
                },
                y: {
                    title:{
                        display:true,
                        text:'Conteo'
                    }

                }
            }
            
        }
    });
    myChart.update();
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}


console.log('no  entiendoo')
let ctx = document.getElementById('myChart').getContext('2d');
let myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [],
        datasets: [{
            label: 'Selected Data',
            data: [],
            backgroundColor: 'rgba(200, 70, 40, 0.7)',
            borderColor: 'rgba(200, 70, 40, 0.7)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            x: {
                title:{
                    display : true,
                    text: 'Nombre de los artistas'
                }
            },
            y: {
                title:{
                    display:true,
                    text:'Conteo'
                }

            }
        }
    }
});
