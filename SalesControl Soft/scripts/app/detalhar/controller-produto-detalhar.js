angular.module('salescontrolapp')
    .controller("ConsultaController", ConsultaController)


    function DetalharController($state, $toastr, $scope){

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


    }