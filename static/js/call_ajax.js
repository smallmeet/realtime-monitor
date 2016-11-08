function callAJAX(page) {
    return $.ajax({
        type:'GET',
        url: page,
    });
}
