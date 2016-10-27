function Graph(id, data) {
    this._id = id;
    this._order = data.order;
    this._data = data.devices;
}

Graph.prototype.getId = function() {
    return this._id;
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
