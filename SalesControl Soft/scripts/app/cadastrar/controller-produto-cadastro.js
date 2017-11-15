angular.module("salescontrolapp")
    .controller("CadastroController", CadastroController);

function CadastroController($scope, toastr, $state){
        $scope.produtos = [];
    var init = function () {
        $scope.produtos = {
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
    $scope.salvar = function(){
        $scope.produtos.push(
            {
                'nome': $scope.produto.nome,
                'marca': $scope.produto.marca,
                'colecao': $scope.produto.colecao,
                'modelo': $scope.produto.modelo,
                'codigo': $scope.produto.codigo,
                'valor': $scope.produto.valor,
                'quantidade': $scope.produto.quantidade,
                'tamanho': $scope.produto.tamanho,
                'descricao': $scope.produto.descricao,
                'imagem': $scope.produto.imagem
            });
        alert("Item adicionado com sucesso.");
        //toastr.success("Produto cadastrado com sucesso!");
        console.log($scope.produtos[0]);
        };
    init();
}