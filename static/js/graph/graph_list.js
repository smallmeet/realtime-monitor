graphList = new function() {
    this._graphes = {};

    this.update = function() {
        callAJAX('/json').done(function(result) {
            graphList.updateData(result);
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

    this.updateData = function(result) {
        result = JSON.parse(result);
        keys = Object.keys(result);
        for(i=0; i<keys.length; i++) {
            this._graphes[keys[i]] = new Graph(keys[i], result[keys[i]]);
            $.getScript('/static/js/graph/plot/' + keys[i] + '.js');
        }
    }
}
