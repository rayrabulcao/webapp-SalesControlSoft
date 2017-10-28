'use strict';

angular.module('bios-setup').controller('UsuarioAlterarController', function ($scope, $state, $mdToast, $http) {
    var init = function () {
        var id = $state.params.id;
        $http.get('/bios-setup-api/usuario/' + id).then(function (response) {
            $scope.usuario = response.data;
        }).catch(function (response) {
            $state.transitionTo('home.usuarios_listar');
        });

        if ($state.current.name === 'home.usuario_alterar') {
            $scope.desabilitar_campo_login = true;
            $scope.pode_salvar_user = true;
        }
    };

    $scope.salvarUsuario = function () {
        $scope.estaSalvando = true;
        $http.put('/bios-setup-api/usuario/' + $state.params.id, {
            nome: $scope.usuario.nome,
            login: $scope.usuario.login,
            password: $scope.usuario.password,
            admin: $scope.usuario.admin
        }).then(function (response) {
            $state.transitionTo('home.usuarios_listar');
        }, function (error) {
            $mdToast.show({
                position: 'top left',
                controller: function ($scope, $mdToast) {
                    $scope.closeToast = function () {
                        $mdToast.hide();
                    }
                },
                templateUrl: 'templates/toast-template-usuario.html'
            });
            if (error.status === 403) {

            }
            $scope.estaSalvando = false;
        });
    };

    init();
});
