angular.module('salescontrolapp')
    .controller("DetalharController", DetalharController)


    function DetalharController($state, toastr, $scope){

        $scope.produtos = {};
        $scope.id = 0;

        $scope.init = function () {
            $scope.produto = {
                    
    };
    }


    }