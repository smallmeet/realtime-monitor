var Snippets = new function() {
    this.graph = function(id, graphName, className) {
        var li = document.createElement('li');
        var graphId = document.createElement('span');
        var name = document.createElement('span');
        var ul = document.createElement('ul');
        var deleteButton = document.createElement('button');

        li.setAttribute('class', className);
        li.setAttribute('id', 'g'+id);

        name.setAttribute('class', 'name');
        name.setAttribute('onclick', 'Views.changeGraphName($(this).parent().attr(\'id\'))');
        name.innerHTML = graphName;

        graphId.setAttribute('class', 'graph-id');
        graphId.innerHTML = '#' + id;

        deleteButton.innerHTML = 'Delete';
        deleteButton.setAttribute('onclick', 'Views.deleteGraph($(this).parent().attr(\'id\'))');

        li.appendChild(name);
        li.appendChild(graphId);
        li.appendChild(deleteButton);
        li.appendChild(ul);

        return li;
    }
}
