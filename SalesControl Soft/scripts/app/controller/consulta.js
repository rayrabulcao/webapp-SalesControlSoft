angular.module('salescontrolapp')
    .controller("ConsultaController", ConsultaController)

function ConsultaController($scope, toastr){
    var vm = this;

    $scope.ConsultaController = [
        {produto: '', }
    ];
}

    vm.consultar = function(){
        console.log($scope.produto);
    }