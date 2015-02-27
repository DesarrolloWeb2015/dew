'use strict'

var app = angular.module('bitacoraApp', []);

app.controller('BitacoraCtrl', ['$scope', '$http', function($scope, $http){
    $scope.done;$http.get('http://api.aiocs.es/bitacora/').
        success(function(data, status){
            $scope.done = data.results;
        }
    ).
    error(function(data, status){
        $scope.done = "ERROR";
    });
}]);
