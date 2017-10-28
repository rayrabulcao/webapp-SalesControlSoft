angular.module('bios-setup',
    [
        'ui.router',
        'ngMdIcons',
        'ngMaterial',
        'ngAnimate',
        'ngAria',
        'ngMessages',
        'md.data.table'
    ]);

angular.module('bios-setup').directive('title', ['$rootScope', '$timeout',
  function($rootScope, $timeout) {
    return {
      link: function() {

        var listener = function(event, toState) {

          $timeout(function() {
            $rootScope.title = (toState.data && toState.data.pageTitle)
            ? toState.data.pageTitle
            : 'Default title';
          });
        };

        $rootScope.$on('$stateChangeSuccess', listener);
      }
    };
  }
]);


angular.module('bios-setup').constant('feedbacks',
    {
        sensorLuminosidade:  {id: 's', description: 'Sensor de Luminosidade'},
        tempo : {id: 't', description: 'Tempo'},
        sensorTempo: {id: 'st', description: 'Sensor/Tempo'}
    }
);

angular.module('bios-setup').run(['$rootScope', '$state', function($rootScope, $state) {

    $rootScope.$on('$stateChangeStart', function(evt, to, params) {
        if (to.redirectTo) {
            evt.preventDefault();
            $state.go(to.redirectTo, params, {location: 'replace'})
        }
    });

    $rootScope.$on('$stateChangeStart', function (event, toState, toParams) {
        var requireLogin = toState.data.requireLogin;

        var usuario = window.sessionStorage.getItem('usuario');

        if ((requireLogin == true) && (usuario == null)) {
            event.preventDefault();
            $state.go('login');
        }
    });
}]);