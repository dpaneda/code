var net = require('net');
var util = require('util');
var crypto = require('crypto');
var readline = require('readline');

/*
var options = {
  'port': 6767,
  'host': '0.0.0.0',
}


var socket = net.connect(options, function() {});
*/

var dh, secret, state = 0;
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

dh = crypto.createDiffieHellman(256);
dh.generateKeys();

rl.on('line', function(line){
    var data = line.toString().trim().split(':');
    var direction = data[0];
    var message = data[1].split('|');
    
    //console.log(direction);
    //console.log(message);

    if (message[0] == 'key') {
      if (direction == 'SERVER->CLIENT') {
        //dh = crypto.createDiffieHellman(message[1], 'hex');
        console.log(util.format('%s:key|%s|%s\n',
            direction,
            dh.getPrime('hex'), 
            dh.getPublicKey('hex')));
      } else {
        secret = dh.computeSecret(message[1], 'hex');
      }
    }
    
    if (message[0] == 'message') {
        cipher = crypto.createCipher('aes192', secret);
        console.log(decipher.update(message[1], 'hex', 'utf8') + decipher.final('utf8'));
    }
})
