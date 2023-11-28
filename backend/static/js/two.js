function generateRandomColorsArray(numColors, colorGenerator) {
    const colorsArray = [];
  
    // Generate the specified number of random colors
    for (let i = 0; i < numColors; i++) {
      const randomColor = colorGenerator();
      colorsArray.push(randomColor);
    }
  
    return colorsArray;
  }

function updateChart2() {
    let selectedData = document.getElementById('dataSelect2').value;

    fetch(`/get_data2/${selectedData}`)
        .then(response => response.json())
        .then(data => { 

            if (charty) {
                charty.destroy(); 
            }

            let colors = generateRandomColorsArray(data.data.length, function(){ 
                const hue = (Math.random() < 0.5 ? Math.random() * 20 : 320 + Math.random() * 60);

                    const saturation = Math.floor(Math.random() * 50) + 25;
                    const lightness = Math.floor(Math.random() * 50) + 40; 
              
                    const pastelColor = `hsl(${hue}, ${saturation}%, ${lightness}%)`;
                  
                    return pastelColor;
                  })

            let ctx = document.getElementById('charty').getContext('2d');
            charty = new Chart(ctx, {
                type: 'pie',
                data: {
                    labels: data.index,
                    datasets: [{
                        label: document.getElementById('dataSelect2').value,
                        data: data.data,
                        backgroundColor: colors
                    }]
                },
                options: {
                    elements: {
                        arc: {
                            borderColor: 'rgba(255, 255, 255, 0.3)', 
                            borderWidth: 2
                        }
                    },
                    plugins: {
                        legend: {
                            labels: {
                                color: 'rgba(255, 255, 255, 0.7)'
                            }
                        }
                    }
                }
            });
            charty.update(); 
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

let ctx2 = document.getElementById('charty').getContext('2d');
let charty = new Chart(ctx2, {
    type: 'pie',
    data: {
        labels: [],
        datasets: [{
            label: 'Selected Data',
            data: [],
            backgroundColor: [],
            borderWidth: 1
        }]
    },
    options: {
    }
});