jQuery(function($) {'use strict',

		
 

		$('.gal_list').slick({
      slidesToShow: 5,
      slidesToScroll: 1,
      infinite: true,
			arrows:true,
      speed: 500,
      autoplay: true,
      autoplaySpeed: 2000,
			responsive: [
      {
        breakpoint: 1224,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }]
    });
		$('.res_list').slick({
      slidesToShow: 4,
      slidesToScroll: 1,
      infinite: true,
			arrows:true,
      speed: 500,
      autoplay: true,
      autoplaySpeed: 2000,
			responsive: [
      {
        breakpoint: 1224,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint: 769,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }]
    });
		$('.vid_list').slick({
      slidesToShow: 4,
      slidesToScroll: 1,
      infinite: true,
			arrows:true,
      speed: 500,
      autoplay: true,
      autoplaySpeed: 2000,
			responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }]
    });
		$('.par_list').slick({
      slidesToShow: 4,
      slidesToScroll: 1,
      infinite: true,
			arrows:true,
      speed: 500,
      autoplay: true,
      autoplaySpeed: 2000,
			responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: true,
          dots: true
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }]
    });
		$('.win_list').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      infinite: true,
			arrows:false,
      speed: 500,
      autoplay: true,
      autoplaySpeed: 2000,
			
    });
		$('footer button.up').click(
			function (e) {
				$('html, body').animate({scrollTop: '0px'}, 800);
			}
		);									
		$('.navbar-toggle').click(function(){
			
			$('body').toggleClass('no-scroll');							
		});

    $('.widget a.dropdown-toggle').click(function(){
			 $(this).next('.dropdown-menu').toggleClass('uopen');
			 $(this).toggleClass('focusme');
   	});   
		if ($(window).width()<600){
			$('.slider .info .container .row').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      infinite: true,
			arrows:false,
      speed: 500,
      autoplay: true,
      autoplaySpeed: 2000,
			
    });
		}								
});
var 	uhe 	= 1,
	lng 	= 'ru',
	has 	= 0,
	imgs  = 1,
	bg  = 1,
	hwidth  = 960,
	bgs 	= ['1','2','3'],
	fonts  = ['20','22','24'];
$(document).ready(function(){uhpv(has)});