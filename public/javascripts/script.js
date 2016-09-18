var ready = function() {
  $('.thumb a').click(function() {
    artist_name = $(this).data('artist');
    if(typeof artist_name != 'undefined') {
      $(".lyrics .subtitle").fadeIn(600)
      $(".lyrics .subtitle").html('Training...')
      $('html, body').animate({
        scrollTop: $(".lyrics .subtitle").offset().top
      }, 1000);
      $.post('/lyric', {artist: artist_name}, function(data) {
        lyrics = data.lyrics.replace('*BREAK*', '\n')
        $('.lyrics .subtitle').html(artist_name.replace('_', ' '))
        $('.lyrics .container').html(lyrics)
      })
    }
  })
}

$(ready)
