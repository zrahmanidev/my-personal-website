// set twitter text
function twitter_text(text) {
	text = text.replace(/[A-Za-z]+:\/\/[A-Za-z0-9-_]+\.[A-Za-z0-9-_:%&\?\/.=]+/g, function (m) {
		return '<a href="' + m + '" target="_blank">' + m + '</a>';
	});
	// Usernames
	text = text.replace(/@[A-Za-z0-9_]+/g, function (u) {
		return '<a href="http://twitter.com/#!/' + u.replace(/^@/, '') + '" target="_blank">' + u + '</a>';
	});
	// Hashtags
	text = text.replace(/#[A-Za-z0-9_\-]+/g, function (u) {
		return '<a class="hashtags" href="http://twitter.com/#!/search?q=' + u.replace(/^#/, '%23') + '" target="_blank">' + u + '</a>';
	});
	
	return text;
}

jQuery(document).ready(function(){	
		
	/* Main Menu */
	$('#logo').click( function() {
		$('#main_menu').easytabs('select', '#id_home');
		return false;
	});

	$('#main_menu').easytabs({
		panelContext: $('#main_content'),
		transitionIn: 'slideDown',
		transitionOut: 'slideUp'
	}).bind('easytabs:before', function(e, $clicked, $targetPanel, settings) {
		if (( $targetPanel.get(0).id != 'id_blog' )) {
			var id = $targetPanel.get(0).id;
			theUrl = "index.html";
			$('html').animate({scrollTop:0}, 'slow');
			$('body').append('<div id="BIGLOADER"></div>');
			$.ajax({
				type: "GET",
				url: theUrl,
				data: "pg_id="+id,
				success: function(){
					window.location.href = theUrl+"#"+id;
				}
			});
			return false;
		} 
	}); 
	$('#main_menu li:nth-child(3) a').trigger('click');
	/*Back to index.html#id_blog*/
	$('#main_menu li:nth-child(3) a').on("click",function(){
			id = 'id_blog';
			theUrl = "index.html";
			$('html').animate({scrollTop:0}, 'slow');
			$('body').append('<div id="BIGLOADER"></div>');
			$.ajax({
				type: "GET",
				url: theUrl,
				data: "pg_id="+id,
				success: function(){
					window.location.href = theUrl+"#"+id;
				}
			});
			return false;
	});
	$('html').animate({scrollTop:0}, 'slow');
	
	/* Main Menu Ends*/
	
	//SUBMIT FORM
	jQuery.validator.addMethod(
		"math", 
		function(value, element, params) { 
			if (value==='')
				return false;
			return this.optional(element) || value == params[0] + params[1]; 
		},
		jQuery.format("Please enter the correct value for {0} + {1}")
	);
	$('#post_comment_form').validate({
		rules: {
			author: {
				minlength: 3,
				required: true
			},
			email: {
				required: true,
				email: true
			},
			url: {
				minlength: 3
			},
			comment: {
				minlength: 10,
				required: true
			},
			captcha: {
				math: [3, 4]
			}
		},
		submitHandler: function(form) {
			var a=$('#post_comment_form').serialize();
			$.ajax({
				type: "POST",
				url: "single_comment_process.php",
				data:a,
				complete:function(){
				},
				beforeSend: function() {
				
				},
				success: function(data){
					alert(data);
					$('#post_comment_form').find("input[type=text], textarea").val("");
				},
				error : function() {
				
				}
			});
			return false;
		}
	});
	
	//TWITTER
	$.getJSON('twitter/ajax/getFromTwitter.php',{})
	.done(function( json ) {
		$max_tweet = 5;
		$i = 0;
		$.each(json,function(){
			text = this.text;
			text = twitter_text(text);
			$('<div class="slide">').append('<span class="tweet">'+text+'</span>').appendTo('#twitter_update_list_container');
			$i++;
			if ($i==$max_tweet) return false;
		});
	})
	.fail(function( jqxhr, textStatus, error ) {
		var err = textStatus + ', ' + error;
		console.log( "Request Failed: " + err);
	})
	.always(function() { console.log( "complete" ); });
});