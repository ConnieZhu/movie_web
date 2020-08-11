$('#comment-submit').click(function(){
    var content = $('#comment-content').val();
    var videoId = $(this).attr('data-video-id');
    var userId = $(this).attr('data-user-id');
    var url = $(this).attr('data-url');
//    var ajax-comment-show = $('#ajax-comment-show');

    if (!content) {
        alert('Reviews cannot be empty!');
        return;
    };

    $.ajax({
        url: url,
        data: {
            content: content,
            videoId: videoId,
            userId: userId
        },
        type: 'post',
        success: function(data){
            console.log(data)
        },
        fail: function(e){
            console.log(e);
        }
    })
});