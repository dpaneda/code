#!/usr/bin/env node
 
var net = require('net');
var util = require('util');
var crypto = require('crypto');
 
var message = require('fs').readFileSync('./message.txt').toString().trim();
 
net.createServer(function(socket) {
 
    var dh, state = 0;
 
    socket.write('hello\n');
 
    socket.on('data', function(data) {
 
        data = data.toString().trim().split('|');
 
        if (state == 0 && data[0] == 'hello') {
            dh = crypto.createDiffieHellman(256);
            dh.generateKeys();
            socket.write(util.format('key|%s|%s\n', dh.getPrime('hex'), dh.getPublicKey('hex')));
            state++;
 
        } else if (state == 1 && data[0] == 'key') {
            var secret = dh.computeSecret(data[1], 'hex');
            var cipher = crypto.createCipher('aes192', secret);
            var secure = cipher.update(message, null, 'hex') + cipher.final('hex');
            socket.write(util.format('message|%s\n', secure));
            state++;
 
        } else {
            socket.write('Error\n');
            socket.end();
        }
 
    });
 
}).listen(6767, '0.0.0.0', function() {
    console.log('listening...');
});
