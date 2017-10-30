angular.module("salescontrolapp")
    .controller("CadastroController", CadastroController);

function CadastroController($scope, toastr){
    var vm = this;

    $scope.item = {};
    
    $scope.produto = {
        nome: '',
        marca: '',
        colecao: '',
        modelo: '',
        codigo: '',
        valor: '',
        quantidade: '',
        tamanho: '',
        descricao: '',
        imagem: ''        
    };

   /* vm.enviar = function() {
        if (this.$scope.produto) {
            this.atualizar();
        } else {
            this.salvar();
        }
    }*/

    vm.salvar = function(){
        
        vm.itens.push({nome: vm.item.nome, marca: vm.item.marca, colecao: vm.item.colecao, modelo: vm.item.modelo, codigo: vm.item.codigo,
            valor: vm.item.valor, quantidade: vm.item.quantidade, tamanho: vm.item.tamanho, descricao: vm.item.descricao, imagem: vm.item.imagem});
        this.$scope.produto = new Produto();
        vm.item.nome = vm.item.marca = vm.item.colecao =
        vm.item.modelo = vm.item.codigo = vm.item.valor =
        vm.item.quantidade = vm.item.tamanho = vm.item.descricao = 
        vm.item.imagem = '';
        this.toastr.success("Item adicionado com sucesso.");
        console.log($scope.produto);
        };
    
    vm.cancelar = function(){
        
    }
}