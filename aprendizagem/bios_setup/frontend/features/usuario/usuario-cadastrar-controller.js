'use strict';

angular.module('bios-setup').controller('UsuarioCadastrarController', function ($scope, $state, $mdToast, $http,$timeout) {

    $scope.estaSalvando = false;
    $scope.desabilitar_campo_login = false;
    $scope.usuario = {nome: undefined, login: undefined, password: undefined, admin: false};

    var init = function () {
        $timeout(function(){
            document.querySelector('#cadastro_login').value = '';
            document.querySelector('#cadastro_senha').value = '';
        },400);

        $scope.$watch('usuario.login', function(){
            $scope.usuario.login = $scope.usuario.login?$scope.usuario.login.replace('/',''):'';
        });
    };

    $scope.verificarLoginExistente = function (podeSalvar) {
        if ($scope.usuario.login) {
            $http.get('/bios-setup-api/usuario/verificar_existente/' + $scope.usuario.login)
                .then(function (response) {
                    $scope.existLogin = response.data;
                    if ($scope.existLogin.length > 0) {
                        $mdToast.show({
                            position: 'top left',
                            controller: function ($scope, $mdToast) {
                                $scope.closeToast = function () {
                                    $mdToast.hide();
                                }
                            },
                            templateUrl: 'templates/toast-template-usuario-login-ja-existe.html'
                        });
                    }
                    else {
                        podeSalvar();
                    }
                });
        }
    };

    $scope.salvarUsuario = function () {

        $scope.verificarLoginExistente(
            function podeSalvar() {
                $http.post('/bios-setup-api/usuarios/', {
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
                });
            }
        );
    };

    init();
});
