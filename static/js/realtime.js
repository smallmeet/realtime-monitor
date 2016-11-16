callAJAX('/json', function(result) {
    graphList.initList(JSON.parse(result));
});

setInterval(function() {
    callAJAX('/json', function(result) {
        graphList.updateList(JSON.parse(result));
    });
    keys = graphList.getKeys();
    for(i=0; i<keys.length; i++) {
        graphList.getGraph(keys[i]).drawGraph();
    }
}, 1000);
