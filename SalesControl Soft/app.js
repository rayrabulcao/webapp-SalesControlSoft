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
    $stateProvider.state("consultar", {
        url: "/consultar",
        templateUrl: "scripts/app/consultar/consultar.html",
        controller: "Consultarcontroller",
        controllerAs: "controller"
    });
    $stateProvider.state("cadastrar", {
        url: "/cadastrar",
        templateUrl: "scripts/app/cadastrar/cadastrar.html",
        controller: "CadastroController",
        controllerAs: "controller"
    });
    $stateProvider.state("editar", {
        url: "/editar",
        templateUrl: "scripts/app/editar/editar.html",
        controller: "EditarController",
        controllerAs: "controller"
    });
    $stateProvider.state("detalhar", {
        url: "/detalhar",
        templateUrl: "scripts/app/detalhar/detalhar.html",
        controller: "DetalharController",
        controllerAs: "controller"
    });
    $urlRouterProvider.otherwise("/");
}