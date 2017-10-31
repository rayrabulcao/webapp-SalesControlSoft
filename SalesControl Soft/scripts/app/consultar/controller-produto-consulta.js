angular.module('salescontrolapp')
    .controller("ConsultaController", ConsultaController)

function ConsultaController($scope, toastr){

    $scope.produto= {};

var init = function () {
        $scope.produto = {
        nome: '',
        marca: '',
        colecao: '',
        modelo: '',
        codigo: '',
        valor: '',
        quantidade: '',
        tamanho: '',
        descricao: '',
        imagem: ''        
    };
    }

    $scope.consultar = function (id){
        $http.get("http://localhost:8080/produto/" + id).then(function(retorno){
            $scope.produto = retorno.data[0];
        }).catch(function(erro){
            alert.error("Erro! Tente novamente");
            console.error(erro);
        });
    }

    $scope.init(){
        $scope.id = $state.params.id;
        // Buscar o produto para edição
        buscarProduto($scope.id);
    }
}