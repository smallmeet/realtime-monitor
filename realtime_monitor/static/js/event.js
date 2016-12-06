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
        var id = this.getId();
        var target = id[0];
        id = id.slice(1);

        var name = $('#name').val();

        if(target == 'd') {
            viewRequest('device', 'change-name', [id, name], function(result) {
                loadList('device');
            });
        }
        else if(target == 'g') {
            if($('#duration').is(':checked')) {
                $.post('/graph/set-interval/' + id, {'duration': $('input[name=duration]').val(), 'start': 'NULL', 'finish': 'NULL', 'data-count': 'NULL'});
            }
            else if($('#start-and-finish').is(':checked')) {
                $.post('/graph/set-interval/' + id, {'duration': 'NULL', 'start': $('input[name=start]').val(), 'finish': $('input[name=finish]').val(), 'data-count': 'NULL'});
            }
            else if($('#data-count').is(':checked')) {
                $.post('/graph/set-interval/' + id, {'duration': 'NULL', 'start': 'NULL', 'finish': 'NULL', 'data-count': $('input[name=data-count]').val()});
            }
            else if($('#none').is(':checked')) {
                $.post('/graph/set-interval/' + id, {'duration': 'NULL', 'start': 'NULL', 'finish': 'NULL', 'data-count': 'NULL'});
            }
            viewRequest('graph', 'change-name', [id, name], function(result) {});
            viewRequest('graph', 'order', [id, $('#order').val()], function(result) {
                loadList('graph');
            });

        }
    }

    this.delete = function() {
        var id = this.getId();
        var target = id[0];
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
            var div = $('.form div:last-child');
            $('.form div:last-child').children().css('display', 'none');
            Config.radioUpdate();
            $('.radio').change(function() {
                Config.radioUpdate();
            });
            $('.vertical.container').css({'filter':'blur(2px)'});
        });
    }

    this.radioUpdate = function() {
        $('.form div:last-child').children().css('display', 'none');
        if($('#duration').is(':checked')) {
            $('.form div:last-child label:nth-child(1)').css('display', 'block');
        }
        else if($('#start-and-finish').is(':checked')) {
            $('.form div:last-child label:nth-child(2)').css('display', 'block');
            $('.form div:last-child label:nth-child(3)').css('display', 'block');
        }
        else if($('#data-count').is(':checked')) {
            $('.form div:last-child label:nth-child(4)').css('display', 'block');
        }
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
