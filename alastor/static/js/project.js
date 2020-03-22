/* Project specific Javascript goes here. */
jQuery(document).ready(function($) {
  var menu = $('#general-nav .dropdown');
  $(document).scroll(function() {
    if ($(this).scrollTop() > 195) {
      $(menu).removeClass('d-none');
    }
    else {
      $(menu).addClass('d-none');
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
