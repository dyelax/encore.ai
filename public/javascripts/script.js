var ready = function() {
  $('.thumb a').click(function() {
    artist_name = $(this).data('artist');
    $.post('/lyric', {artist: artist_name}, function(data) {
      lyrics = data.lyrics
      console.log(lyrics)
      $('.lyrics-container').html(lyrics)
    })
  })
}

$(ready)