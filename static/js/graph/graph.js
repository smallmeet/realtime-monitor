function Graph(id, data) {
    this._graphId = 'g' + id;
    this._plotId = '#p' + id;
    this._data = data;
}

Graph.prototype.getGraphId = function() {
    return this._graphId;
}

Graph.prototype.getPlotId = function() {
    return this._plotId;
}

Graph.prototype.getData = function() {
    return this._data;
}

Graph.prototype.drawGraph = function() {
    console.log("There's no proper function for " + this._graphId);
}

Graph.prototype.update = function(data) {
    this._data = data;
}
