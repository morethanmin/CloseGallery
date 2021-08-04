$(function () {
  let lastScroll = 0

  $('#base-submenu').hide()
  $('.base-submenu-content').hide()

  $('#base-nav, #base-submenu').hover(
    function () {
      console.log('!!!')
      $('#base-submenu').show()
      $('.base-submenu-content').show()
    },
    function () {
      $('#base-submenu').hide()
      $('.base-submenu-content').hide()
    }
  )
  $(window).scroll(function (event) {
    let st = $(this).scrollTop()
    if (st > lastScroll && st > 60) {
      $('#base-header').hide()
    } else {
      $('#base-header').show()
    }
    lastScroll = st
  })
})
