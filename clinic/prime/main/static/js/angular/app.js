'use strict';

var prime = angular.module('prime.clinic', ['ui.calendar','ngRoute', 'angularMoment']).config(['$locationProvider','$interpolateProvider', '$routeProvider', function($locationProvider, $interpolateProvider, $routeProvider){
    $locationProvider.html5Mode({ enabled: true, requireBase: false, rewriteLinks: false });
    $interpolateProvider.startSymbol('<%');
    $interpolateProvider.endSymbol('%>');
}]);

prime.run(function(amMoment) {
    amMoment.changeLocale('ru');
});