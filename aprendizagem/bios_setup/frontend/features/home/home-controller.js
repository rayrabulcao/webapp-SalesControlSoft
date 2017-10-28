'use strict';

angular.module('bios-setup').controller('HomeController', function ($scope, $http, $state, $mdToast, $mdDialog, $rootScope) {


    var vm = this;
    vm.statesActual = $state;

    var init = function () {
        $rootScope.currentUser = window.sessionStorage.getItem('usuario');
        $rootScope.isAdmin = window.sessionStorage.getItem('admin');
    };


    $scope.logout = function(user) { 
        window.sessionStorage.removeItem('usuario');
        window.sessionStorage.removeItem('admin');

        $state.go('login');
     }; 

    vm.goTo = function(state){
        $state.go(state);
    }


    vm.isStateCurrent = function (stateArray) {
        try {
            if(stateArray){
                return stateArray.indexOf(vm.statesActual.current.name) > -1;
            } else {
                return false;
            }
        }
        catch (err) {
            return false;
        }
    };



    init();
});