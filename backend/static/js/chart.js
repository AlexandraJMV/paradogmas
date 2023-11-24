const ctx = document.getElementById('myChart');
var dataElement = document.getElementById("data");
var data = dataElement.dataset.value;
console.log(data)

var jsonData = JSON.parse(data);

console.log(jsonData)

new Chart(ctx, {
  type: 'bar',
  data: {
    labels: jsonData.index,
    datasets: [{
      label: jsonData.name,
      data: jsonData.data,
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});