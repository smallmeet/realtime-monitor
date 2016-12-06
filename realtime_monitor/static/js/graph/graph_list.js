graphList = new function() {
    this._graphs = {};

    this.getKeys = function() {
        return Object.keys(this._graphs);
    }

    this.getGraph = function(graphId) {
        return this._graphs[graphId];
    }

    this.initList = function(json) {
        keys = Object.keys(json);
        for(i=0; i<keys.length; i++) {
            this._graphs['g'+keys[i]] = new Graph(keys[i], json[keys[i]]);
            this.getGraph('g'+keys[i]).loadCSS();
            this.getGraph('g'+keys[i]).loadJS();
        }
    }

    this.updateList = function(json) {
        keys = Object.keys(json);
        for(i=0; i<keys.length; i++) {
            this.getGraph('g' + keys[i]).update(json[keys[i]]);
        }
    }
}
