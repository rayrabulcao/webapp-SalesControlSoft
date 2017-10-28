'use strict';

angular.module('bios-setup').controller('EtapasListarController', function ($scope, $mdDialog, $state, $mdSidenav, EtapaService, $rootScope) {

    var vm = this;
    vm.statesActual = $state;
    var url = '';

    var init = function () {
        EtapaService.getAll().then(function (response) {
            $scope.etapas = response;
        });
    };

    $scope.query = {
        limit: 5,
        page: 1
    };

    $scope.openLeftMenu = function () {
        $mdSidenav('navigation-drawer').toggle();
    };

    $scope.confirmarRemocaoDaEtapa = function (idDaEtapa) {
        EtapaService.get(idDaEtapa).then(function (response) {
            var etapa = response;

            if (etapa.existeInstrucao) {
                url = 'templates/dialog-alert.html';
            } else {
                url = 'templates/dialog-delete.html';
            }

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
                    templateUrl: url,
                    parent: angular.element(document.body),
                    clickOutsideToClose: false
                })
                .then(function () {
                    EtapaService.delete(idDaEtapa).then(function () {
                        init();
                    });
                }, function () {
                });
        });
    };

    init();
});
