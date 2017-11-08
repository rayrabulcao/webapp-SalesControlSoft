angular.module('salescontrolapp')
    .controller("ConsultaController", ConsultaController)

function ConsultaController($scope, toastr, $state, $http){

    $scope.produto= {};
    $scope.id = 0;


/*var init = function () {
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
    }*/
    $scope.init = function (){
        $scope.id = $state.params.id;
        $scope.consultar($scope.id);
    }

    $scope.consultar = function (id){
        $http.get("http://127.0.0.1:8080/produto/" + id).then(function(retorno){
            $scope.produto = retorno.data[0];
        }).catch(function(erro){
            alert("Erro! Tente novamente");
            console.error(erro);
        });
    }

    /*$scope.init(){
        $scope.id = $state.params.id;
        // Buscar o produto para edição
        buscarProduto($scope.id);
    }*/
    $scope.init();
}