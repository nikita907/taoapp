$(function(){

    $("#typing").typed({
        strings: [" В Африке гориллы.", " В Африке большие.", " Злые крокодилы."],
        typeSpeed: 70,
        backDelay: 1500,
        startDelay: 2500,
        loop: true,
        loopCount: 2,
        contentType: 'html',
    });

});
if ($('.text-slider').length == 1) {
    var typed_strings = $('.text-slider-items').text();
    var typed = new Typed('.text-slider', {
        strings: typed_strings.split(','),
        typeSpeed: 80,
        loop: true,
        backDelay: 1100,
        backSpeed: 30
    });
}