function Graph(id, data) {
    this._graphId = id;
    this._plotId = '#' + id.replace('g', 'p');
    this._order = data.order;
    this._data = data.devices;
}

Graph.prototype.getGraphId = function() {
    return this._graphId;
}

Graph.prototype.getPlotId = function() {
    return this._plotId;
}

Graph.prototype.getOrder = function() {
    return this._order;
}

Graph.prototype.getData = function() {
    return this._data;
}

Graph.prototype.drawGraph = function() {
    console.log("There's no proper function for " + this._id);
}

Graph.prototype.update = function(data) {
    this._order = data.order;
    this._data = data.devices;
}
