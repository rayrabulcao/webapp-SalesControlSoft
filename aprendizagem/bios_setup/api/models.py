from bios_setup import db

#-------> SCHEMA DBO - GBI <----

class Placa_Mae(db.Model):
    __tablename__ = 'placa_mae'
    __table_args__ = {'schema': 'dbo'}

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    tipo = db.Column(db.String)
    nomeDesc = db.Column(db.String)

    def to_dict(self):
        return dict(
            nomeDesc=self.nomeDesc,
            tipo=self.tipo,
            nome=self.nome,
            id=self.id
        )

    def __repr__(self):
        return '<Placa_Mae %r>' % (self.id)


class Codigo_BIOS(db.Model):
    __tablename__ = 'codigo_bios'
    __table_args__ = {'schema': 'dbo'}

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String)
    codigo = db.Column(db.String)
    codigo_bios = db.Column(db.String)

    placa_mae_id = db.Column(db.Integer, db.ForeignKey('dbo.placa_mae.id'))
    placa_mae = db.relationship('Placa_Mae')

    status = db.Column(db.String)
    dmiVersion = db.Column(db.String)

    def to_dict(self):
        return dict(
            dmiVersion=self.dmiVersion,
            status=self.status,
            placa_mae=self.placa_mae.to_dict(),
            codigo=self.codigo,
            codigo_bios=self.codigo_bios,
            descricao=self.descricao,
            id=self.id
        )

    def __repr__(self):
        return '<Codigo_BIOS %r>' % (self.id)


#-------> SCHEMA BS - GBI <----

class Etapa(db.Model):
    __tablename__ = 'etapa'
    __table_args__ = {'schema': 'bs'}

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String, unique=True)
    status = db.Column(db.Boolean)
    existe_instrucao = False

    def to_dict(self):
        return dict(
            existeInstrucao=self.existe_instrucao,
            descricao=self.descricao,
            status=self.status,
            id=self.id
        )

    def __repr__(self):
        return '<Etapa %r>' % (self.id)


class Instrucao(db.Model):
    __tablename__ = 'instrucao'
    __table_args__ = {'schema': 'bs'}

    id = db.Column(db.Integer, primary_key=True)
    id_etapa = db.Column(db.Integer, db.ForeignKey('bs.etapa.id'))
    etapa = db.relationship('Etapa')
    id_codigo_bios = db.Column(db.Integer, db.ForeignKey('dbo.codigo_bios.id'))
    codigo_bios = db.relationship('Codigo_BIOS')
    posicao = db.Column(db.Integer)
    descricao = db.Column(db.String)

    def to_dict(self):
        return dict(
            codigo_bios=self.codigo_bios.to_dict(),
            etapa=self.etapa.to_dict(),
            posicao=self.posicao,
            descricao=self.descricao,
            id=self.id
        )

    def __repr__(self):
        return '<Instrucao %r>' % (self.id)


class Configuracao(db.Model):
    __tablename__ = 'configuracao'
    __table_args__ = {'schema': 'bs'}

    id = db.Column(db.Integer, primary_key=True)
    id_placa_mae = db.Column(db.Integer, db.ForeignKey('dbo.placa_mae.id'))
    placa_mae = db.relationship('Placa_Mae')
    id_etapa = db.Column(db.Integer, db.ForeignKey('bs.etapa.id'))
    etapa = db.relationship('Etapa')
    id_codigo_bios = db.Column(db.Integer, db.ForeignKey('dbo.codigo_bios.id'))
    codigo_bios = db.relationship('Codigo_BIOS')
    descricao_instrucao = db.Column(db.String)
    feedback_por = db.Column(db.String)
    color = db.Column(db.Integer)
    sensor_de = db.Column(db.Integer)
    sensor_ate = db.Column(db.Integer)
    tempo = db.Column(db.Float)
    posicao = db.Column(db.Integer)
    bloqueado = db.Column(db.Boolean)
    tipo = db.Column(db.Integer)

    def to_dict(self):
        return dict(
            tipo=self.tipo,
            bloqueado=self.bloqueado,
            posicao=self.posicao,
            tempo=self.tempo,
            sensor_ate=self.sensor_ate,
            sensor_de=self.sensor_de,
            feedback_por=self.feedback_por,
            color=self.color,
            descricao_instrucao=self.descricao_instrucao,
            codigo_bios=self.codigo_bios.to_dict(),
            etapa=self.etapa.to_dict(),
            placa_mae=self.placa_mae.to_dict(),
            id=self.id
        )

    def __repr__(self):
        return '<Configuracao %r>' % (self.id)


