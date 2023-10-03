//csrf token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

$(document).ready(function () {
    $(document).on("click", "#myid", function () {
        const offset = $("#"+$(this).val()).offset();
        const offset2 = $("#target").offset();
        var top = offset.top - offset2.top;
        $('#scroll').animate({scrollTop: top},500);
    });
});

//하트 누르기
$(document).ready(function () {
    $(document).on("click", "#Like", function () {
        var pk = $(this).attr('name')
        $.ajax({ // ajax로 서버와 통신
            type: "POST", // 데이터를 전송하는 방법
            url: "/intru/like/", // 통신할 url을 지정
            data: { 'pk': pk ,'csrfmiddlewaretoken': csrftoken}, // 서버로 데이터 전송시 옵션, pk를 넘겨야 어떤 video인지 알 수 있음
            dataType: "json",
            success: function (response) { // 성공  
                $("#count-" + pk).html(response.likes_count + "개"); // 좋아요 개수 변경
            },
            error: function (request, status, error) { // 실패
                alert("로그인이 필요합니다.")
            },
        });
    });
});