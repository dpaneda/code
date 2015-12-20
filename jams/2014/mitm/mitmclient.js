#!/usr/bin/env node
 
var net = require('net');
var util = require('util');
var crypto = require('crypto');
 
var options = {
    'port': 6969,
    'host': 'pladaria.vpn.tuenti.local',
}
 
var dh, secret = 0;
var socket = net.connect(options, function() {});
 
socket.on('data', function(data) {
    mitm_data = data.toString().trim().split(':')
    direction = mitm_data[0]
    raw_data = mitm_data[1]
    data = raw_data.split('|');
 
    if (data[0] == 'hello') {
        socket.write('hello\n');
 
    } else if (data[0] == 'key') {
        if (direction == 'SERVER->CLIENT') {
            dh = crypto.createDiffieHellman(data[1], 'hex');
            dh.generateKeys();
            secret = dh.computeSecret(data[2], 'hex');
            socket.write(raw_data);
        } else {
          socket.write(util.format('key|%s\n', dh.getPublicKey('hex')));
        }
 
    } else if (data[0] == 'message') {
        var decipher = crypto.createDecipher('aes192', secret);
        var message = decipher.update(data[1], 'hex', 'utf8') + decipher.final('utf8');
        console.log(message);
        socket.end();
 
    } else {
        console.log('Error');
        socket.end();
    }
 
});