class Comando(db.Model):
    __tablename__ = 'comando'
    __table_args__ = {'schema': 'bs'}

    id = db.Column(db.Integer, primary_key=True)
    id_configuracao = db.Column(db.Integer, db.ForeignKey('bs.configuracao.id'))
    configuracao = db.relationship('Configuracao')
    nome_tecla = db.Column(db.String)
    codigo_tecla = db.Column(db.Integer)
    posicao = db.Column(db.Integer)

    def to_dict(self):
        return dict(
            posicao=self.posicao,
            codigo_tecla=self.codigo_tecla,
            nome_tecla=self.nome_tecla,
            configuracao=self.configuracao.to_dict(),
            id=self.id
        )

    def __repr__(self):
        return '<Comando %r>' % (self.id)

class Configuracao_op(db.Model):
    __tablename__ = 'configuracao_op'
    __table_args__ = {'schema': 'bs'}

    id = db.Column(db.Integer, primary_key=True)
    id_placa_mae = db.Column(db.Integer, db.ForeignKey('dbo.placa_mae.id'))
    placa_mae = db.relationship('Placa_Mae')
    id_etapa = db.Column(db.Integer, db.ForeignKey('bs.etapa.id'))
    etapa = db.relationship('Etapa')
    id_codigo_bios = db.Column(db.Integer, db.ForeignKey('dbo.codigo_bios.id'))
    codigo_bios = db.relationship('Codigo_BIOS')
    op = db.Column(db.String)
    descricao_instrucao = db.Column(db.String)
    feedback_por = db.Column(db.String)
    color = db.Column(db.Integer)
    sensor_de = db.Column(db.Integer)
    sensor_ate = db.Column(db.Integer)
    tempo = db.Column(db.Float)
    posicao = db.Column(db.Integer)
    bloqueado = db.Column(db.Boolean)
    tipo = db.Column(db.Integer)

    def to_dict(self):
        return dict(
            tipo=self.tipo,
            bloqueado=self.bloqueado,
            posicao=self.posicao,
            tempo=self.tempo,
            sensor_ate=self.sensor_ate,
            sensor_de=self.sensor_de,
            feedback_por=self.feedback_por,
            color=self.color,
            descricao_instrucao=self.descricao_instrucao,
            op=self.op,
            codigo_bios=self.codigo_bios.to_dict(),
            etapa=self.etapa.to_dict(),
            placa_mae=self.placa_mae.to_dict(),
            id=self.id
        )

    def __repr__(self):
        return '<Configuracao %r>' % (self.id)


class Comando_op(db.Model):
    __tablename__ = 'comando_op'
    __table_args__ = {'schema': 'bs'}

    id = db.Column(db.Integer, primary_key=True)
    id_configuracao_op = db.Column(db.Integer, db.ForeignKey('bs.configuracao_op.id'))
    configuracao_op = db.relationship('Configuracao_op')
    nome_tecla = db.Column(db.String)
    codigo_tecla = db.Column(db.Integer)
    posicao = db.Column(db.Integer)

    def to_dict(self):
        return dict(
            posicao=self.posicao,
            codigo_tecla=self.codigo_tecla,
            nome_tecla=self.nome_tecla,
            configuracao=self.configuracao.to_dict(),
            id=self.id
        )

    def __repr__(self):
        return '<Comando %r>' % (self.id)

class Usuario (db.Model):
    __tablename__ = 'usuario'
    __table_args__ = {'schema': 'bs'}

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    login = db.Column(db.String)
    password = db.Column(db.String)
    admin = db.Column(db.Boolean)

    def to_dict(self):
        return dict(
            admin=self.admin,
            password=self.password,
            login=self.login,
            nome=self.nome,
            id=self.id
        )

    def __repr__(self):
        return 'Usuario %r' % (self.id)
