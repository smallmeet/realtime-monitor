loadPlots();
loadGraphes();

setInterval(function() {
    graphList.update();
    keys = graphList.getKeys();
    for(i=0; i<keys.length; i++) {
        graphList.getGraph(keys[i]).drawGraph();
    }
}, 1000);
