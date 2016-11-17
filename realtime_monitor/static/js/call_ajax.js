function callAJAX(page, callback) {
    $.ajax({
        type:'GET',
        url: page,
        success: callback
    });
}
