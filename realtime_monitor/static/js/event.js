function viewRequest(target, action, params, callback) {
    var link = '/' + target + '/' + action;
    var i;
    for(i=0; i<params.length; i++) {
        link += '/' + params[i];
    }

    callAJAX(link, callback);
}

var Config = new function() {
    this.close = function() {
        $('.config').remove();
        $('.vertical.container').css({'filter':'blur(0px)'});
    }

    this.getId = function() {
        return $('.config').attr('id').slice(2);
    }

    this.apply = function() {
        id = this.getId();
    }

    this.delete = function() {
        id = this.getId();
        target = id[0];
        id = id.slice(1);
        if(target == 'd') {
            target = 'device';
        }
        else if(target == 'g') {
            target = 'graph';
        }

        viewRequest(target, 'delete', [id], function(result) {
            loadList(target);
            Config.close();
        });
    }

    this.config = function(id) {
        callAJAX('/config/' + id, function(result) {
            $(result).appendTo('body');
            $('.vertical.container').css({'filter':'blur(2px)'});
        });
    }
}

function loadList(target) {
    callAJAX('/load-list/' + target, function(result) {
        if(target == 'device') {
            $('#devices ul').html(result);
        }
        else if(target == 'graph') {
            $('#graphs ol').html(result);
        }
    });
}
