graphList = new function() {
    this._graphes = {};

    this.getCSSPath = function() {
        return '/static/css/plot/';
    }

    this.getJSPath = function() {
        return '/static/js/plot/'
    }

    this.getKeys = function() {
        return Object.keys(this._graphes);
    }

    this.getGraph = function(graphId) {
        return this._graphes[graphId];
    }

    this.initList = function(json) {
        keys = Object.keys(json);
        for(i=0; i<keys.length; i++) {
            this._graphes['g'+keys[i]] = new Graph(keys[i], json[keys[i]]);
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
