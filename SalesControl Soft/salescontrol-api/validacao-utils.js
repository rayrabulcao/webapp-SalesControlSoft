const CAMPOS_VALIDOS = 
[
    'codigo',
    'colecao',
    'descricao',
    'imagem',
    'marca',
    'modelo',
    'nome',
    'quantidade',
    'tamanho',
    'valor'
];

class ValidacaoUtils {

    isProdutoValido(produto) {
        let valido = true;

        CAMPOS_VALIDOS.forEach(campo => {
            if(!produto.hasOwnProperty(campo)) {
                valido = false;
            }
        });

        return valido;
    }

    getCamposValidos(produto) {
        let novo = new Object();

        CAMPOS_VALIDOS.forEach(campo => {
            if(produto.hasOwnProperty(campo)) {
                novo[campo] = produto[campo];
            }
        });

        return novo;
    }

}

module.exports = new ValidacaoUtils();
