App.factory('APIService', function($rootScope, $http, $q){


  var http = function(method, url, data) {
    var deferred = $q.defer();
    $http({
      method: method,
      url: '/api' + url,
      data: (data || {}),
    })
    .success(function(returnedData){
      deferred.resolve(returnedData);
    })
    .error(function(returnedData) {
      console.log('API ERROR: ' + returnedData.error);
      deferred.reject(returnedData);
    });
    return deferred.promise;
  };

  var httpGET = function(url) {
    return http('GET', url, null);
  };
  var httpPOST = function(url, data) {
    return http('POST', url, data);
  };
  var httpPUT = function(url, data) {
    return http('PUT', url, data);
  };
  var httpDELETE = function(url, data) {
    return http('DELETE', url, data);
  };

  return {


    getSoftphoneToken: function(callback) {
      httpGET('/softphone-token').then(function(returnedData) {
        console.log('getSoftPhoneToken returned:');
        console.log(returnedData);
        callback(returnedData);
      });
    },



  }
});