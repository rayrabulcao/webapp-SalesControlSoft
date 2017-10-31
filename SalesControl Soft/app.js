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

function routerConfig($stateProvider, $urlRouterProvider) {
    // Principal
    $stateProvider
      .state('principal', {
        url: '/',
        templateUrl: 'app/principal/principal.html',
        controller: 'PrincipalCtrl',
        controllerAs: 'controller'
      });

    // Detalhar
    $stateProvider
      .state('produtoDetalhar', {
        url: '/produto-detalhar/:id',
        templateUrl: 'app/produto/produto-detalhar.html',
        controller: 'DetalharCtrl',
        controllerAs: 'controller'
      });
    // Listagem
    $stateProvider
      .state('produtoListar', {
        url: '/produto-listar',
        templateUrl: 'app/produto/produto-listar.html',
        controller: 'ProdutoListarCtrl',
        controllerAs: 'controller'
    });
    // Cadastrar
    $stateProvider
      .state('produtoCadastrar', {
        url: '/produto-cadastrar',
        templateUrl: 'app/produto/produto-cadastrar.html',
        controller: 'ProdutoCadastrarCtrl',
        controllerAs: 'controller'
    });
    // Editar
    $stateProvider
      .state('produtoEditar', {
        url: '/produto-editar/:id',
        templateUrl: 'app/produto/produto-cadastrar.html',
        controller: 'ProdutoEditarCtrl',
        controllerAs: 'controller'
    });

    $urlRouterProvider.otherwise('/');
  }

})();