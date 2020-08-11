$('#regist-submit').click(function(){
    var username = $('#username').val();
    var password = $('#password').val();
    var url = $(this).attr('data-url');

    if (!username ||!password) {
        alert('Missing Necessary Fields!');
        return;
    }

    $.ajax({
        url: url,
        type: 'post',
        data: {
            username: username,
            password: password
        },
        success: function(data){
            alert(data.msg)
        },
        fail: function(e){
            console.log('error:%s', e)
        }
    });

});

$('#login-submit').click(function(){
    var username = $('#username').val();
    var password = $('#password').val();
    var url = $(this).attr('data-url');

    if (!username ||!password) {
        alert('Missing Necessary Fields!');
        return;
    }

    $.ajax({
        url: url,
        type: 'post',
        data: {
            username: username,
            password: password
        },
        success: function(data){
            if (data.code) {
                alert(data.msg)
            } else {
                window.location.href = '/client/video/ex';
            }
        },
        fail: function(e){
            console.log('error:%s', e)
        }
    });
});
