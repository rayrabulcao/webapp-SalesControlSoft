angular.module('bios-setup').filter('html',function ($sce) {
    return function (text) {
        return $sce.trustAsHtml(text);
    };
});