jQuery(document).ready(function($) { 
    
	/**
	* FitVids - Responsive Videos in posts
	*/
	$("#site-main").fitVids();

    $(function () {

        $('.sf-menu').superfish({
            'speed': 'fast',
            'delay' : 0,
            'animation': {
                'height': 'show'
            }
        });

    });

    $(".site-toggle-anchor").click(function(){
        $("#site-mobile-menu").toggleClass("is-visible");
        $(".site-toggle-label").toggleClass("is-visible");
        $(".site-toggle-icon").toggleClass("is-visible");

    });

    $(".sub-menu-toggle").click(function(){
        $(this).next().toggleClass("is-visible");
        $(this).toggleClass("is-visible");
    });

});