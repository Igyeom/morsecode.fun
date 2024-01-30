let reports = document.getElementById('reports').innerHTML.split(" // ")

reports.splice(0, 1)
reports.splice(0, 1)
reports.splice(0, 1)

nested = []

function ban(target) {
    setTimeout(function(){document.location.href = "https://morsecode.fun/ban/" + target}, 500)
}

for (i of reports) {
    i = i.substring(10).split(" BY ")
    var timestamp = i[0]
    var reporter = i[1].split(" AGAINST ")[0]
    var target = i[1].split(" AGAINST ")[1]

    nested.push([timestamp, reporter, target])
}

for (i of nested) {
    document.querySelector('table').innerHTML += "<tr>Report by " + reporter + " against " + target + " at timestamp: " + timestamp + "<button class='btn btn-warning' onclick='ban(\"" + target + "\");' style='transform: translate(0, -3pt);'>Ban</button><button class='btn btn-danger' style='transform: translate(0, -3pt);'>X</button></tr>"
}