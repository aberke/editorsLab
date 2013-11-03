function IndexCntl($scope, $location) {

	$scope.goTo = function(path) {
		console.log('goTo path: ' + path);
		window.location.href = path;
	};
};

function MainCntl($scope, $location, $timeout, APIService){

	$scope.callStatus;

	$scope.showCallInfo = false;
	$scope.showHangupButton = false;


	$scope.recordIntro = function() {
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
		$scope.callStatus = 'Disconnected';
		
		APIService.getSoftphoneToken(function(token){
            Twilio.Device.setup(token);

		   $("#call").click(function() {  
		        Twilio.Device.connect();
		    });
		    $("#hangup").click(function() {  
		        connection.sendDigits("#");
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
		        $('#call').toggle();
		        $('#hangup').toggle();
		    }
		});		
	};

	var init = function(){

		setupSoftPhone();
	}
	init();
}