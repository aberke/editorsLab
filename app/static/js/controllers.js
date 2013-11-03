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

		$('.goTo-article-listen').on(clickEventName, function(event) {
			console.log(event);
			goTo('/article-listen');
		});
	}
	init();
};

function MainCntl($scope, $location, $timeout, APIService){

	$scope.articleRecordingUrl = "http://api.twilio.com/2010-04-01/Accounts/ACe5b88e1903b04f5735be5341582223cb/Recordings/RE3fbd0653f499d45107da3c76506b5f2e";

	$scope.callStatus;

	$scope.showCallInfo = false;
	$scope.showHangupButton = false;


	var recordComment = function() {
		if ($scope.currentCaller) {
			return alert('Call with ' + $scope.currentCaller.firstname + ' ' + $scope.currentCaller.lastname + 'already in progress. You must hang up before you can start a new call.');
		}
		if ($scope.blogcastInfo.twilioIntroRecordingUrl && (!confirm('Recording a new introduction will delete the previously stored introduction.  Are you sure you want to do that?'))){
			return false;
		}
		$scope.showCallInfo = true;
		$scope.showHangupButton = true;
		
		Twilio.Device.connect({
            CallerId:'+15162092653'
        });
	}

	/* using jquery event listener instead of ng-click to avoid nested $apply() calls */
	$('#hangup-button').on('click', function(){ Twilio.Device.disconnectAll(); });
	
	var setupSoftPhone = function(){

		console.log('setupSoftPhone first test:');
		APIService.test(function() {
			console.log('test callback');
		});

		$scope.callStatus = 'Disconnected';
		
		APIService.getSoftphoneToken(function(token){
            Twilio.Device.setup(token);

		   $("#record-audio").on("touchend", function() {
		        console.log('touchend');
		    });
		   console.log('hi');


		   $("#record-audio").on(clickEventName, function() {
		   		console.log('touchstart');
		        $('#test').css('color', 'blue');  
		        Twilio.Device.connect();
		    });
		    $("#hangup").on(clickEventName, function() {  
		        Twilio.Device.disconnectAll();
		    });
		 
		    Twilio.Device.ready(function (device) {
		        $('#status').text('Ready to start recording');
		    });
		 
		    Twilio.Device.offline(function (device) {
		        $('#status').text('Offline');
		    });
		 
		    Twilio.Device.error(function (error) {
		        $('#status').text(error);
		    });
		 
		    Twilio.Device.connect(function (conn) {
		        connection=conn;
		        $('#status').text("On Air");
		        $('#status').css('color', 'red');
		        toggleCallStatus();
		    });
		 
		    Twilio.Device.disconnect(function (conn) {
		        $('#status').html('Recording ended<br/><a href="show_recordings.php">view recording list</a>');
		        $('#status').css('color', 'black');
		        toggleCallStatus();
		    });
		     
		    function toggleCallStatus(){
		        $('#record-audio').toggle();
		        $('#hangup').toggle();
		    }
		});		
	};

	var goTo = function(path) {
		console.log('goTo path: ' + path);
		window.location.href = path;
	};

	var clickEventName;
	var init = function(){
		console.log('hi');
		if ('ontouchstart' in document) {
			clickEventName = 'touchstart';
		} else {
			clickEventName = 'click';
		}

		$('.goTo-index').on(clickEventName, function(event) {
			goTo('/');
		});

		setupSoftPhone();
	}
	console.log('about to call init');
	init();
}