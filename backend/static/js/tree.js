let chartum = null; 

function destroyChart(chart) {
    return new Promise(resolve => {
        if (chart !== null && chart.destroy) {
            chart.destroy();
            resolve();
        } else {
            resolve();
        }
    });
}

function updateChart3() {
    let selectedData_1 = document.getElementById('dataSelect3_1').value;
    let selectedData_2 = document.getElementById('dataSelect3_2').value;

    fetch(`/get_data3/${selectedData_1}/${selectedData_2}`)
        .then(response => response.json())
        .then(data => {
            destroyChart(chartum).then(() => {


                let ctx = document.getElementById('chartum').getContext('2d');
                chartum = new Chart(ctx, {
                    type: 'scatter',
                    data: {
                        datasets: [{
                            label: selectedData_1 + " vs " + selectedData_2,
                            data: data,
                            backgroundColor: 'rgba(260, 110, 130, 0.8)',
                        }]
                    },
                    options: {
                        scales: {
                            x: {
                                type: 'linear',
                                position: 'bottom',
                                title:{
                                    display : true,
                                    text: selectedData_1,
                                    color:'rgba(255, 255, 255, 0.7)'
                                },
                                ticks: {
                                    color: 'rgba(255, 255, 255, 0.7)'
                                },
                                grid: {
                                    color: 'rgba(255, 255, 255, 0.7)'
                                }
                            },
                            y: {
                                type: 'linear',
                                title:{
                                    display:true,
                                    text:selectedData_2,
                                    color: 'rgba(255, 255, 255, 0.7)'
                                },
                                ticks: {
                                    color: 'rgba(255, 255, 255, 0.7)'
                                },
                                grid: {
                                    color: 'rgba(255, 255, 255, 0.7)'
                                }

                            }
                        },
                        plugins: {
                            tooltip: {
                              callbacks: {
                                label: function (context) {
                                  var label = context.dataset.data[context.dataIndex].label || '';
                                  return label;
                                }
                              }
                            },
                            legend: {
                                labels: {
                                    color: 'rgba(255, 255, 255, 0.7)'
                                }
                            }
                          },
                          
                    }
                });
                chartum.update();
            });
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
}

let ctx3 = document.getElementById('chartum').getContext('2d');
    chartum = new Chart(ctx3, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Scatter Plot',
                data: [],
                backgroundColor: 'rgba(260, 110, 130, 0.8)'
            }]
        },
        options: {
            scales: {
                x: {
                    type: 'linear',
                    position: 'bottom',
                    ticks: {
                        color: 'rgba(255, 255, 255, 0.7)'
                    },
                    grid: {
                        color: 'rgba(255, 255, 255, 0.7)'
                    }
                },
                y: {
                    min: 0,
                    ticks: {
                        color: 'rgba(255, 255, 255, 0.7)'
                    },
                    grid: {
                        color: 'rgba(255, 255, 255, 0.7)'
                    }
                },
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

    document.getElementById('data1_button').addEventListener('click', updateChart3);
    document.getElementById('data2_button').addEventListener('click', updateChart3);

    

