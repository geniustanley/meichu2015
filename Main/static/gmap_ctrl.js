var gmapApp = angular.module('gmapApp', [])
    .config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('{$');
        $interpolateProvider.endSymbol('$}');
    });
gmapApp.controller('GMapCtrl', function($scope, $http) {
    $scope.ready = false;
    $scope.timeSlot = [{
        'id': 0,
	'start': 0,
	'end': 6
    }, {
        'id': 1,
	'start': 7,
	'end': 12
    }, {
        'id': 2,
	'start': 13,
	'end': 18
    }, {
        'id': 3,
	'start': 19,
	'end': 24
    }, {
    	'id': 4,
	'start': 0,
	'end': 24
    }];
    $http.get("/detail/" + reportId)
        .success(function(response) {
		$('.progress').hide();
		$scope.data = response.result;
		var s = $scope.timeSlot[0].start;
		var e = $scope.timeSlot[0].end;
		showMarkers(filter(s, e, $scope.data));
		$scope.timeSelected = 0;
		$scope.ready = true;
	});
    $scope.timeSelected = 0;
    $scope.switchMarkers = function(which) {
    	if ($scope.ready == false)
	    return;
        clearMarkers();
	var s = $scope.timeSlot[which].start;
	var e = $scope.timeSlot[which].end;
        showMarkers(filter(s, e, $scope.data));
        $scope.timeSelected = which;
    };
});

function filter(start, end, data) {
	var result = [];
	for (var i = 0; i < data.length; i++) {
		var date = new Date(data[i].time);
		if (date.getHours() == 0 && date.getMinutes() == 0)
		    continue;
		if (date.getHours() >= start && date.getHours() <= end)
			result.push(new google.maps.Marker({
			    position: {'lat': parseFloat(data[i].latitude), 'lng': parseFloat(data[i].longitude)},
			}));
	}
	return result;
}
