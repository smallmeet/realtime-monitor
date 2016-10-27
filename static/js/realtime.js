var client = new XMLHttpRequest();
client.open('GET', '/json');
client.onreadystatechange = function() {
    graphList.updateData(client.responseText);
    keys = Object.keys(graphList._graphes);
    for(i=0; i<keys.length; i++) {
        $.getScript('/static/js/graph/plot/' + keys[i] + '.js')
    }
}
client.send();

setInterval(function() {
    graphList.update();
    keys = Object.keys(graphList._graphes);
    for(i=0; i<keys.length; i++) {
        graphList.getGraph(keys[i]).drawGraph();
    }
}, 1000);
