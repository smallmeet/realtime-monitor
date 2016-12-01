callAJAX('/data/get', function(result) {
    graphList.initList(JSON.parse(result));
});

setInterval(function() {
    var i;
    callAJAX('/data/get', function(result) {
        graphList.updateList(JSON.parse(result));
    });
    keys = graphList.getKeys();
    for(i=0; i<keys.length; i++) {
        graphList.getGraph(keys[i]).draw();
    }
}, 1000);
