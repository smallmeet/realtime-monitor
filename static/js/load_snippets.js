function loadPlots() {
    callAJAX('/plots').done(function(result) {
        $('#dashboard').html(result);
    });
}

function loadGraphes() {
    callAJAX('/graphes').done(function(result) {
        $('#graphes').html(result);
    });
}
