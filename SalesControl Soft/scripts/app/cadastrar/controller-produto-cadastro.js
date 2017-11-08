angular.module("salescontrolapp")
    .controller("CadastroController", CadastroController);

function CadastroController($scope, toastr,$state){
        

        $scope.produtos = [];

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
    

    /*$scope.enviar = function() {
        if ($scope.produto) {
            atualizar(id);
        } else {
            salvar();
        }


    $scope.atualizar = function(id){
        $scope.produtos = {};
        $scope.edit = false;
        alert ("Produto Atualizado com sucesso!");
    }
}*/

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
        
        //alert("Item adicionado com sucesso.");
        //toastr.success("Produto cadastrado com sucesso!");
        console.log($scope.produtos[0]);
        //$state.transitionTo('consultar');

        app.factory('notificationFactory', function(){
            return{
                sucess: function (text){
                    toastr.success("Produto cadastrado com sucesso!");
                },
                error: function(text){
                    toastr.error("Erro no cadastro do produto");
                }
            };

        });
        };
    
    /*$scope.cancelar = function(){
        
    }*/
    init();
}