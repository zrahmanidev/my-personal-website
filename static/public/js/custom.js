jQuery(document).ready(function(){
	//slider for photo on home
	$('#photo_slider').cycle({
		fx:'fade',
		pager:  '#photo_slider_nav',

		containerResize: 1,
		pagerAnchorBuilder: function(idx, el) {
			return '<a href="#" title="Photo '+ (idx+1) +'"></a>';
		},
		slideResize: 0,
		width: '100%',
		fit: 1,
		timeout:3000

	});
});