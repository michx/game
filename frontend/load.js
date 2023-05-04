let data = [];

// Make AJAX call to API
fetch('https://example.com/api')
	.then(response => response.json())
	.then(jsonData => {
		// Loop through data returned by API
		jsonData.forEach(item => {
			// Convert timestamp to Date object
			let date = new Date(item.timestamp);

			// Add data point to array
			data.push({
				x: date,
				y: item.value
			});
		});

		// Create chart with data
		createChart(data);
	})
	.catch(error => {
		console.error(error);
	});

function createChart(data) {
	// Get canvas element and context
	let canvas = document.getElementById('myChart');
	let context = canvas.getContext('2d');

	// Create chart object
	let chart = new Chart(context, {
		type: 'line',
		data: {
			datasets: [{
				label: 'My Data',
				data: data,
				fill: false,
				borderColor: 'rgb(75, 192, 192)',
				lineTension: 0.1
			}]
		},
		options: {
			scales: {
				xAxes: [{
					type: 'time',
					time: {
						unit: 'minute'
					}
				}]
			}
		}
	});
}
