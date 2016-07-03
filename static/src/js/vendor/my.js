/* Author:
B.R. Mullikin
*/
var scrolled;
var lastScrollTop = 0;
var delta = 5;
var navbarHeight = $('.top-header').outerHeight();
// check if email is valid (weak check)
// escape id
function q(x) {
     return x.replace(/(:|\.)/g,'\\$1');
 }

Array.prototype.indexOfBool = function(item) {
    var i = this.length;
    while (i--) {
        if(this[i] === item) {
            return true;
        }
    }
    return false;
};

function hasScrolled() {
    var top = $(this).scrollTop();
    if(Math.abs(lastScrollTop - top) <= delta) {
        return;
    }
    if (top > lastScrollTop && top > navbarHeight) {
        $('.top-header').addClass('is-minimized');
    } else {
        if(top + $(window).height() < $(document).height()) {
            $('.top-header').removeClass('is-minimized');
        }
    }
    lastScrollTop = top;
}
$(function(){
    if (document.hidden == null || !document.hidden) {
        $('html').addClass('page-ready');
    }
    function onFocus(){
        $('html').addClass('page-ready');
    }
    window.onfocus = onFocus;
    $('a.jump, a.footnote-backref, a.footnote-ref, a[href^="#"]:not(.carousel-control), .home a[href^="/#"]').click(function(event) {

        event.preventDefault();

        var the_url = this.href;
        var parts = the_url.split("#");
        var target = q(parts[1]);

        var offset = $("#"+target).offset();
        var top = offset.top;
        $('html, body').animate({scrollTop:top-150}, 500);
    });
    $(".menu-button").click(function(){
        $(this).toggleClass('open');
        $('.menu').toggleClass("closed");
        $('html').toggleClass("no-scrollbar");
    });
    $(window).scroll(function(event) {
        scrolled = true;
    });
    setInterval(function(){
        if(scrolled) {
            hasScrolled();
            scrolled = false;
        }
    }, 250);
});
