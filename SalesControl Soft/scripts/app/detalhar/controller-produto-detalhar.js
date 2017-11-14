angular.module('salescontrolapp')
    .controller("DetalharController", DetalharController)


    function DetalharController($state, toastr, $scope){

        $scope.produtos = {};
        $scope.id = 0;

        $scope.init = function () {
            $scope.id = $state.params.id;
            $scope.buscarProduto($scope.id);
                    
        }

        // Busca o produto na API
    $scope.buscarProduto = function(id){
        $http.get("http://127.0.0.1:8080/#!/" + id).then(function(retorno){
            $scope.produto = retorno.data[0];
        }).catch(function(erro){
            toastr.error("Ocorreu um erro! Tente novamente.");
        });
    }

    init();
    }


    