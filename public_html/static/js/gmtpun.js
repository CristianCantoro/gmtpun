$(function() {
    $(".inputform").submit(function( event ) {
        event.preventDefault();

        $('#submit').attr('disabled', 'disabled');


        $.ajax({
                type: "POST",
                url: window.location.href + "/",
                data: $(this).serialize(),
                success: function(post_response) {
                    $('#submit').removeAttr('disabled');
                    $('#results-placeholder').hide().html(post_response).fadeIn(1500);
                    },
                });


        return false;
        });
});
