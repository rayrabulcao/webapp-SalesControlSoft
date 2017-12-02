function AuthController(AuthService, Profile) {
    var vm = this;
    
    vm.submit = submit;
    
    function submit(username, password) {
        AuthService.login(username, password).then(function(response) {
            // A factory Profile guardará as informações dos Perfis
            // do usuários que são passadas pelo back-end
            
            roles: ['ADMIN', 'CLIENTE']
            Profile.setRoles(response.data.roles);
        }).catch(function(response) {
           // Lidar com casos de erro
        });
    }
}