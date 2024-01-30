function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min);
}

function loadLogs() {
  $.ajax({
    url: "/logs",
    async: true,
    success: function (data){
      // console.log(JSON.parse(JSON.parse(JSON.stringify(data))));

      if (JSON.parse(JSON.parse(JSON.stringify(data)))['blocked'].length == 0) {
        $('#output').val(JSON.parse(JSON.parse(JSON.stringify(data)))['logs'].replaceAll('\\n', '\n'));
      } else {
        for (const u of JSON.parse(JSON.parse(JSON.stringify(data)))['blocked']) {
        console.log(u)
        $('#output').val(JSON.parse(JSON.parse(JSON.stringify(data)))['logs'].replaceAll('\\n', '\n').split('\n').filter(function(line){
          return line.indexOf(u.toUpperCase()) == -1;
        }).join('\n'));
      }
      }
      // $('#output').val(data);
    }
  });
  document.getElementById('output').scrollTop = document.getElementById('output').scrollHeight
}

setInterval(loadLogs, 100);

document.getElementById("freq").value = getRandomInt(500, 1000);

var frequency = document.getElementById("freq").value;

var context = new AudioContext();
var o = context.createOscillator();

o.frequency.value = frequency;
var ontime = 0;
var offtime = 0;
var intervalon = 0;
var intervaloff = 0;
var message = "";
var log = ""

var MORSE_CODE = {".-": "a", "-...":"b", "-.-.": "c", "-..": "d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j", "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o", ".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y", "--..":"z", ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9", "-----":"0", "|":" ", "..--":"\n"};

var decodeMorse = function(morseCode){
  var words = (morseCode).split('  ');
  var letters = words.map((w) => w.split(' '));
  var decoded = [];

  for(var i = 0; i < letters.length; i++){
    decoded[i] = [];
    for(var x = 0; x < letters[i].length; x++){
        if(MORSE_CODE[letters[i][x]]){
            decoded[i].push( MORSE_CODE[letters[i][x]] );
        }
    }
  }

  return decoded.map(arr => arr.join('')).join(' ');
}

function red() {
  var key = document.getElementById('key');
  key.style.backgroundColor = "red";
  clearInterval(intervalon);
  o.type = "sine";
  o.connect(context.destination);
  o.start();
  ontime = 0;
  intervalon = setInterval(count, 10);
}

function lime() {
  var key = document.getElementById('key');
  key.style.backgroundColor = "lime";
  o.disconnect(context.destination);
  o.stop();
  o = context.createOscillator();
  o.frequency.value = frequency;
  clearInterval(intervaloff);
  dit_or_dah();
  offtime = 0;
  intervaloff = setInterval(countoff, 10);
}

function setfreq() {
  var freq = document.getElementById('freq').value;
  var submit = document.getElementById('submit');
  submit.style.backgroundColor = "red";
  frequency = freq;
  o.frequency.value = frequency;
}

function black() {
  var submit = document.getElementById('submit');
  submit.style.backgroundColor = "black";
}

function count() {
  ontime++;
}

function countoff() {
  offtime++;
  if (offtime > 60) {
    log += decodeMorse(message).toUpperCase();
    $.post( "/getvar", {
        javascript_data: log
    });
    message = "";
    log = "";
    clearInterval(intervaloff);
  }/* else if (offtime > 60) {
    log += decodeMorse(message).toUpperCase();
    message = "";
  }
  */
}

function dit_or_dah() {
  if (ontime < 25) {
    message = message + ".";
  } else {
    message = message + "-";
  }
}

function block() {
  window.open("../action/" + document.getElementById('name').value, '_blank').focus();
}