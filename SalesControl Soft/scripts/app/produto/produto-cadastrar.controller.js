angular.module("teste").controller("ProdutoCadastrarCtrl", ProdutoCadastrarCtrl);

function ProdutoCadastrarCtrl($scope, toastr, ProdutoService) {
    var vm = this;
    $scope.produto = {
        nome: '',
        codigo: '',
        valor: '',
        imagem: '',
        quantidade: '',
        descricao: ''
    };

    function limparForm() {
        $scope.produto = {
            nome: '',
            codigo: '',
            valor: '',
            imagem: '',
            quantidade: '',
            descricao: ''
        };
    }

    vm.salvar = function () {
        ProdutoService.salvar($scope.produto).then(function (retorno) {
            toastr.success("Produto cadastrado com sucesso!");
            limparForm();
        }).catch(function(erro){
            toastr.error("Ocorreu um erro. Tente novamente!");
            console.error(erro);
        });
    }
}
