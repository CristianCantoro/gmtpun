jQuery(document).ready(function() {
jQuery(".inputform").submit(function() {

        jQuery('#submit').attr('disabled', 'disabled');

        jQuery.ajax({
                type: "POST",
                url: "/",
                data: $(this).serialize(),
                success: function(post_response) {
                    jQuery('#submit').removeAttr('disabled');
                    jQuery('#results-placeholder').hide().html(post_response).fadeIn(1500);
                    },
                });

        return false;
        });

});
