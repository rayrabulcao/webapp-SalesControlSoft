'use strict';

angular.module('bios-setup').controller('LoginController', function ($scope, $http, $state, $mdToast, $mdDialog, $rootScope, $window, $document) {


    var init = function () {
        $scope.acesso = '';
    };

    $scope.loginUser = function (user) {
        var valor = [];
        valor.push({
            login: user.username,
            senha: user.password
        })

        $http.post('/bios-setup-api/login/', valor).then(function (response) {
            $scope.acesso = response.data;

            if ($scope.acesso == '') {
                $scope.message = 'Usuário ou Senha inválidos!';
            }
            else {
                window.sessionStorage.setItem('usuario', $scope.acesso[0].nome);
                window.sessionStorage.setItem('admin', $scope.acesso[0].admin);
                $rootScope.isAdmin =  window.sessionStorage.getItem('admin')
                if($rootScope.isAdmin === 'true'){
                    $state.go('home');
                }
                else {
                    $state.go('home.config-por-op_listar');
                }
            }

        });
    };

    init();
});