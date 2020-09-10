$(document).ready(function () {
    $('#sum').click(function () {
        var a = $('#a').val();
        var b = $('#b').val();

        $.get('/app/add/',{'a':a, 'b':b}, function (ret) {
            $('#result').html(ret)
        })

    })
})