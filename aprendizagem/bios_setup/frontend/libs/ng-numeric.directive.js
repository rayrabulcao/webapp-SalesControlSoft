(function () {

  'use strict';

  function NgNumeric() {
    return {
      restrict: 'A',
      require: 'ngModel',


      link: function (scope, element) {
        var shiftKey = 16;
        var leftArrowKey = 37;
        var rightArrowKey = 39

        element.bind('keyup', function (event) {
          var code = event.keyCode;
          if (code != shiftKey && code != leftArrowKey && code != rightArrowKey) {
            element[0].value = element[0].value.replace(/\D/g, '');
          }
        });

        element.bind('blur', function () {
          element[0].value = element[0].value.replace(/\D/g, '');
        });
      }
    };
  }

  angular.module('bios-setup').directive('ngNumeric', NgNumeric);
})();
