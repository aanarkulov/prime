'use strict';

var prime = angular.module('prime.clinic', ['ui.calendar','ngRoute', 'angularMoment']).config(['$locationProvider','$interpolateProvider', '$routeProvider', function($locationProvider, $interpolateProvider, $routeProvider){
    // $locationProvider.html5Mode(true);
    $interpolateProvider.startSymbol('<%');
    $interpolateProvider.endSymbol('%>');
}]);