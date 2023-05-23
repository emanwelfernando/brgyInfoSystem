var single = document.getElementById('totalSingles').value;
var married = document.getElementById('totalMarried').value;
var divorced = document.getElementById('totalDivorced').value;

const ctx = document.getElementById('residentChart');

new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Singles', 'Married', 'Divorced'],
    datasets: [{
      label: 'Barangay Marital Statuses',
      data: [single, married, divorced],
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