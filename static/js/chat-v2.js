/*function getRandomInt(min, max) {
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

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

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

// code by https://github.com/lukedmartin/morse
let morse = (function() {
	var isSilent = true,
		alpha = {
			A: ".-",
			B: "-...",
			C: "-.-.",
			D: "-..",
			E: ".",
			F: "..-.",
			G: "--.",
			H: "....",
			I: "..",
			J: ".---",
			K: "-.-",
			L: ".-..",
			M: "--",
			N: "-.",
			O: "---",
			P: ".--.",
			Q: "--.-",
			R: ".-.",
			S: "...",
			T: "-",
			U: "..-",
			V: "...-",
			W: ".--",
			X: "-..-",
			Y: "-.--",
			Z: "--..",
			" ": "/",
			"1": ".----",
			"2": "..---",
			"3": "...--",
			"4": "....-",
			"5": ".....",
			"6": "-....",
			"7": "--...",
			"8": "---..",
			"9": "----.",
			"0": "-----"
		},
		morse = flipObject(alpha);

	morse["|"] = " ";

	function flipObject(obj) {
		var ret = {},
			prop;

		for ( prop in obj ) ret[obj[prop]] = prop;

		return ret;
	}

	function encode( str ) {
		var ret = "",
			i = 0,
			len = str.length;

		str = str.toUpperCase();

		for ( ; i < len; i++ ) {
			if ( alpha[ str.charAt(i) ] )
				ret += " " + alpha[ str.charAt(i) ];
			else if ( !isSilent )
				new Error("morse.encode: Can't handle " + str.charAt(i));
		}

		return ret.slice(1);
	}

	function decode( str ) {
		var split = str.split(" "),
            ret = "",
			i = 0,
			len = split.length;

		for ( ; i < len; i++ ) {
			if ( morse[ split[i] ] )
				ret += morse[ split[i] ];
			else if ( !isSilent )
				new Error("morse.decode: Can't handle " + split[i]);
		}

		return ret;
	}

	return {
		encode: encode,
		decode: decode,
		silent: function() {
			isSilent = !!arguments.length;
		}
	};

})();

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
  }
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

async function play(s) {
  var player = context.createOscillator();
  player.frequency.value = 800;
  player.type = "sine";

  var encoded = morse.encode(s)
  document.getElementById('key').disabled = true;
  for (const char of encoded) {
    if (char == "-") {
      red();
      await sleep(600);
      lime();
    } else if (char == ".") {
      red();
      await sleep(200);
      lime();
    } else if (char == "/") {
      await sleep(1000);
    } else if (char == " ") {
      await sleep(200);
    }
  }
  document.getElementById('key').disabled = false;
}*/

var context = new AudioContext();
var o = context.createOscillator();

var frequency = 550.0;
o.frequency.value = frequency;
var ontime = 0;
var offtime = 0;
var intervalon = 0;
var intervaloff = 0;
var message;
let ditdah = "";
let a = true;
let b = true;
let wpm = 5;

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
  a = true;
  b = true;
}

function htmlDecode(input) {
  var doc = new DOMParser().parseFromString(input, "text/html");
  return doc.documentElement.textContent;
}

function setfreq() {
  var freq = document.getElementById('freq').value;
  var submit = document.getElementById('submit');
  submit.style.backgroundColor = "red";
  frequency = freq;
  o.frequency.value = frequency;
}

function setwpm() {
  var setwpm = document.getElementById("setwpm");
  setwpm.style.backgroundColor = "red";
  wpm = document.getElementById('wpm').value;
}

function black() {
  var submit = document.getElementById('submit');
  submit.style.backgroundColor = "black";
}

function black2() {
  var setwpm = document.getElementById('setwpm');
  setwpm.style.backgroundColor = "black";
}

function count() {
  ontime++;
}

function countoff() {
  offtime++;

  if (offtime > 1.2 / wpm * 700) {
    if (b) {
      document.getElementById('result').value += "  ";
      b = false;
    }
    ditdah = "";
  } else if (offtime > 1.2 / wpm * 300) {
    //document.getElementById('result').value += decodeMorse(message).toUpperCase();
    if (a) {
      document.getElementById('result').value += " ";
      a = false;
    }
    ditdah = "";
  }
}

function dit_or_dah() {
  if (ontime < 1.2 / wpm * 100) {
    ditdah += ".";
    document.getElementById('result').value = document.getElementById('result').value.slice(0, -1)
    document.getElementById('result').value += decodeMorse(ditdah).toUpperCase();
    console.log(decodeMorse(ditdah).toUpperCase());
  } else {
    ditdah += "-";
    document.getElementById('result').value = document.getElementById('result').value.slice(0, -1)
    document.getElementById('result').value += decodeMorse(ditdah).toUpperCase();
    console.log(decodeMorse(ditdah).toUpperCase());
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
  document.getElementById('output').value += document.getElementById('result').value + "\n";
  document.getElementById('result').value = "";
}

function cancel() {
  document.getElementById('result').value = "";
}

document.addEventListener('keydown', (e) => {
  if (e.code === "Enter")        send();
  if (e.code === "Escape")         document.getElementById('result').value = "";
});

function block() {
  window.open("../action/" + document.getElementById('name').value, '_blank').focus();
}

function loadLogs() {
  $.ajax({
    url: "/logs-v2",
    async: true,
    success: function (data){
      document.getElementById("chat").innerHTML = JSON.parse(data)['logs'];

      // console.log(JSON.parse(JSON.parse(JSON.stringify(data))));
      
      /*
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
      */
      // $('#output').val(data);
    }
  });
}

setInterval(loadLogs, 100);