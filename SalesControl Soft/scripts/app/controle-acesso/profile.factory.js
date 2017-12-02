angular.module('salescontrolapp')
.factory("Profile", Profile)

function Profile() {
    var roles = [];
    
    return {
        setRoles: setRoles,
        isAdmin: isAdmin,
        isCliente: isCliente
    };
    
    function setRoles(roles) {
        this.roles = roles;
    }
    
    function isAdmin() {
        return contains(this.roles, 'ADMIN');
    }
    
    function isCliente() {
        return contains(this.roles, 'CLIENTE');
    }
       
    function contains(array, element) {
	return array && array.indexOf(element) > -1;
    }
}