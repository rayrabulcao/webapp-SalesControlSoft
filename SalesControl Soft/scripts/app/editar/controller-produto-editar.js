angular.module('salescontrolapp')
.controller("EditarController", EditarController)

function EditarController($scope, toastr, $state, $http){

    $scope.produto = {};
    $scope.id = 0;

    $scope.buscarProduto = function (id){
        $scope.get("http://127.0.0.1:8080/#!/").then(function(retorno){
            $scope.produto = retorno.data[0];
        }).catch(function(erro){
            toastr.error("Ocorreu um erro! Tente novamente.");
            console.error(erro);
        });
    }

    $scope.init = function(){
        // Pegar o ID da URL
        $scope.id = $state.params.id;
        // Buscar o produto para edição
        $scope.buscarProduto($scope.id);
    }

    $scope.salvar = function(){
        $scope.get("http:127.0.0.1:8080//#!/" + $scope.id, $scope.produto).then(function(retorno){
            toastr.success("Produto atualizado com sucesso!");
        }).catch(function(erro){
            toastr.error("Ocorreu um erro! Tente novamente.");
            console.error(erro);
        });
    }

    init();
}