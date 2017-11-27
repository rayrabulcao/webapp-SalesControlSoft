angular.module("salescontrolapp")
.controller("LoginController", LoginController);

function LoginController ($scope, toastr, $state, $http, $rootScope, $window, $document){
        
    var init = function () {
        $scope.acesso = '';
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
			} else if (value.username != user.username && value.password != user.password){
				toastr.error('Usuário e senha Inválidos!'); 
          	}
	});
    };

    //$scope.taLogado = false;

//function logar (){
//     $scope.taLogado = true;
// }

 //function logOut(){
   //  $scope.taLogado = false;
 //}

    init();
}
