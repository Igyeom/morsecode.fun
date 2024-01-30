document.getElementById('ranked').hidden = true;

function ranked() {
    document.getElementById('ranked').hidden = false;
    $.post({
        type: "POST",
        url: "../ranked",
        data: null,
        success: function(data){
            if (data != "500") {
                console.log('Success!');
                console.log(data)
                location.href = "../matches/" + data.replace("id","")
            } else {
                console.log('Something went wrong!');
            }
        },
      });
}

setInterval(function() {
    $.post({
        type: "POST",
        url: "../queue",
        data: null,
        success: function(data){
            document.getElementById('joinRanked').innerHTML = "Enter A Ranked Match (Current Queued: " + data + ")"
        },
      });
}, 1000);