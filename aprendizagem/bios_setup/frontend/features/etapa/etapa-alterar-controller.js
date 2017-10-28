'use strict';

angular.module('bios-setup').controller('EtapaAlterarController', function ($scope, $state, $mdToast, EtapaService, $rootScope) {
    var init = function () {
        var id = $state.params.id;
        EtapaService.get(id)
            .then(function (response) {
                $scope.etapa = response;
            }, function () {
                $state.transitionTo('home.etapas_listar');
            });
    };

    $scope.salvarEtapa = function () {
        EtapaService.update($state.params.id, $scope.etapa.descricao, $scope.etapa.status)
            .then(function () {
                    $state.transitionTo('home.etapas_listar');
                },
                function (error) {
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
