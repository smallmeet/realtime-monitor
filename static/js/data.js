data = new function() {
    this._data = {};

    this.update = function() {
        $(document).ready(function() {
            $.ajax({
                type: 'GET',
                url: '/json',
                success: function(result) {
                    data._data = result;
                },
            });
        });
    }
}
