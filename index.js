var $owl = $('.owl-carousel');

$owl.children().each( function( index ) {
  $(this).attr( 'data-position', index ); // NB: .attr() instead of .data()
});

$owl.owlCarousel({
  // center: true,
  loop: true,
  items: 5,
});

$(document).on('click', '.owl-item>div', function() {
  // see https://owlcarousel2.github.io/OwlCarousel2/docs/api-events.html#to-owl-carousel
  var $speed = 300;  // in ms
  $owl.trigger('to.owl.carousel', [$(this).data( 'position' ), $speed] );
});


// sidebar

const container = document.querySelector('.container');
const button = document.getElementById('icon');
const sidebar = document.querySelector('.sidebar');
const backdrop = document.querySelector('.backdrop');

button.addEventListener('click', function () {
    sidebar.classList.add('show')
    container.classList.add('move');
    backdrop.classList.add('show');
})

backdrop.addEventListener('click', function () {
    sidebar.classList.remove('show')
    container.classList.remove('move');
    backdrop.classList.remove('show');
})