'use strict';

angular.module('bios-setup').service('EtapaService', function ($q, $http) {
    var url = '/bios-setup-api/etapas';
    return {
        getAll: function () {
            return $q(function (resolve, reject) {
                $http.get(url).then(function (response) {
                    resolve(response.data);
                }, function (error) {
                    reject(error);
                });
            });
        },
        get: function (id_etapa) {
            return $q(function (resolve, reject) {
                $http.get(url + '/' + id_etapa).then(function (response) {
                    resolve(response.data);
                }).catch(function (error) {
                    reject(error);
                });
            });
        },
        create: function (descricao, status) {
            return $q(function (resolve, reject) {
                $http.post(url, {
                    descricao: descricao,
                    status: status
                })
                    .then(function (response) {
                        resolve(response.data);
                    }, function (error) {
                        reject(error);
                    });
            });
        },
        update: function (id_etapa, descricao, status) {
            return $q(function (resolve, reject) {
                $http.put(url + '/' + id_etapa, {
                    descricao: descricao,
                    status: status
                }).then(function (response) {
                    resolve(response);
                }, function (error) {
                    reject(error);
                });
            });
        },
        delete: function (id_etapa) {
            return $q(function (resolve, reject) {
                $http.delete(url + '/' + id_etapa).then(function (response) {
                    resolve(response);
                }, function (error) {
                    reject(error);
                });
            });
        }
    }
});
