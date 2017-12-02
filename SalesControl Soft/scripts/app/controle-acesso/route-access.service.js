angular.module('salescontrolapp')
.service("RouteAccessService", RouteAccessService)

function RouteAccessService($location) {
    this.checkRoles = function(access) {
        if (!access) {
            $location.path('/login');
        }
    }
}