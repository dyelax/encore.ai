var express = require('express');
var router = express.Router();
var SSH = require('simple-ssh')

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/lyric', function(req, res, next) {
  artist = req.body.artist

  var cmd = 'cd /home/mjc/Research/encore.ai/code; python runner.py -l ../save/models/'+artist+'/model.ckpt -a '+artist+' -t'

  var ssh = new SSH({
    host: '138.16.160.16',
    port: 5556,
    user: 'mjc',
    pass: 'L@xin4life'
  });

  ssh.exec(cmd, {
    error: function(err, resp) {
      console.log(error)
    },
    out: function(err, resp) {
      if(err) {
        throw err;
      }
      console.log(resp)
      raw_response = resp.trim().split('\n')
      console.log(raw_response)
      lyrics = raw_response[raw_response.length - 1]
      res.setHeader('Content-Type', 'application/json');
      res.send(JSON.stringify({lyrics: lyrics}));
    }
  }).start();
});

module.exports = router;
