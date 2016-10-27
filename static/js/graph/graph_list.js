graphList = new function() {
    this._graphes = {};

    this.update = function() {
        $(document).ready(function() {
            $.ajax({
                type: 'GET',
                url: '/json',
                success: function(result) {
                    result = JSON.parse(result);
                    keys = Object.keys(result);
                    for(i=0; i<keys.length; i++) {
                        if(keys[i] in graphList._graphes) {
                            graphList._graphes[keys[i]].update(result[keys[i]]);
                        }
                        else {
                            graphList._graphes[keys[i]] = new Graph(keys[i], result[keys[i]]);
                        }
                    }
                },
            });
        });
    }

    this.getGraph = function(graphId) {
        return this._graphes[graphId];
    }
}
