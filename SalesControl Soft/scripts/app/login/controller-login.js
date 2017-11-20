angular.module("salescontrolapp")
.controller("LoginController", LoginController);

function LoginController ($scope, toastr, $state, $http, $rootScope, $window, $document){
        
    var init = function () {
        $scope.acesso = '';
    };

    $scope.loginUser = function (user) {
        var valor = [];
        valor.push({
            login: user.username,
            senha: user.password
        })

        $http.post('http://127.0.0.1:8080/produto/', valor).then(function (response) {
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
                    $state.go('home');
                }
            }

        });
    };

    init();
}

// $scope.taLogado = false;

// function logar (){
//     $scope.taLogado = true;
// }

// function logOut(){
//     $scope.taLogado = false;
// }