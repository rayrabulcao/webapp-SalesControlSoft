function Config($routeProvider) {
	.when('/', {
		templateUrl: '/auth/auth.html',
		controller: 'AuthController',
		controllerAs: 'vm'
	})
	.when('/admin', {
		templateUrl: '/admin/admin.html',
		controller: 'AdminController',
		controllerAs: 'vm',
		resolve: {
		    checkRoles: function(RouteAccessService, Profile) {
		        return RouteAccessService.checkRoles(Profile.isAdmin());
		    }
		}
	})
	.when('/users', {
		templateUrl: '/users/users.html',
		controller: 'UsersController',
		controllerAs: 'vm',
		resolve: {
		    checkRoles: function(RouteAccessService, Profile) {
		        return RouteAccessService.checkRoles(Profile.isAdmin() ||
		                                             Profile.isModification());
		    }
		}
	});
}