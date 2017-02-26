const http = require('http');

const flag = "kyouko";

server = http.createServer();

server.on('request', function(request, response) {
    if (request.headers['password'] == undefined) { 
        response.end('Could Not Find "password" header');
    }

    var password = request.headers['password'] || '';

    var time = 0;

    for (var i = password.length - 1; i >= 0; i--) {
        if (flag[i] == undefined) {
            time = Math.random();
            break;
        } else if (flag[i] == password[i]) {
            time += Math.random() + 1.2;
        } else {
            break;
        }
    }

    time += Math.random();

    if (password == flag) {
        response.end('flag: kyouko');
    } else {
        response.end('Time taken: ' + time);
    }
});

server.listen(8090);

