const express = require('express');
const app = express();
const http = require('http').Server(app);
var chokidar = require('chokidar');
const io = require('socket.io')(http);

const port = process.env.PORT || 3000;

app.use(express.static(__dirname + '/.'));

http.listen(port, () => console.log('listening on port ' + port));

var watcher = chokidar.watch("/Volumes/grau'"+"s/0-proj/_faces/narciatio/v4/output/crop/", {
	ignored: /[\/\\]\./, persistent: true
});

var log = console.log.bind(console);
  
watcher
	.on('add', function(path) { 
		var test = "/Volumes/grau'"+"s/0-proj/_faces/narciatio/v4/";
		var newPath = path.replace(test, "");
		log('File', newPath, 'has been added');
		io.emit('PATH',newPath)
	})
	.on('ready', function() { log('Initial scan complete. Ready for changes.'); })
	
io.on('connection', function(socket){
	console.log('a user connected');});;