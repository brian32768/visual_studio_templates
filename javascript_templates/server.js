'use strict';
var http = require('http');
var port = process.env.PORT || 1337;
var path = require('path');
var fs = require('fs');
var base = '.';

http.createServer(function (req, res) {

    pathname = base + req.url;
    if (req.url === '/') {
        pathname = base + '/index.html';
    }

    ext = path.extname(pathname)
    var ct = "text/html";
    switch (ext) {
        case ".js":
            ct = "application/javascript";
            break;
        case '.png':
            ct = "application/image";
            break;
        case '.css':
            ct = "text/css";
            break;
    }

    try {
        var file = fs.createReadStream(pathname);
        res.setHeader('Content-Type', ct);
        res.statusCode = 200;
        file.on("open", function () {
            file.pipe(res);
        });
        console.log("Loaded ", pathname, ' as "', ct, '".');
    } catch (e) {
        res.writeHead(404);
        res.write('Page not found 404\n');
        res.write(e)
        res.end();
    }

