/*global angular*/
 "use strict";
  angular.module("salescontrolapp").directive("navbarSales", function () {
     return {
         restrict: "E",
         transclude: true,
         templateUrl: "scripts/app/diretivas/navbar.html",
         controller: ""
     };
 });
