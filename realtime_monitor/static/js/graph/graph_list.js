graphList = new function() {
    this._graphs = {};

    this.getCSSPath = function() {
        return '/static/css/plot/';
    }

    this.getJSPath = function() {
        return '/static/js/plot/'
    }

    this.getKeys = function() {
        return Object.keys(this._graphs);
    }

    this.getGraph = function(graphId) {
        return this._graphs[graphId];
    }

    this.initList = function(json) {
        keys = Object.keys(json);
        for(i=0; i<keys.length; i++) {
            this.insertGraph(keys[i]);
        }
    }

    this.updateList = function(json) {
        keys = Object.keys(json);
        for(i=0; i<keys.length; i++) {
            this.getGraph('g' + keys[i]).update(json[keys[i]]);
        }
    }

    this.insertGraph = function(id) {
        this._graphs['g'+id] = new Graph(id, {});
        this.getGraph('g'+id).loadCSS();
        this.getGraph('g'+id).loadJS();
    }

    this.removeGraph = function(id) {
        delete this._graphs['g'+id];
        $('#c'+id).remove();
    }
}
