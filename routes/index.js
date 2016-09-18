var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/lyric', function(req, res, next) {
  artist = 'kanye_west'
  var exec = require('child_process').exec;
  var cmd = 'python code/runner.py -l save/models/kanye_west/model.ckpt -a kanye_west -t'

  exec(cmd, function(error, stdout, stderr) {
    raw_response = stdout.trim().split('\n')
    lyrics = raw_response[raw_response.length - 1]
    res.setHeader('Content-Type', 'application/json');
    res.send(JSON.stringify({lyrics: lyrics}));
  });
});

module.exports = router;
