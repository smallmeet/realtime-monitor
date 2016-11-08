function loadPlots() {
    callAJAX('/plots').done(function(result) {
        $('#dashboard').html(result);
    });
}
