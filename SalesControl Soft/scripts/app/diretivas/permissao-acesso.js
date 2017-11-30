/*global angular*/
"use strict";
angular.module("salescontrolapp",[]).directive("permissaoAcesso", function () {
    return {
        restrict: 'A',
        link: function ($scope, element, attrs) {
            if (attrs.permissaoAcesso === 'block') {
                element.attr('disabled', 'disabled');
                element.append('<span class="block fa fa-lock"></span>');
            }
        }
   };
});