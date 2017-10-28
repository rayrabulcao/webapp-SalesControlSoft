angular.module('bios-setup')
    .config(function ($stateProvider, $urlRouterProvider, $locationProvider) {

        $urlRouterProvider.otherwise('/etapas/listar');

        $stateProvider
        .state('home', {
            url: '/',
            templateUrl: 'features/home/home.html',
            controller: 'HomeController',
            redirectTo: 'home.configuracoes_listar'
        })
        .state('home.etapas_listar', {
            url: 'etapas/listar',
            templateUrl: 'features/etapa/etapas-listar.html',
            controller: 'EtapasListarController',
            data : { pageTitle: 'Etapas' }
        })
        .state({
            name: 'home.etapa_alterar',
            url: 'etapa/alterar?:id',
            templateUrl: 'features/etapa/etapa-cadastrar-alterar.html',
            controller: 'EtapaAlterarController',
            data : { pageTitle: 'Alterar Etapa' }
        })
        .state('home.etapa_cadastrar', {
            url: 'etapa/cadastrar',
            templateUrl: 'features/etapa/etapa-cadastrar-alterar.html',
            controller: 'EtapaCadastrarController',
            data : { pageTitle: 'Cadastro de Etapas' }
        })
        .state('login', {
            url: '/login',
            templateUrl: 'features/login/login.html',
            controller: 'LoginController',
            data : { requireLogin: false }
        })
        .state('home.configuracao_cadastrar', {
            url: 'configuracao/cadastrar',
            templateUrl: 'features/configuracao/configuracao-cadastrar.html',
            controller: 'ConfiguracaoController',
            params: {
                id_placa_mae: null,
                id_codigo_bios: null
            },
            data : { pageTitle: 'Cadastro de Configurações das Instruções' }
        })
       .state('home.usuario_cadastrar', {
            url: 'usuario/cadastrar',
            templateUrl: 'features/usuario/usuario-cadastrar-alterar.html',
            controller: 'UsuarioCadastrarController',
            data : { pageTitle: 'Cadastro de Usuário' }
        })
        .state('home.usuarios_listar', {
            url: 'usuarios/listar',
            templateUrl: 'features/usuario/usuarios-listar.html',
            controller: 'UsuariosListarController',
            data : { pageTitle: 'Usuários' }
        })
        .state({
            name: 'home.usuario_alterar',
            url: 'usuario/alterar?:id',
            templateUrl: 'features/usuario/usuario-cadastrar-alterar.html',
            controller: 'UsuarioAlterarController',
            data : { pageTitle: 'Alterar Usuário' }
        });
    });
