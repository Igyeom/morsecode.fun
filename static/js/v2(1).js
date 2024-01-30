var context = new AudioContext();
var o = context.createOscillator();

var frequency = 550.0;
o.frequency.value = frequency;
var ontime = 0;
var offtime = 0;
var intervalon = 0;
var intervaloff = 0;
var message;
let ditdah;
let letter;

var MORSE_CODE = {".-": "a", "-...":"b", "-.-.": "c", "-..": "d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j", "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o", ".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t", "..-":"u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y", "--..":"z", ".----":"1", "..---":"2", "...--":"3", "....-":"4", ".....":"5", "-....":"6", "--...":"7", "---..":"8", "----.":"9", "-----":"0", "|":" "};

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
    /*ditdah += "   ";
    document.getElementById('result').value += decodeMorse(message).toUpperCase();
    ditdah = "";
    message = "";
    clearInterval(intervaloff);*/
  } else if (offtime > 20) {
    //document.getElementById('result').value += decodeMorse(message).toUpperCase();
  }
}

function dit_or_dah() {
  if (ontime < 20) {
    ditdah += ".";
    document.getElementById('result').value = document.getElementById('result').value.slice(0, -1)
    document.getElementById('result').value += decodeMorse(ditdah).toUpperCase();
  } else {
    ditdah += "-";
    document.getElementById('result').value = document.getElementById('result').value.slice(0, -1)
    document.getElementById('result').value += decodeMorse(ditdah).toUpperCase();
  }
}

function request() {
  if (document.getElementById('report').checked) {
    window.location.href = "../../report/" + document.getElementById('user').innerHTML;
  } else {
    window.location.href = "../../act/" + document.getElementById('user').innerHTML;
  }
}

function send() {
  document.getElementById('output').value += document.getElementById('result').value + "\n"
  document.getElementById('result').value = "";
}

document.addEventListener('keydown', (e) => {
  if (e.code === "Enter")        send();
});