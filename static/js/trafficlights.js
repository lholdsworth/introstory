$(document).ready(function() {

	$('#recommend').click(function(){
		console.log("recommend");
		var userid;
		userid = $(this).attr("data-userid");
		$.get('/profiles/recommend/', {user_id: userid}, function(data){			
			$('.recommend').html('You recommend this');
			$('.indifferent').html('<a href="#" id="indifferent" data-userid="{{ user.id }}">I am indifferent to this</a>');
			$('.donotrecommend').html('<a href="#" id="donotrecommend" data-userid="{{ user.id }}">I do not recommend this</a>');
		});
	});


	$('#indifferent').click(function(){
		console.log("indifferent");
		var userid;
		userid = $(this).attr("data-userid");
		$.get('/profiles/indifferent/', {user_id: userid}, function(data){
			$('.recommend').html('<a href="#" id="recommend" data-userid="{{ user.id }}">I recommend this</a>');
			$('.indifferent').html('You are indifferent to this');
			$('.donotrecommend').html('<a href="#" id="donotrecommend" data-userid="{{ user.id }}">I do not recommend this</a>');
		});
	});


	$('#donotrecommend').click(function(){
		console.log("c: donotrecommend");
		var userid;
		userid = $(this).attr("data-userid");
		$.get('/profiles/donotrecommend/', {user_id: userid}, function(data){
			$('.recommend').html('<a href="#" id="recommend" data-userid="{{ user.id }}">I recommend this</a>');
			$('.indifferent').html('<a href="#" id="indifferent" data-userid="{{ user.id }}">I am indifferent to this</a>');
			$('.donotrecommend').html('You do not recommend this');
		});
	});

});