$( document ).ready(function() {
    $(window).resize(function() {
        $(".tile").height($("#smallest_tile").width());
        $(".carousel").height($("#smallest_tile").width());
        $(".item").height($("#smallest_tile").width());
    });
    $(this).trigger('resize');
});
