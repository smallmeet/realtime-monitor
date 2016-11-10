graphList = new function() {
    this._graphes = {};
    this._cssPath = '/static/css/plot/';
    this._jsPath = '/static/js/plot/';

    this.update = function() {
        callAJAX('/json', function(result) {
            graphList.JSONtoGraphList(JSON.parse(result));
        });
    }

    this.getList = function() {
        return this._graphes;
    }

    this.getKeys = function() {
        return Object.keys(this._graphes);
    }

    this.getGraph = function(graphId) {
        return this._graphes[graphId];
    }

    this.JSONtoGraphList = function(result) {
        keys = Object.keys(result);
        for(i=0; i<keys.length; i++) {
            this._graphes[keys[i]] = new Graph(keys[i], result[keys[i]]);
            $.getScript(this._jsPath + keys[i] + '.js');
        }
    }
}
