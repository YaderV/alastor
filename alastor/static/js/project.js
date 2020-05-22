/* Project specific Javascript goes here. */
jQuery(document).ready(function($) {
  var menu = $('#general-nav .dropdown');
  var logo = $('#logo-small');
  $(document).scroll(function() {
    if ($(this).scrollTop() > 195) {
      $(menu).removeClass('d-none');
      // $(logo).removeClass('d-none');
    }
    else {
      $(menu).addClass('d-none');
      // $(logo).addClass('d-none');
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
