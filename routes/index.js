var express = require('express');
var router = express.Router();
var parser = require('../modules/parser.js');

/* GET home page. */
router.get('/', function(req, res) {
  res.send('done');
});

router.get('/parse',function(req,res){
	parser.parse( req.query , function(err,data){
		res.send(data);
	});

});

router.post('/parse',function(req,res){
	parser.parse( req.body , function(err,data){
		res.send(data);
	});
});

module.exports = router;
