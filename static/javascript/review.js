$(function () {
  let imgs = $('#rw-img')
  let len = imgs.length,
    counter = 0
  ;[].forEach.call(imgs, function (img) {
    if (img.complete) incrementCounter()
    else img.addEventListener('load', incrementCounter, false)
  })
  function incrementCounter() {
    counter++
    if (counter === len) {
      $('#rw-box').css('opacity', '1')
    }
  }
})
