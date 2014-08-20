jQuery(document).ready(function() {
jQuery(".inputform").submit(function( event ) {

        event.preventDefault();

        jQuery('#submit').attr('disabled', 'disabled');

        jQuery.ajax({
                type: "POST",
                url: "/gmtpun/",
                data: $(this).serialize(),
                success: function(post_response) {
                    jQuery('#submit').removeAttr('disabled');
                    jQuery('#results-placeholder').hide().html(post_response).fadeIn(1500);
                    },
                });

        return false;
        });

});
