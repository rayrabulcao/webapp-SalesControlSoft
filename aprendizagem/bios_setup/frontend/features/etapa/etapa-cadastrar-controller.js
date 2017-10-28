'use strict';

angular.module('bios-setup').controller('EtapaCadastrarController', function ($scope, $state, $mdToast, EtapaService, $rootScope) {

    $scope.estaSalvando = false;

    var init = function () {
        $scope.etapa = {descricao: undefined, status: true};
    };

    $scope.salvarEtapa = function () {
        $scope.estaSalvando = true;
        EtapaService.create($scope.etapa.descricao, $scope.etapa.status)
            .then(function () {
                $state.transitionTo('home.etapas_listar');
            }, function (error) {
                $mdToast.show({
                    position: 'top left',
                    controller: function ($scope, $mdToast) {
                        $scope.closeToast = function () {
                            $mdToast.hide();
                        }
                    },
                    templateUrl: 'templates/toast-template-etapa.html'
                });
                if (error.status === 403) {
                }
                $scope.estaSalvando = false;
            });
    };

    init();
});
