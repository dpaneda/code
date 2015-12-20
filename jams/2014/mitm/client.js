#!/usr/bin/env node
 
var net = require('net');
var util = require('util');
var crypto = require('crypto');
 
var options = {
    'port': 6767,
    'host': '0.0.0.0',
}
 
var dh, secret, state = 0;
 
var socket = net.connect(options, function() {});
 
socket.on('data', function(data) {
 
    data = data.toString().trim().split('|');
 
    if (state == 0 && data[0] == 'hello') {
        socket.write('hello\n');
        state++;
 
    } else if (state == 1 && data[0] == 'key') {
        dh = crypto.createDiffieHellman(data[1], 'hex');
        dh.generateKeys();
        secret = dh.computeSecret(data[2], 'hex');
        socket.write(util.format('key|%s\n', dh.getPublicKey('hex')));
        state++;
 
    } else if (state == 2 && data[0] == 'message') {
        var decipher = crypto.createDecipher('aes192', secret);
        var message = decipher.update(data[1], 'hex', 'utf8') + decipher.final('utf8');
        console.log(message);
        socket.end();
 
    } else {
        console.log('Error');
        socket.end();
    }
 
});
