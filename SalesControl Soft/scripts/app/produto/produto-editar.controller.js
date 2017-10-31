angular.module("teste").controller("ProdutoEditarCtrl", ProdutoEditarCtrl);

function ProdutoEditarCtrl($scope, toastr, ProdutoService, $state){
    var vm = this;
    $scope.produto = {};
    $scope.id = 0;

    function buscarProduto(id){
        ProdutoService.buscarPorId(id).then(function(retorno){
            $scope.produto = retorno.data[0];
        }).catch(function(erro){
            toastr.error("Ocorreu um erro! Tente novamente.");
            console.error(erro);
        });
    }

    function init(){
        // Pegar o ID da URL
        $scope.id = $state.params.id;
        // Buscar o produto para edição
        buscarProduto($scope.id);
    }

    vm.salvar = function(){
        ProdutoService.atualizar($scope.id, $scope.produto).then(function(retorno){
            toastr.success("Produto atualizado com sucesso!");
        }).catch(function(erro){
            toastr.error("Ocorreu um erro! Tente novamente.");
            console.error(erro);
        });
    }

    init();
}