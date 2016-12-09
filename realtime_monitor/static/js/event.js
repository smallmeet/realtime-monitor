var Config = new function() {
    this.open = function(id) {
        callAJAX('/config/' + id, function(result) {
            $('body').append(result);
            Config.selectUpdate();
            $('select').change(function() {
                Config.selectUpdate();
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
            switch($('select').val()) {
                case 'duration':
                    content = {'duration': $('input[name=duration]').val(), 'start': 'NULL', 'finish': 'NULL', 'data-count': 'NULL'};
                    break;
                case 'start-and-finish':
                    content = {'duration': 'NULL', 'start': $('input[name=start]').val(), 'finish': $('input[name=finish]').val(), 'data-count': 'NULL'};
                    break;
                case 'data-count':
                    content = {'duration': 'NULL', 'start': 'NULL', 'finish': 'NULL', 'data-count': $('input[name=data-count]').val()};
                    break;
                default:
                    content = {'duration': 'NULL', 'start': 'NULL', 'finish': 'NULL', 'data-count': 'NULL'};
                    break;
            }

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

    this.selectUpdate = function() {
        $('.form div:nth-child(4)').children().css('display', 'none');
        switch($('select').val()) {
            case 'duration':
                $('.form div:nth-child(4) label:nth-child(1)').css('display', 'block');
                break;
            case 'start-and-finish':
                $('.form div:nth-child(4) label:nth-child(2)').css('display', 'block');
                $('.form div:nth-child(4) label:nth-child(3)').css('display', 'block');
                break;
            case 'data-count':
                $('.form div:nth-child(4) label:nth-child(4)').css('display', 'block');
                break;
            default:
                break;
        }
    }

    this.reopen = function() {
        var id = $('.config h3').text()[0].toLowerCase() + $('.config .id').text().slice(1);
        this.apply(id);
        this.close();
        this.open(id);
    }

    this.createLabel = function(deviceId) {
        callAJAX('/label/create/' + deviceId, function(result) {
            Config.reopen();
        });
    }

    this.deleteLabel = function(id) {
        callAJAX('/label/delete/' + id, function(result) {
            Config.reopen();
        });
    }

    this.attachLabel = function(graphId) {
        id = prompt('Label ID', '');
        callAJAX('/graph/attach/' + graphId + '/' + id, function(result) {
            Config.reopen();
        });
    }

    this.detachLabel = function(graphId, labelId) {
        callAJAX('/graph/detach/' + graphId + '/' + labelId, function(result) {
            Config.reopen();
        });
    }

    this.renameLabel = function(id) {
        name = prompt('Name', '');
        callAJAX('/label/change-name/' + id + '/' + name, function(result) {
            Config.reopen();
        })
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
