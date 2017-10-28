'use strict';

angular.module('bios-setup').controller('UsuariosListarController', function ($scope, $mdDialog, $state, $mdSidenav, $http) {

    var init = function () {
        $http.get('/bios-setup-api/usuarios').then(function (response) {
            $scope.usuarios = response.data;
        });
    };

    $scope.query = {
        limit: 5,
        page: 1
    };

    $scope.openLeftMenu = function () {
        $mdSidenav('navigation-drawer').toggle();
    };

    $scope.confirmarRemocaoDoUsuario = function (idDoUsuario) {
        $mdDialog
            .show({
                controller: function ($scope) {

                    $scope.confirmar = function () {
                        $mdDialog.hide();
                    };
                    $scope.cancelar = function () {
                        $mdDialog.cancel();
                    };
                },
                templateUrl: 'templates/dialog-delete.html',
                parent: angular.element(document.body),
                clickOutsideToClose: false
            })
            .then(function () {
                $http.delete('/bios-setup-api/usuario/' + idDoUsuario).then(function (response) {
                    init();
                });
            }, function () {
                console.log('cancelou');
            });
    }

init();
});
