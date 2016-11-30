var Views = new function() {
    this.createGraph = function() {
        callAJAX('/graph/create', function(result) {
            json = JSON.parse(result);
            $('#graphs ol').append(Snippets.graph(json.id, json.name, 'graph off'));
        });
    }

    this.changeGraphName = function(id) {
        var name = prompt('Enter the new name');
        callAJAX('/graph/change-name/' + id.slice(1) + '/' + name, function(result) {
            $('#' + id + ' span.name').text(name);
        });
    }

    this.deleteGraph = function(id) {
        callAJAX('/graph/delete/' + id.slice(1), function(result) {
            $('#' + id).remove();
        });
    }
}
