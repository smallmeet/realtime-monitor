function Graph(id, data) {
    this._graphId = 'g' + id;
    this._plotId = 'p' + id;
    this._cssId = 'c' + id;
    this._data = data;
}

Graph.prototype.getGraphId = function() {
    return this._graphId;
}

Graph.prototype.getPlotId = function() {
    return this._plotId;
}

Graph.prototype.getCSSId = function() {
    return this._cssId;
}

Graph.prototype.getData = function() {
    return this._data;
}

Graph.prototype.loadCSS = function() {
    $('<link>',  {
        rel: 'stylesheet',
        type: 'text/css',
        href: '/static/css/plot/' + this.getGraphId() + '.css',
        id: this.getCSSId()
    }).appendTo('head');
}

Graph.prototype.loadJS = function() {
    $.getScript('/static/js/plot/' + this.getGraphId() + '.js');
}

Graph.prototype.draw = function() {
    console.log("There's no proper function for " + this._graphId);
}

Graph.prototype.update = function(data) {
    this._data = data;
}
