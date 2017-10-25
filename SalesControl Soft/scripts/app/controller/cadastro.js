angular.module("salescontrolapp")
    .controller("CadastroController", CadastroController);

function CadastroController($scope, toastr){
    var vm = this;
    
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

    vm.salvar = function(){
        console.log($scope.produto);
        // $scope.produto = {};
    }

    vm.cancelar = function(){
        
    }
}