graphList = new function() {
    this._graphes = {};

    this.update = function() {
        $(document).ready(function() {
            $.ajax({
                type: 'GET',
                url: '/json',
                success: function(result) {
                    graphList._graphes = {};
                    result = JSON.parse(result);
                    keys = Object.keys(result);
                    for(i=0; i<keys.length; i++) {
                        graphList._graphes[keys[i]] = new Graph(keys[i], result[keys[i]]);
                    }
                },
            });
        });
    }
}
