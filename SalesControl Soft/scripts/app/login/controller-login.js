angular.module("salescontrolapp")
.controller("LoginController", LoginController);

function LoginController ($scope, toastr, $state, $http, $rootScope, $window, $document){

    var init = function () {
		$scope.acesso = '';
		//$scope.message = 'Usuário ou Senha inválidos!';
    };

    $scope.loginUser = function (user) {
        var usuarios = [
		{
			username:'admin', password:'12345', admin:true
		},
          	{
			username:'cliente', password:'cliente123', admin:false
		},
          ]
	      angular.forEach(usuarios, function(value, index){
        	if(value.username == user.username && value.password == user.password){
	              delete value.password;
        	      $rootScope.currentUser = value;
        	      $state.go('home');
			}
			if (value.username != user.username && value.password != user.password){
				toastr.error('Usuário e senha Inválidos!');
          	}
	});
	};
    
    init();
}
