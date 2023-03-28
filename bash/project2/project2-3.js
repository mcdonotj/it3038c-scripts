const http = require('http');
const server = http.createServer((req, res) => {
	res.writeHead(200, {'Content-Type': 'text/html' });
	res.write(`
	 <html>
	 <title> D&D Simulator</title>
	 <h1>Welcome to D&D Simulator! Choose your character!</h1>
	 <body>
		<button onclick="mage()">Mage</button>
		<button onclick="knight()">Knight</button>
		<button onclick="archer()">Archer</button>
		<div id="result"></div>
		<script>
			function mage() {
			const xhr1 = new XMLHttpRequest();
			xhr1.open('GET', '/', true);
			xhr1.onload = function() {
				const result = document.getElementId('result');
				result.innerHTML = this.responseText;
			};
			xhr1.send();
			}
		</script>
	</body>
	</html>
	`);
	
});


//response

server.on('request', (req, res) => {
	if (req.url === '/') {
		res.writeHead(200, {'Content-Type':'text/plain' });
		res.write('You chose Mage!');
		res.end();
	}
});

//server start


server.listen(3000, () => {
	console.log('Server listening on port 3000');
});
