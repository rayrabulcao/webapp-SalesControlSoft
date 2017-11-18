angular.module('salescontrolapp')
    .controller("DetalharController", DetalharController)


function DetalharController($state, toastr, $scope, $http) {
    $scope.produto = {};
    $scope.id = 0;

    var init = function () {
        $scope.id = $state.params.id;
        $scope.buscarProduto($scope.id);
    }

    $scope.editar = function (id) {
        $state.go("editar", { id: id });
    }

    $scope.buscarProduto = function (id) {
        $http.get("http://127.0.0.1:8080/produto/" + id).then(function (retorno) {
            $scope.produto = retorno.data[0];
        }).catch(function (erro) {
            toastr.error("Ocorreu um erro! Tente novamente.");
            console.error(erro);
        });
    }
    init();
}