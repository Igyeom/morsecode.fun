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
let wpm = 2;
let m = [new Audio('../static/audio/metronome.wav'), new Audio('../static/audio/metronome-alt.wav')];
let vol = context.createGain();
vol.gain.value = 0.2;

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

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function metronome() {
    m[1].play();
    await sleep(1.2 / wpm * 1000);
    m[0].play();
    await sleep(1.2 / wpm * 1000);
    m[0].play();
    await sleep(1.2 / wpm * 1000);
    m[0].play();
    await sleep(1.2 / wpm * 1000);
    m[1].play();
    await sleep(1.2 / wpm * 1000);
}

async function metronomeExample() {
    m[1].play();
    await sleep(1.2 / wpm * 1000);
    m[0].play();
    red();
    await sleep(1.2 / wpm * 1000);
    m[0].play();
    await sleep(1.2 / wpm * 1000);
    m[0].play();
    await sleep(1.2 / wpm * 1000);
    m[1].play();
    lime();
    await sleep(1.2 / wpm * 1000);
}

async function sMetronomeExample() {
    m[0].play();
    red();
    await sleep(1.2 / wpm * 1000);
    lime();
}

async function sMetronome() {
    m[0].play();
    await sleep(1.2 / wpm * 100);
}

function red() {
  var key = document.getElementById('key');
  key.style.backgroundColor = "red";
  clearInterval(intervalon);
  o.type = "sine";
  o.connect(vol);
  vol.connect(context.destination);
  o.start();
  ontime = 0;
  intervalon = setInterval(count, 10);
}

function lime() {
  var key = document.getElementById('key');
  key.style.backgroundColor = "lime";
  vol.disconnect(context.destination);
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

let fired = false;


addEventListener("keydown", function(e){
    if (!fired && e.code !== "Escape" && e.code !== "Enter") {
        fired = true;
        red();
    }
});

addEventListener("keyup", function(e){
    if (e.code !== "Escape" && e.code !== "Enter") {
        fired = false;
        lime();
    }
});

async function start() {
    document.getElementById('guide').innerHTML = "Welcome to your free morse code course at morsecode.fun. For the first lesson, we will help you get used to the timings, and use a metronome to ease you into the skill, and teach you a few letters. Press the 'Key' button or press any key to continue."
    while (key.style.backgroundColor == "lime") {
        await sleep(50)
    }
    document.getElementById('guide').innerHTML += "<br><br>First, we'll let you hear the metronome. When there is a high-pitched beat, it means to get ready. Then at the first low beat after that, start holding down the key. When you hear another high beat, you release. The metronome will keep playing on loop five times at 2 WPM. Don't do anything yet, though, just get used to the signals."
    if (key.style.backgroundColor == "red") {
        lime();
        for (x of Array(5)) {
            document.getElementById('result').value = ""
            await metronome()
        }
    }

    wpm = 5
    document.getElementById('guide').innerHTML += "<br><br>Morse Code is made out of 'dit's and 'dah's. The long signal (or a dah) is three times as long as a short signal (or a dit). Let's say one unit is a length of a dit. Each dit or a dah is separated by one unit, while each letter is separated by three units. Also, each word is separated by seven units. Here's an example usage. Pay attention to the colour of the Key."
    document.getElementById('result').value = ""

    await sleep(5000)

    document.getElementById('guide').innerHTML += "<br>Ready?"

    await sleep(1000)

    document.getElementById('guide').innerHTML += " Go!"

    await sMetronomeExample()

    await metronomeExample()
}