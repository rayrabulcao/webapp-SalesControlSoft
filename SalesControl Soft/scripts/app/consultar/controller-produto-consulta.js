angular.module('salescontrolapp')
    .controller("ConsultaController", ConsultaController)

function ConsultaController($scope, toastr, $state, $http){

    $scope.produto= {};
    $scope.id = 0;

    $scope.init = function (){
        $scope.id = $state.params.id;
        $scope.consultar($scope.id);
    }

     function init(){
        $scope.produto = [];
        $scope.consultar();
    }

    $scope.editar = function (id){
        $state.go("produtoEditar", {id: id});
    }

    $scope.excluir = function (id){
        $http.delete("http://127.0.0.1:8080/#!/" + id).then(function (retorno){
            toastr.success("Produto excluído com sucesso");
            consultar();
        }).catch(function(erro){
            toastr.error("Ocorreu um erro. Tente novamente");
            console.error(erro);
        });
    }

    $scope.consultar = function (id){
        $http.get("http://127.0.0.1:8080/#!/").then(function(retorno){
            $scope.produto = retorno.data;
        }).catch(function(erro){
            alert("Erro! Tente novamente");
            console.error(erro);
        });
    }


    init();
}
