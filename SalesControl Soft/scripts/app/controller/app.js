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
    $stateProvider.state("listar", {
        url: "/listar",
        templateUrl: "views/l",
        controller: "",
        controllerAs: ""
    });
    $stateProvider.state("cadastrar", {
        url: "/cadastrar",
        templateUrl: "views/screen_cadastrar.html",
        controller: "CadastroController",
        controllerAs: "controller"
    });
    $urlRouterProvider.otherwise("/listar");
}