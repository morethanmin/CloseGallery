$(function () {
  $('#id-mainweek-extendcard').hide()
  $('#id-mainreview-celebrity').hide()

  $('#id-mainweek-btn').click(function () {
    $('#id-mainweek-extendcard').show()

    if ($('#id-mainweek-btn').text() === '+ 더보기') $('#id-mainweek-btn').text('더 많은 작품 보기')
    else window.location.replace('/painting/')
  })

  $('#id-mainreview-tab-user').click(function () {
    $(this).addClass('id-mainreview-tabs-active')
    $('#id-mainreview-tab-celebrity').removeClass('id-mainreview-tabs-active')
    $('#id-mainreview-user').show()
    $('#id-mainreview-celebrity').hide()
  })
  $('#id-mainreview-tab-celebrity').click(function () {
    $(this).addClass('id-mainreview-tabs-active')
    $('#id-mainreview-tab-user').removeClass('id-mainreview-tabs-active')
    $('#id-mainreview-celebrity').show()
    $('#id-mainreview-user').hide()
  })
})

var swiper = new Swiper('.id-maintheme-slide', {
  slidesPerView: 5,
  spaceBetween: 30,
  loop: true,
  pagination: {
    el: '.id-maintheme-pagination',
    clickable: true,
  },
  navigation: {
    nextEl: '.id-maintheme-button-next',
    prevEl: '.id-maintheme-button-prev',
  },
})

console.log('swiper')
