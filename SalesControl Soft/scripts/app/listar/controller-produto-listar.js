angular.module('salescontrolapp')
    .controller("ListarController", ListarController)

function ListarController($scope, toastr, $state, $http){
    $scope.produto= {};
    $scope.id = 0;
    
    var init = function(){
        $scope.consultar();
    }

    $scope.editar = function (id){
        $state.go("editar", {id: id});
    }

    $scope.visualizar = function (id){
        $state.go("detalhar", {id: id});
    }
    $scope.excluir = function (id){
        $http.delete("http://127.0.0.1:8080/produto/" + id).then(function (retorno){
            toastr.success("Produto excluído com sucesso");
            consultar();
        }).catch(function(erro){
            toastr.error("Ocorreu um erro. Tente novamente");
            console.error(erro);
        });
    }
    $scope.consultar = function (){
        $http.get("http://127.0.0.1:8080/produto").then(function(retorno){
            $scope.produtos = retorno.data;
        }).catch(function(erro){
            alert("Erro! Tente novamente");
            console.error(erro);
        });
    }
    init();
}
