var express = require('express');
var router = express.Router();
var parser = require('../modules/parser.js');

router.get('/parse',function(req,res){
	parser.parse( req.query , function(err,data){
		if(err) console.log("Error:",err);
		res.send(data);
	});

});

router.post('/parse',function(req,res){
	parser.parse( req.body , function(err,data){
		if(err) console.log("Error:",err);
		res.send(data);
	});
});

module.exports = router;
