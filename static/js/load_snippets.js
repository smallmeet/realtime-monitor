function loadPlots() {
    callAJAX('/plots', function(result) {
        $('#dashboard').html(result);
    });
}

function loadGraphes() {
    callAJAX('/graphes', function(result) {
        $('#graphes').html(result);
    });
}

function loadDevices() {
    callAJAX('/devices', function(result) {
        $('#devices').html(result);
    });
}
