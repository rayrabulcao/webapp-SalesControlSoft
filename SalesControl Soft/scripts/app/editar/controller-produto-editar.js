angular.module('salescontrolapp')
.controller("EditarController", EditarController)

function EditarController($scope, toastr, $state, $http){
    $scope.produto = {};

    var init = function(){
        $scope.id = $state.params.id;
        $scope.buscarProduto($scope.id);
    }
    $scope.buscarProduto = function (id){
        $http.get("http://127.0.0.1:8080/produto/" + id).then(function(retorno){
            $scope.produto = retorno.data[0];
        }).catch(function(erro){
            toastr.error("Ocorreu um erro! Tente novamente.");
            console.error(erro);
        });
    }

    $scope.atualizar = function(produto){
        $http.put("http:127.0.0.1:8080/produto", produto).then(function(retorno){
            toastr.success("Produto atualizado com sucesso!");
        }).catch(function(erro){
            toastr.error("Ocorreu um erro! Tente novamente.");
            console.error(erro);
        });
    }
    init();
}