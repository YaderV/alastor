/* Project specific Javascript goes here. */
jQuery(document).ready(function($) {
  var menu = $('.navbar-default');
  // var home = $('.nav-secondary ul li:first-child');
  $(document).scroll(function() {
    if ($(this).scrollTop() > 195) {
      $(menu).addClass('menu-top-fixed');
      // $(home).show();
    }
    else {
      $(menu).removeClass('menu-top-fixed');
      // $(home).hide();
    }
  });
  if ($('.version-list').length) {
    $('.version-list').slick({
      infinite: true,
      slidesToShow: 6,
      slidesToScroll: 2
    });
  }
});
