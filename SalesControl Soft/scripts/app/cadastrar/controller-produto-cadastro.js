angular.module("salescontrolapp")
    .controller("CadastroController", CadastroController);

function CadastroController($scope, toastr, $state, $http) {
    $scope.produtos = [];
    var init = function () {
        $scope.produtos = {
            nome: '',            marca: '',            colecao: '',            modelo: '',            codigo: '',            valor: '',            quantidade: '',            tamanho: '',            descricao: '',            imagem: ''        };
    }
    $scope.salvar = function () {
        $http.post('http://localhost:8080/produto', (
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
            }));
        }
    
init();
};