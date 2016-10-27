function Graph(graphId, data) {
    this._graphId = graphId;
    this._order = data.order;
    this._data = data.devices;
}

Graph.prototype.drawGraph = function() {
    console.log("There's no proper function for this graph.");
}

Graph.prototype.update = function(data) {
    this._order = data.order;
    this._data = data.devices;
}
