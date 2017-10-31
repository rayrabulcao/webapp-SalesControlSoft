angular.module("teste").controller("DetalharCtrl", DetalharCtrl);

function DetalharCtrl($scope, toastr, ProdutoService, $state){
    var vm = this;
    $scope.produto = {};
    $scope.id = 0;

    vm.init = function (){
        // Receber o ID da URL
        $scope.id = $state.params.id;
        // Chama método para buscar o produto
        vm.buscarProduto($scope.id);
    }

    // Busca o produto na API
    vm.buscarProduto = function(id){
        ProdutoService.buscarPorId(id).then(function(retorno){
            $scope.produto = retorno.data[0];
        }).catch(function(erro){
            toastr.error("Ocorreu um erro! Tente novamente.");
        });
    }

    vm.init();
}