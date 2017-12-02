// Definição do módulo
angular.module("salescontrolapp", ["toastr","ui.router"]);

// Configuração
angular.module("salescontrolapp").config(config);

function config(toastrConfig){
    toastrConfig.autoDismiss = true;
    toastrConfig.timeOut = 3000;
    toastrConfig.closeButton = true;
    toastrConfig.progressBar = true;
}

// Rotas
angular.module("salescontrolapp").config(routerConfig);

function routerConfig ($stateProvider, $urlRouterProvider){
    $stateProvider.state("home", {
        url: "/home",
        templateUrl: "scripts/app/home/home.html",
        controller: "HomeController",
        controllerAs: "controller",
        resolve: {
		    checkRoles: function(RouteAccessService, Profile) {
		        return RouteAccessService.checkRoles(Profile.isAdmin());
		    }
		}
    });
    $stateProvider.state("listar", {
        url: "/listar",
        templateUrl: "scripts/app/listar/listar.html",
        controller: "ListarController",
        controllerAs: "controller",
        resolve: {
		    checkRoles: function(RouteAccessService, Profile) {
		        return RouteAccessService.checkRoles(Profile.isAdmin() || Profile.isCliente());
		    }
		}
    });
    $stateProvider.state("cadastrar", {
        url: "/cadastrar",
        templateUrl: "scripts/app/cadastrar/cadastrar.html",
        controller: "CadastroController",
        controllerAs: "controller",
        resolve: {
		    checkRoles: function(RouteAccessService, Profile) {
		        return RouteAccessService.checkRoles(Profile.isAdmin());
		    }
		}
    });
    $stateProvider.state("editar", {
        url: "/editar/:id",
        templateUrl: "scripts/app/editar/editar.html",
        controller: "EditarController",
        controllerAs: "controller",
        resolve: {
		    checkRoles: function(RouteAccessService, Profile) {
		        return RouteAccessService.checkRoles(Profile.isAdmin());
		    }
		}
    });
    $stateProvider.state("detalhar", {
        url: "/detalhar/:id",
        templateUrl: "scripts/app/detalhar/detalhar.html",
        controller: "DetalharController",
        controllerAs: "controller",
        resolve: {
		    checkRoles: function(RouteAccessService, Profile) {
		        return RouteAccessService.checkRoles(Profile.isAdmin() || Profile.isCliente());
		    }
		}
    });
    $stateProvider.state("login", {
        url: "/login",
        templateUrl: "scripts/app/login/login.html",
        controller: "LoginController",
        controllerAs: "controller"
    });
    $urlRouterProvider.otherwise("/login");
}