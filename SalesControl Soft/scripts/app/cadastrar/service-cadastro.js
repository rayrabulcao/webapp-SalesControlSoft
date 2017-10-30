import { Produto } from './model/produto.model';

export class ProdutoService {

    /** @ngInject */
    constructor(
        private $http: ng.IHttpService,
        private API_URL: string
    ) {
        this.API_URL += 'produto';
    }

    public list(): ng.IHttpPromise<Produto[]> {
        return this.$http.get(this.API_URL);
    }

    public get(_id: string): ng.IHttpPromise<Produto> {
        // A interpolação equivale a this.API_URL + '/' + _id
        return this.$http.get(`${this.API_URL}/${_id}`);
    }

    public save(produto: Produto): ng.IHttpPromise<string> {
        return this.$http.post(this.API_URL, produto);
    }

    public update(produto: Produto): ng.IHttpPromise<string> {
        return this.$http.put(`${this.API_URL}/${produto._id}`, produto);
    }

    public delete(_id: string): ng.IHttpPromise<string> {
        return this.$http.delete(`${this.API_URL}/${_id}`);
    }
}

