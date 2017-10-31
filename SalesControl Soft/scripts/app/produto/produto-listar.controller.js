angular.module("teste").controller("ProdutoListarCtrl", ProdutoListarCtrl);

function ProdutoListarCtrl($scope, toastr, ProdutoService, $state) {
    var vm = this;

    vm.editar = function (idProduto) {
        $state.go("produtoEditar", { id: idProduto });
    }

    vm.excluir = function(id){
        ProdutoService.excluir(id).then(function(retorno){
            toastr.success("Produto excluído com sucesso!");
            buscarTodos();
        }).catch(function(erro){
            toastr.error("Ocorreu um erro. Tente novamente.");
            console.error(erro);
        });
    }

    function buscarTodos() {
        ProdutoService.buscarTodos().then(function (retorno) {
            $scope.produtos = retorno.data;
        }).catch(function (erro) {
            toastr.error("Ocorreu um errro. Tente novamente.");
            console.error(erro);
        });
    }

    function init() {
        $scope.produtos = [];
        buscarTodos();
    }

    init();
}