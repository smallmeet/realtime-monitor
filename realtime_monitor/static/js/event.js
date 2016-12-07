var Config = new function() {
    this.open = function(id) {
        callAJAX('/config/' + id, function(result) {
            $('body').append(result);
            Config.radioUpdate();
            $('.radio').change(function() {
                Config.radioUpdate();
            });
            $('.vertical.container').css({'filter':'blur(2px)'});
        });
    }

    this.close = function() {
        $('.config').remove();
        $('.vertical.container').css({'filter':'blur(0px)'});
    }

    this.apply = function(id) {
        var target = id[0];
        id = id.slice(1);

        var name = $('input[name=name]').val();

        if(target == 'd') {
            callAJAX('/device/change-name/' + id + '/' + name, function(result) {
                loadList('device');
            });
        }
        else if(target == 'g') {
            var content;
            if($('#duration').is(':checked'))
                content = {'duration': $('input[name=duration]').val(), 'start': 'NULL', 'finish': 'NULL', 'data-count': 'NULL'};
            else if($('#start-and-finish').is(':checked'))
                content = {'duration': 'NULL', 'start': $('input[name=start]').val(), 'finish': $('input[name=finish]').val(), 'data-count': 'NULL'};
            else if($('#data-count').is(':checked'))
                content = {'duration': 'NULL', 'start': 'NULL', 'finish': 'NULL', 'data-count': $('input[name=data-count]').val()};
            else if($('#none').is(':checked'))
                content = {'duration': 'NULL', 'start': 'NULL', 'finish': 'NULL', 'data-count': 'NULL'};

            $.post('/graph/set-interval/' + id, content);
            callAJAX('/graph/change-name/' + id + '/' + name, function(result) {});
            callAJAX('/graph/order/' + id + '/' + $('input[name=order]').val(), function(result) {
                loadList('graph');
                loadPlots();
            });
        }
    }

    this.activate = function(id) {
        callAJAX('/graph/toggle/' + id.slice(1), function(result) {
            loadList('graph');
            loadPlots();
            graphList.insertGraph(id.slice(1));
        })
    }

    this.deactivate = function(id) {
        callAJAX('/graph/toggle/' + id.slice(1), function(result) {
            loadList('graph');
            loadPlots();
            graphList.removeGraph(id.slice(1));
        })
    }

    this.delete = function(id) {
        var target = id[0];
        id = id.slice(1);
        if(target == 'd') {
            callAJAX('/device/delete/' + id, function(result) {
                loadList('device');
                Config.close();
            });
        }
        else if(target == 'g') {
            callAJAX('/graph/delete/' + id, function(result) {
                graphList.removeGraph(id);
                loadList('graph');
                loadPlots();
                Config.close();
            });
        }
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

function loadPlots() {
    callAJAX('/load-plots', function(result) {
        $('#dashboard').html(result);
    });
}
