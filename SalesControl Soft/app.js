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
        controllerAs: "controller"
    });
    $stateProvider.state("listar", {
        url: "/listar",
        templateUrl: "scripts/app/listar/listar.html",
        controller: "ListarController",
        controllerAs: "controller"
    });
    $stateProvider.state("cadastrar", {
        url: "/cadastrar",
        templateUrl: "scripts/app/cadastrar/cadastrar.html",
        controller: "CadastroController",
        controllerAs: "controller"
    });
    $stateProvider.state("editar", {
        url: "/editar/:id",
        templateUrl: "scripts/app/editar/editar.html",
        controller: "EditarController",
        controllerAs: "controller"
    });
    $stateProvider.state("detalhar", {
        url: "/detalhar/:id",
        templateUrl: "scripts/app/detalhar/detalhar.html",
        controller: "DetalharController",
        controllerAs: "controller"
    });
    $stateProvider.state("login", {
        url: "/login",
        templateUrl: "scripts/app/login/login.html",
        controller: "LoginController",
        controllerAs: "controller"
    });
    $stateProvider.state("cadastroUsuario", {
        url: "/cadastroUsuario",
        templateUrl: "scripts/app/cadastro-usuario/cadastrar-usuario.html",
        controller: "CadastroUsuarioController",
        controllerAs: "controller"
    });
    $urlRouterProvider.otherwise("/login");
}