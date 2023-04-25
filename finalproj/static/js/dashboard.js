/* globals Chart:false, feather:false */

(function () {
  'use strict'

  feather.replace({ 'aria-hidden': 'true' })

  // Graphs
  var ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [
        '白天', '晚上',
        '白天', '晚上',
        '白天', '晚上',
        '白天', '晚上',
        '白天', '晚上',
        '白天', '晚上',
        '白天', '晚上'
      ],
      datasets: [
        {
          label: 'High Temperature',
          data: [
            30, null,
            28, null,
            25, null,
            27, null,
            30, null,
            31, null,
            30, null
          ],
          lineTension: 0,
          backgroundColor: 'transparent',
          borderColor: '#f44336',
          borderWidth: 4,
          pointBackgroundColor: '#f44336',
          spanGaps: true,
          fill: false
        },
        {
          label: 'Low Temperature',
          data: [
            null, 16,
            null, 16,
            null, 15,
            null, 15,
            null, 16,
            null, 18,
            null, 18
          ],
          lineTension: 0,
          backgroundColor: 'transparent',
          borderColor: '#2196f3',
          borderWidth: 4,
          pointBackgroundColor: '#2196f3',
          spanGaps: true,
          fill: false
        }
      ]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: true
      }
    }
  })
})()
