const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require("ip");


http.createServer((req, res) => {
        if (req.url === "/") {
                fs.readFile("./Public/index.html", "UTF-8", (err, body) => {
                res.writeHead(200, {"Content-Type": "text/html"});
                res.end(body);
        });
        } else if(req.url.match("/sysinfo")) {
	myUpTime =(os.uptime() / 864000);
        myHostName = os.hostname();
	myTotMem = (os.totalmem() / 10000);
	myFreeMem = (os.freemem() / 10000);
        html = `
        <!DOCTYPE html>
        <html>
                <head>
                        <title>Node JS Response</title>
                </head>
                <body>
                <p>Hostname: ${myHostName}</p>
                <p>IP: ${ip.address()}</p>
                <p>Server Uptime:${myUpTime} Days</p>
		<p>Total Memory: ${myTotMem} MB</p>
                <p>Free Memory:${myFreeMem} MB</p>
                <p>Number of CPUs:${os.cpus().length} </p>
                </body>
        </html>`

        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
        } else {
        res.writeHead(404, {"content-Type": "text/plain"});
        res.end("404 File Not found at ${req.url}");
        }
}).listen(3000);

console.log("Server listening on port 3000");
