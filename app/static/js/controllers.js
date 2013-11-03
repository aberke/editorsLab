function IndexCntl($scope, $location) {

	var clickEventName;

	var goTo = function(path) {
		console.log('goTo path: ' + path);
		window.location.href = path;
	};

	var init = function(){
		if ('ontouchstart' in document) {
			clickEventName = 'touchstart';
		} else {
			clickEventName = 'click';
		}
		console.log('clickEventName: ' + clickEventName);

		$('#article-1-listen').on(clickEventName, function(event) {
			goTo('/article-1/listen');
		});
		$('#article-2-listen').on(clickEventName, function(event) {
			goTo('/article-2/listen');
		});
	}
	init();
};

function MainCntl($scope, $location){

	var goTo = function(path) {
		console.log('goTo path: ' + path);
		window.location.href = path;
	};

	var clickEventName;
	var init = function(){
		if ('ontouchstart' in document) {
			clickEventName = 'touchstart';
		} else {
			clickEventName = 'click';
		}

		$('.goTo-index').on(clickEventName, function(event) {
			goTo('/');
		});
	}
	init();
}