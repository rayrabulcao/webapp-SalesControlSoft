import json

import sqlalchemy
from sqlalchemy.sql.expression import func

from flask import abort, jsonify, request
from sqlalchemy.exc import IntegrityError

from sqlalchemy import desc

from bios_setup import app, db
from bios_setup.api import models

import os

import os.path

from tinydb import TinyDB


@app.route('/bios-setup-api/etapas', methods=['GET'])
def get_all_etapas():
    entities = models.Etapa.query.all()
    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/bios-setup-api/etapas/ativas', methods=['GET'])
def get_etapas_ativas():
    entities = db.session.query(models.Etapa) \
        .filter(models.Etapa.status != 0)
    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/bios-setup-api/etapas/<int:id>', methods=['GET'])
def get_etapa(id):
    entity = models.Etapa.query.get(id)
    entity.existe_instrucao = models.Instrucao.query.filter(models.Instrucao.id_etapa == id).count() > 0

    if not entity:
        abort(404)
    response = entity.to_dict()

    return jsonify(response)


@app.route('/bios-setup-api/etapas', methods=['POST'])
def create_etapa():
    entity = models.Etapa(
        descricao=request.json['descricao'],
        status=request.json['status']
    )

    try:
        db.session.add(entity)
        db.session.commit()
    except IntegrityError:
        abort(403)

    return jsonify(entity.to_dict())


@app.route('/bios-setup-api/etapas/<int:id>', methods=['PUT'])
def update_etapa(id):
    entity = models.Etapa.query.get(id)
    if not entity:
        abort(404)
    entity = models.Etapa(
        descricao=request.json['descricao'],
        status=request.json['status'],
        id=id
    )
    try:
        db.session.merge(entity)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        abort(403)
    return '', 204


@app.route('/bios-setup-api/etapas/<int:id>', methods=['DELETE'])
def delete_etapa(id):
    db.session.query(models.Instrucao).filter(models.Instrucao.id_etapa == id).delete(
        synchronize_session='fetch')
    entity = models.Etapa.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/bios-setup-api/instrucoes', methods=['GET'])
def get_all_instrucoes():
    entities = db.session.query(models.Instrucao) \
        .join(models.Etapa) \
        .join(models.Codigo_BIOS) \
        .join(models.Placa_Mae) \
        .with_entities(
            models.Instrucao.id_codigo_bios,
            models.Instrucao.id_etapa,
            models.Etapa.descricao,
            models.Codigo_BIOS.descricao,
            models.Codigo_BIOS.codigo,
            models.Codigo_BIOS.codigo_bios,
            models.Placa_Mae.id,
            models.Placa_Mae.nomeDesc
        ) \
        .group_by(
            models.Instrucao.id_etapa,
            models.Instrucao.id_codigo_bios,
            models.Etapa.descricao,
            models.Codigo_BIOS.descricao,
            models.Codigo_BIOS.codigo,
            models.Codigo_BIOS.codigo_bios,
            models.Placa_Mae.id,
            models.Placa_Mae.nomeDesc
        ) \
        .filter(models.Etapa.status != 0)

    return json.dumps(
        [
            dict(
                id_codigo_bios=entity[0],
                id_etapa=entity[1],
                etapa_desc=entity[2],
                bios_desc=entity[3],
                bios_codigo=entity[4],
                codigo_bios=entity[5],
                id_placa_mae=entity[6],
                nomeDesc=entity[7]
            )
            for entity in entities
            ]
    )


@app.route('/bios-setup-api/instrucoes/<int:id_placa_mae>/<int:id_versao_bios>/<int:id_etapa>', methods=['GET'])
def get_all_instrucoes_by_versao_bios_etapa(id_placa_mae, id_versao_bios, id_etapa):
    entities = db.session.query(models.Instrucao) \
        .join(models.Codigo_BIOS) \
        .join(models.Placa_Mae) \
        .filter(
            models.Instrucao.id_codigo_bios == id_versao_bios,
            models.Instrucao.id_etapa == id_etapa,
            models.Codigo_BIOS.placa_mae_id == id_placa_mae
        )
    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/bios-setup-api/instrucoes/<int:id_versao_bios>/<int:id_etapa>', methods=['GET'])
def get_all_instrucoes_by_versao_bios_etapa_que_tem_instrucao(id_versao_bios, id_etapa):
    entities = db.session.query(models.Instrucao) \
        .filter(
            models.Instrucao.id_codigo_bios == id_versao_bios,
            models.Instrucao.id_etapa == id_etapa
        )
    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/bios-setup-api/instrucoes/<int:id>', methods=['GET'])
def get_instrucao(id):
    entity = models.Instrucao.query.get(id)
    if not entity:
        abort(404)
    return jsonify(entity.to_dict())


@app.route('/bios-setup-api/instrucoes/<int:id_versao_bios>/<int:id_etapa>', methods=['POST'])
def create_instrucao(id_versao_bios, id_etapa):
    db.session.query(models.Instrucao).filter(models.Instrucao.id_codigo_bios == id_versao_bios,
                                              models.Instrucao.id_etapa == id_etapa).delete(
        synchronize_session='fetch');

    for index, item in enumerate(request.json['instrucoes']):
        entity = models.Instrucao(
            id_codigo_bios=id_versao_bios,
            id_etapa=id_etapa,
            descricao=item,
            posicao=index
        )
        db.session.add(entity)

    db.session.commit()
    return '', 204


@app.route('/bios-setup-api/instrucoes/<int:id_versao_bios>/<int:id_etapa>', methods=['DELETE'])
def delete_instrucao(id_versao_bios, id_etapa):
    db.session.query(models.Instrucao).filter(
        models.Instrucao.id_codigo_bios == id_versao_bios,
        models.Instrucao.id_etapa == id_etapa
    ).delete(synchronize_session='fetch')
    db.session.commit()
    return '', 204


@app.route('/bios-setup-api/versoes_bios', methods=['GET'])
def get_all_versoes_bios():
    entities = db.session.query(models.Codigo_BIOS).join(models.Placa_Mae).order_by('nomeDesc')
    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/bios-setup-api/modelos', methods=['GET'])
def get_all_modelos():
    entities = models.Placa_Mae.query.order_by('nomeDesc').all()
    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/bios-setup-api/configuracoes', methods=['GET'])
def get_all_configuracoes():
    entities = db.session.query(models.Configuracao) \
        .join(models.Codigo_BIOS) \
        .join(models.Placa_Mae) \
        .with_entities\
            (
                models.Placa_Mae.id,
                models.Placa_Mae.nomeDesc,
                models.Codigo_BIOS.id,
                models.Codigo_BIOS.codigo_bios,
                models.Codigo_BIOS.codigo
            ).distinct()

    return json.dumps\
            (
                [
                    dict
                        (
                            id_placa_mae=entity[0],
                            nomeDesc=entity[1],
                            id_codigo_bios=entity[2],
                            codigo_bios=entity[3],
                            codigo=entity[4]
                        )
                    for entity in entities
                ]
        )


@app.route('/bios-setup-api/configuracoes/etapas/<int:id_versao_bios>', methods=['GET'])
def get_etapas_for_bios(id_versao_bios):
    entities = db.session.query(models.Etapa) \
        .join(models.Configuracao) \
        .filter(models.Configuracao.id_codigo_bios == id_versao_bios) \
        .with_entities(models.Etapa.id, models.Etapa.descricao, models.Configuracao.id_codigo_bios) \
        .group_by(models.Etapa.id, models.Etapa.descricao, models.Configuracao.id_codigo_bios)

    return json.dumps(
        [dict(id_etapa=entity[0], descricao_etapa=entity[1], id_versao_bios=entity[2]) for entity in entities])


@app.route('/bios-setup-api/configuracao/config_etapas/<int:id_versao_bios>', methods=['GET'])
def get_etapas_for_bios_por_config(id_versao_bios):
    entities = db.session.query(models.Etapa) \
        .join(models.Configuracao) \
        .filter(models.Configuracao.id_codigo_bios == id_versao_bios) \
        .with_entities(models.Etapa.id, models.Etapa.descricao) \
        .group_by(models.Etapa.id, models.Etapa.descricao)

    return json.dumps(
        [dict(id_etapa=entity[0], descricao_etapa=entity[1]) for entity in entities])


@app.route('/bios-setup-api/config_por_op/config_etapas/<int:id_placa_mae>/<int:id_versao_bios>/<path:op>', methods=['GET'])
def get_etapas_for_bios_por_config_por_op(id_placa_mae, id_versao_bios, op):
    entities = db.session.query(models.Etapa) \
        .join(models.Configuracao_op) \
        .filter\
            (
                models.Configuracao_op.id_codigo_bios == id_versao_bios,
                models.Configuracao_op.id_placa_mae == id_placa_mae,
                models.Configuracao_op.op == op) \
        .with_entities(models.Etapa.id, models.Etapa.descricao) \
        .group_by(models.Etapa.id, models.Etapa.descricao)

    return json.dumps(
        [dict(id_etapa=entity[0], descricao_etapa=entity[1]) for entity in entities])


@app.route('/bios-setup-api/configuracoes/instrucoes/<int:id_versao_bios>/<int:id_etapa>', methods=['GET'])
def get_instrucoes_for_bios(id_versao_bios, id_etapa):
    entities = db.session.query(models.Configuracao) \
        .join(models.Etapa) \
        .with_entities(models.Configuracao.descricao_instrucao, models.Configuracao.posicao) \
        .filter(models.Configuracao.id_codigo_bios == id_versao_bios, models.Configuracao.id_etapa == id_etapa)

    return json.dumps(
        [dict(descricao_instrucao=entity[0], posicao=entity[1]) for entity in entities])


@app.route('/bios-setup-api/configuracoes/configuracao_instrucoes/<int:id_placa>/<int:id_versao_bios>/<int:id_etapa>',
           methods=['GET'])
def get_instrucoes_configuracao_bios(id_placa, id_versao_bios, id_etapa):
    entities = db.session.query(models.Configuracao) \
        .filter(
            models.Configuracao.id_placa_mae == id_placa,
            models.Configuracao.id_codigo_bios == id_versao_bios,
            models.Configuracao.id_etapa == id_etapa
    ).order_by('posicao')

    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/bios-setup-api/configuracoes/', methods=['POST'])
def create_configuracao():
    j = 0

    nome_tecla = request.json['nome_tecla']
    codigo_tecla = request.json['codigo_tecla']

    if 'feedback' in request.json:
        feed = request.json['feedback']
    else:
        feed = None

    if 'color' in request.json:
        color = request.json['color']
        if color == None:
            color = 100

    # if 'sensor_de' in request.json:
    #     s_de = request.json['sensor_de']
    #     if s_de == None:
    #         s_de = 0

    s_de = 0

    # if 'sensor_ate' in request.json:
    #     s_ate = request.json['sensor_ate']
    #     if s_ate == None:
    #         s_ate = 0

    s_ate = 0

    if 'tempo' in request.json:
        temp = request.json['tempo']
        if temp == None:
            temp = 0.1


    if 'tipo' in request.json:
        tipo = request.json['tipo']
    else:
        tipo = 1

    instrucoes = request.json['instrucao']
    posicao = request.json['posicao']
    bloqueado = request.json['bloqueado']

    id_placa_mae = request.json['placa_mae']
    id_etapa = request.json['etapa']
    id_codigo_bios = request.json['codigo_bios']

    excluiu = request.json['instrucao_excluidas']

    if excluiu:
        db.session.query(models.Configuracao) \
            .filter(
                models.Configuracao.id_placa_mae == id_placa_mae,
                models.Configuracao.id_codigo_bios == id_codigo_bios
            ) \
            .delete(synchronize_session='evaluate')
    else:
        db.session.query(models.Configuracao) \
            .filter(
                models.Configuracao.id_placa_mae == id_placa_mae,
                models.Configuracao.id_codigo_bios == id_codigo_bios,
                models.Configuracao.id_etapa == id_etapa,
                models.Configuracao.descricao_instrucao == instrucoes
            ) \
            .delete(synchronize_session='evaluate')
        
    entity = models.Configuracao(
        id_placa_mae=id_placa_mae,
        id_etapa=id_etapa,
        id_codigo_bios=id_codigo_bios,
        descricao_instrucao=instrucoes,
        feedback_por=feed,
        color=color,
        sensor_de=s_de,
        sensor_ate=s_ate,
        tempo=temp,
        posicao=posicao,
        bloqueado=bloqueado,
        tipo=tipo
    )
    try:
        db.session.add(entity)
        db.session.commit()
    except IntegrityError:
        abort(403)

    id_configuracao = db.session.query(func.max(models.Configuracao.id))
    for id_config in id_configuracao:
        pass
    id_configuracao = id_config[0]

    while j < len(codigo_tecla):
        entityComando = models.Comando(
            id_configuracao=id_configuracao,
            nome_tecla=nome_tecla[j],
            codigo_tecla=codigo_tecla[j],
            posicao=posicao
        )
        try:
            db.session.add(entityComando)
            db.session.commit()
            j = j + 1
        except IntegrityError:
            abort(403)
    return '', 204


@app.route('/bios-setup-api/configuracoes/comandos/<int:id_placa_mae>/<int:id_versao_bios>/<int:id_etapa>/<string:descricao_instrucao>',
           methods=['GET'])
def get_all_comandos_configuracoes(id_placa_mae,  id_versao_bios, id_etapa, descricao_instrucao):
    entities = db.session.query(models.Configuracao) \
        .join(models.Comando) \
        .with_entities(
        models.Comando.nome_tecla,
        models.Comando.codigo_tecla,
        models.Configuracao.feedback_por,
        models.Configuracao.sensor_de,
        models.Configuracao.sensor_ate,
        models.Configuracao.tempo,
        models.Configuracao.bloqueado,
        models.Configuracao.tipo,
        models.Configuracao.color
    ).filter(models.Configuracao.id_placa_mae == id_placa_mae,
             models.Configuracao.id_codigo_bios == id_versao_bios,
             models.Configuracao.id_etapa == id_etapa,
             models.Configuracao.descricao_instrucao == descricao_instrucao)

    return json.dumps(
        [
            dict
                (
                nome_tecla=entity[0],
                codigo_tecla=entity[1],
                feedback_por=entity[2],
                sensor_de=entity[3],
                sensor_ate=entity[4],
                tempo=entity[5],
                bloqueado=entity[6],
                tipo=entity[7],
                color=entity[8]
            )
            for entity in entities
            ]
    )


@app.route('/bios-setup-api/configuracoes/<int:id_placa_mae>/<int:id_codigo_bios>', methods=['DELETE'])
def delete_configuracao(id_placa_mae, id_codigo_bios):
    db.session.query(models.Configuracao) \
        .filter(
        models.Configuracao.id_placa_mae == id_placa_mae,
        models.Configuracao.id_codigo_bios == id_codigo_bios) \
        .delete(
        synchronize_session='evaluate'
    )
    db.session.commit()
    return '', 204


@app.route('/bios-setup-api/configuracoes/<int:id_placa_mae>/<int:id_codigo_bios>', methods=['GET'])
def get_all_configuracoes_for_placa_and_bios(id_placa_mae, id_codigo_bios):
    entities = db.session.query(models.Configuracao) \
        .filter(
        models.Configuracao.id_placa_mae == id_placa_mae,
        models.Configuracao.id_codigo_bios == id_codigo_bios
    )

    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/bios-setup-api/configuracoes/versoes_bios/<int:id_placa_mae>', methods=['GET'])
def get_all_versoes_bios_by_placa_mae(id_placa_mae):
    targetCodigoBiosExists = db.session.query(models.Configuracao) \
        .with_entities(models.Configuracao.id_codigo_bios) \
        .filter(models.Configuracao.id_placa_mae == id_placa_mae)

    entities = db.session.query(models.Codigo_BIOS) \
        .with_entities(models.Codigo_BIOS.id, models.Codigo_BIOS.codigo, models.Codigo_BIOS.descricao) \
        .join(models.Instrucao) \
        .filter(~models.Codigo_BIOS.id.in_(targetCodigoBiosExists)) \
        .group_by(models.Codigo_BIOS.id, models.Codigo_BIOS.codigo, models.Codigo_BIOS.descricao)

    return json.dumps(
        [
            dict
                (
                id=entity[0],
                codigo_bios=entity[1],
                descricao_bios=entity[2]
            )
            for entity in entities
            ]
    )


@app.route('/bios-setup-api/configuracoes/versoes_bios_by_placa/<int:id_placa_mae>', methods=['GET'])
def get_all_versoes_bios_by_placa_mae_ativa(id_placa_mae):
    entities = db.session.query(models.Codigo_BIOS).join(models.Placa_Mae).filter(models.Placa_Mae.id==id_placa_mae).order_by('codigo_bios')
    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/bios-setup-api/configuracoes/gerar_script/<int:id_placa_mae>/<int:id_codigo_bios>', methods=['POST'])
def gerar_script_configuracao(id_placa_mae, id_codigo_bios):
    caminho = '/'
    # db_path_file = '/mnt/biossetup/'
    db_path_file = '/var/www/html/biossetup/'
    entrada = ''

    codigo_bios = db.session.query(models.Codigo_BIOS.codigo_bios).filter(models.Codigo_BIOS.id == id_codigo_bios)
    for codigo_bio in codigo_bios:
        pass
    codigo_bios = codigo_bio[0]


    nomeDesc = db.session.query(models.Placa_Mae.nomeDesc).filter(models.Placa_Mae.id == id_placa_mae)
    for nmDesc in nomeDesc:
        pass
    nomeDesc = nmDesc[0]


    codigo = db.session.query(models.Codigo_BIOS.codigo).filter(models.Codigo_BIOS.id == id_codigo_bios)
    for code in codigo:
        pass
    codigo = code[0]

    nome_arquivo = str(codigo_bios) + '_' + str(nomeDesc) + '_' + str(codigo) + '.json'
    pwd = db_path_file + nome_arquivo

    if (os.path.isfile(pwd)):
        os.remove(pwd)
        file_script = TinyDB(pwd)
    else:
        file_script = TinyDB(pwd)

    for configuracao in request.json:
        j = 0
        t = 0

        etapas = db.session.query(models.Etapa.descricao).filter(models.Etapa.id == configuracao['etapa'])
        for etapa in etapas:
            pass
        descricao_etapa = etapa[0]

        data_table = file_script.table(str(descricao_etapa))

        tipo = configuracao['tipo']

        if (tipo == 0):
            while t < len(configuracao['codigo_tecla']):
                if (t == 0):
                    entrada = str(configuracao['codigo_tecla'][t])
                else:
                    entrada = entrada + '-' + str(configuracao['codigo_tecla'][t])
                t = t + 1
            if configuracao['color'] == None:
                configuracao['color'] = 100

            if configuracao['tempo'] == None:
                configuracao['tempo'] = 0.1

            data_table.insert \
                    (
                    {
                        'tempo': configuracao['tempo'],
                        'comando': entrada,
                        'tipo': configuracao['tipo'],
                        'step': configuracao['instrucao'],
                        'color': int(configuracao['color']),
                        'ldr1': int(0),
                        'ldr2': int(0)
                    }
                )
            entrada = ''
        else:
            while j < len(configuracao['codigo_tecla']):
                if configuracao['color'] == None:
                    configuracao['color'] = 100
                data_table.insert \
                        (
                        {
                            'tempo': configuracao['tempo'],
                            'comando': configuracao['codigo_tecla'][j],
                            'tipo': configuracao['tipo'],
                            'step': configuracao['instrucao'],
                            'color': int(configuracao['color']),
                            'ldr1': int(0),
                            'ldr2': int(0)
                        }
                    )
                j = j + 1

    return '', 204


@app.route('/bios-setup-api/config_por_op/', methods=['POST'])
def create_config_por_op():
    j = 0

    nome_tecla = request.json['nome_tecla']
    codigo_tecla = request.json['codigo_tecla']

    if 'feedback' in request.json:
        feed = request.json['feedback']
    else:
        feed = None

    if 'color' in request.json:
        color = request.json['color']
        if color == None:
            s_de = 100

    # if 'sensor_de' in request.json:
    #     s_de = request.json['sensor_de']
    #     if s_de == None:
    #         s_de = 0

    s_de = 0

    # if 'sensor_ate' in request.json:
    #     s_ate = request.json['sensor_ate']
    #     if s_ate == None:
    #         s_ate = 0

    s_ate = 0

    if 'tempo' in request.json:
        temp = request.json['tempo']
        if temp == None:
            temp = 0.1

    if 'tipo' in request.json:
        tipo = request.json['tipo']
    else:
        tipo = 1

    instrucoes = request.json['instrucao']
    posicao = request.json['posicao']
    bloqueado = request.json['bloqueado']

    id_placa_mae = request.json['placa_mae']
    id_etapa = request.json['etapa']
    id_codigo_bios = request.json['codigo_bios']

    op = request.json['op']

    op_backup = request.json['op_backup']

    excluiu = request.json['instrucao_excluidas']

    if excluiu:
        db.session.query(models.Configuracao_op) \
            .filter(
            models.Configuracao_op.id_placa_mae == id_placa_mae,
            models.Configuracao_op.id_codigo_bios == id_codigo_bios,
            models.Configuracao_op.op == op_backup
        ) \
            .delete(synchronize_session='evaluate')
    else:
        db.session.query(models.Configuracao_op) \
            .filter(
            models.Configuracao_op.id_placa_mae == id_placa_mae,
            models.Configuracao_op.id_etapa == id_etapa,
            models.Configuracao_op.id_codigo_bios == id_codigo_bios,
            models.Configuracao_op.descricao_instrucao == instrucoes,
            models.Configuracao_op.op == op_backup
        ) \
            .delete(synchronize_session='evaluate')


    entity = models.Configuracao_op(
        id_placa_mae=id_placa_mae,
        id_etapa=id_etapa,
        id_codigo_bios=id_codigo_bios,
        descricao_instrucao=instrucoes,
        feedback_por=feed,
        color=color,
        sensor_de=s_de,
        sensor_ate=s_ate,
        tempo=temp,
        posicao=posicao,
        bloqueado=bloqueado,
        tipo=tipo,
        op=op
    )
    try:
        db.session.add(entity)
        db.session.commit()
    except IntegrityError:
        abort(403)

    id_configuracao_op = db.session.query(func.max(models.Configuracao_op.id))
    for id_config in id_configuracao_op:
        pass
    id_configuracao_op = id_config[0]

    while j < len(codigo_tecla):
        entityComando = models.Comando_op(
            id_configuracao_op=id_configuracao_op,
            nome_tecla=nome_tecla[j],
            codigo_tecla=codigo_tecla[j],
            posicao=posicao
        )
        try:
            db.session.add(entityComando)
            db.session.commit()
            j = j + 1
        except IntegrityError:
            abort(403)
    return '', 204


@app.route('/bios-setup-api/config_por_op/', methods=['GET'])
def get_all_configuracao_por_op():
    entities = db.session.query(models.Configuracao_op) \
        .join(models.Codigo_BIOS) \
        .join(models.Placa_Mae) \
        .with_entities \
            (
            models.Placa_Mae.id,
            models.Placa_Mae.nomeDesc,
            models.Codigo_BIOS.id,
            models.Codigo_BIOS.codigo_bios,
            models.Codigo_BIOS.codigo,
            models.Configuracao_op.op
        ).distinct()

    return json.dumps(
        [
            dict
                (
                id_placa_mae=entity[0],
                nomeDesc=entity[1],
                id_codigo_bios=entity[2],
                codigo_bios=entity[3],
                codigo=entity[4],
                op=entity[5]
            )
            for entity in entities
            ]
    )


@app.route('/bios-setup-api/config_por_op/<int:id_placa_mae>/<int:id_codigo_bios>/<path:ordem_producao>', methods=['DELETE'])
def delete_configuracao_por_op(id_placa_mae, id_codigo_bios, ordem_producao):
    db.session.query(models.Configuracao_op) \
        .filter(
            models.Configuracao_op.id_placa_mae == id_placa_mae,
            models.Configuracao_op.id_codigo_bios == id_codigo_bios,
            models.Configuracao_op.op == ordem_producao)\
        .delete(
        synchronize_session='evaluate'
    )
    db.session.commit()
    return '', 204


@app.route('/bios-setup-api/config_por_op/<path:ordem_producao>', methods=['GET'])
def get_all_configuracoes_op_for_op(ordem_producao):
    entities = db.session.query(models.Configuracao_op) \
        .filter(
            models.Configuracao_op.op == ordem_producao
    )

    return json.dumps([entity.to_dict() for entity in entities])

@app.route('/bios-setup-api/login/', methods=['POST'])
def get_user_valido():

    acesso = request.json

    entities = db.session.query(models.Usuario)\
        .filter(
        models.Usuario.login == acesso[0]['login'],
        models.Usuario.password == acesso[0]['senha']
    )

    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/bios-setup-api/config_por_op/modelos/', methods=['GET'])
def get_all_modelos_config_por_op():
    entities = db.session.query(models.Configuracao)\
        .join(models.Placa_Mae)\
        .with_entities\
        (
            models.Placa_Mae.id,
            models.Placa_Mae.nomeDesc
        )\
        .group_by\
        (
            models.Placa_Mae.id,
            models.Placa_Mae.nomeDesc
        )
    return json.dumps(
        [
            dict
                (
                id_placa_mae=entity[0],
                nomeDesc=entity[1]
            )
            for entity in entities
            ]
    )

@app.route('/bios-setup-api/config_por_op/bios/<int:id_placa>', methods=['GET'])
def get_all_bios_config_por_op(id_placa):
    entities = db.session.query(models.Configuracao) \
    .join(models.Codigo_BIOS) \
    .join(models.Placa_Mae) \
    .with_entities\
        (
            models.Codigo_BIOS.id,
            models.Codigo_BIOS.codigo_bios,
            models.Codigo_BIOS.codigo,
            models.Placa_Mae.id,
            models.Placa_Mae.nomeDesc
        )  \
    .filter(models.Configuracao.id_placa_mae == id_placa) \
    .distinct()
    return json.dumps(
        [
            dict
                (
                id_codigo_bios=entity[0],
                codigo_bios=entity[1],
                codigo=entity[2],
                id_placa=entity[3],
                nomeDesc=entity[4]
            )
            for entity in entities
            ]
    )


@app.route('/bios-setup-api/config_por_op/verificar_existente/<path:op>', methods=['GET'])
def verificar_config_por_op_existente(op):
    entities = db.session.query(models.Configuracao_op)\
        .filter\
        (
            models.Configuracao_op.op == op
        )
    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/bios-setup-api/usuario/verificar_existente/<string:login>', methods=['GET'])
def verificar_login_existente(login):
    entities = db.session.query(models.Usuario).filter(models.Usuario.login == login)
    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/bios-setup-api/config_por_op/config_por_op_instrucoes/<int:id_placa>/<int:id_versao_bios>/<int:id_etapa>/<path:op>',
           methods=['GET'])
def get_instrucoes_config_por_op_bios(id_placa, id_versao_bios, id_etapa, op):
    entities = db.session.query(models.Configuracao_op) \
        .filter\
            (
                models.Configuracao_op.id_placa_mae == id_placa,
                models.Configuracao_op.id_codigo_bios == id_versao_bios,
                models.Configuracao_op.id_etapa == id_etapa,
                models.Configuracao_op.op == op
            ).order_by('posicao')
    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/bios-setup-api/config_por_op/comandos/<int:id_placa_mae>/<int:id_versao_bios>/<int:id_etapa>/<string:descricao_instrucao>/<path:op>',
           methods=['GET'])
def get_all_comandos_config_por_op(id_placa_mae, id_versao_bios, id_etapa, descricao_instrucao, op):
    entities = db.session.query(models.Configuracao_op) \
        .join(models.Comando_op) \
        .with_entities(
        models.Comando_op.nome_tecla,
        models.Comando_op.codigo_tecla,
        models.Configuracao_op.feedback_por,
        models.Configuracao_op.sensor_de,
        models.Configuracao_op.sensor_ate,
        models.Configuracao_op.tempo,
        models.Configuracao_op.bloqueado,
        models.Configuracao_op.tipo,
        models.Configuracao_op.color
    ).filter(models.Configuracao_op.id_placa_mae == id_placa_mae,
             models.Configuracao_op.id_codigo_bios == id_versao_bios,
             models.Configuracao_op.id_etapa == id_etapa,
             models.Configuracao_op.descricao_instrucao == descricao_instrucao,
             models.Configuracao_op.op == op)

    return json.dumps(
        [
            dict
                (
                nome_tecla=entity[0],
                codigo_tecla=entity[1],
                feedback_por=entity[2],
                sensor_de=entity[3],
                sensor_ate=entity[4],
                tempo=entity[5],
                bloqueado=entity[6],
                tipo=entity[7],
                color=entity[8]
            )
            for entity in entities
            ]
    )


@app.route('/bios-setup-api/config_por_op/gerar_script/<int:id_placa_mae>/<int:id_codigo_bios>', methods=['POST'])
def gerar_script_config_por_op(id_placa_mae, id_codigo_bios):
    # db_path_file = '/mnt/biossetup/'
    db_path_file = '/var/www/html/biossetup/'

    entrada = ''

    codigo_bios = db.session.query(models.Codigo_BIOS.codigo_bios).filter(models.Codigo_BIOS.id == id_codigo_bios)
    for codigo_bio in codigo_bios:
        pass
    codigo_bios = codigo_bio[0]


    nomeDesc = db.session.query(models.Placa_Mae.nomeDesc).filter(models.Placa_Mae.id == id_placa_mae)
    for nmDesc in nomeDesc:
        pass
    nomeDesc = nmDesc[0]


    codigo = db.session.query(models.Codigo_BIOS.codigo).filter(models.Codigo_BIOS.id == id_codigo_bios)
    for code in codigo:
        pass
    codigo = code[0]

    nome_arquivo = str(codigo_bios) + '_' + str(nomeDesc) + '_' + str(codigo) + '.json'
    pwd = db_path_file + nome_arquivo

    if (os.path.isfile(pwd)):
        os.remove(pwd)
        file_script = TinyDB(pwd)
    else:
        file_script = TinyDB(pwd)

    for configuracao in request.json:
        j = 0
        t = 0

        etapas = db.session.query(models.Etapa.descricao).filter(models.Etapa.id == configuracao['etapa'])
        for etapa in etapas:
            pass
        descricao_etapa = etapa[0]

        data_table = file_script.table(str(descricao_etapa))

        tipo = configuracao['tipo']

        if(tipo == 0):
            while t < len(configuracao['codigo_tecla']):
                if (t==0):
                    entrada = str(configuracao['codigo_tecla'][t])
                else:
                    entrada = entrada + '-' + str(configuracao['codigo_tecla'][t])
                t = t + 1
            if configuracao['color'] == None:
                configuracao['color'] = 100

            if configuracao['tempo'] == None:
                configuracao['tempo'] = 0.1

            data_table.insert \
                    (
                        {
                            'tempo': configuracao['tempo'],
                            'comando': entrada,
                            'tipo': configuracao['tipo'],
                            'step': configuracao['instrucao'],
                            'color': int(configuracao['color']),
                            'ldr1': int(0),
                            'ldr2': int(0)
                        }
                    )
            entrada = ''
        else:
            while j < len(configuracao['codigo_tecla']):
                if configuracao['color'] == None:
                    configuracao['color'] = 100
                data_table.insert\
                    (
                        {
                            'tempo': configuracao['tempo'],
                            'comando': configuracao['codigo_tecla'][j],
                            'tipo': configuracao['tipo'],
                            'step': configuracao['instrucao'],
                            'color': int(configuracao['color']),
                            'ldr1': int(0),
                            'ldr2': int(0)
                        }
                    )
                j = j + 1

    return '', 204

@app.route('/bios-setup-api/configuracao/etapa/<int:id_codigo_bios>', methods=['GET'])
def add_mais_etapa_configuracao(id_codigo_bios):

    targetEtapaNotExists = db.session.query(models.Codigo_BIOS)\
        .join(models.Configuracao)\
        .join(models.Etapa)\
        .with_entities(models.Etapa.id)\
        .filter(models.Codigo_BIOS.id == id_codigo_bios)

    entities = db.session.query(models.Etapa) \
        .filter(~models.Etapa.id.in_(targetEtapaNotExists))

    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/bios-setup-api/config_por_op/etapa/<int:id_codigo_bios>', methods=['GET'])
def add_mais_etapa_config_por_op(id_codigo_bios):

    targetEtapaNotExists = db.session.query(models.Codigo_BIOS)\
        .join(models.Configuracao_op)\
        .join(models.Etapa)\
        .with_entities(models.Etapa.id)\
        .filter(models.Codigo_BIOS.id == id_codigo_bios)

    entities = db.session.query(models.Etapa) \
        .filter(~models.Etapa.id.in_(targetEtapaNotExists))

    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/bios-setup-api/usuarios/', methods=['POST'])
def create_usuario():
    entity = models.Usuario(
        nome=request.json['nome'],
        login=request.json['login'],
        password=request.json['password'],
        admin=request.json['admin']
    )
    try:
        db.session.add(entity)
        db.session.commit()
    except IntegrityError:
        abort(403)

    return jsonify(entity.to_dict())


@app.route('/bios-setup-api/usuario/<int:id>', methods=['GET'])
def get_usuario(id):
    entity = models.Usuario.query.get(id)
    if not entity:
        abort(404)
    response = entity.to_dict()

    return jsonify(response)


@app.route('/bios-setup-api/usuarios/', methods=['GET'])
def get_all_usuarios():
    entities = models.Usuario.query.all()
    return json.dumps([entity.to_dict() for entity in entities])


@app.route('/bios-setup-api/usuario/<int:id>', methods=['PUT'])
def update_usuario(id):
    entity = models.Usuario.query.get(id)
    if not entity:
        abort(404)
    entity = models.Usuario(
        nome=request.json['nome'],
        login=request.json['login'],
        password=request.json['password'],
        admin=request.json['admin'],
        id=id
    )
    try:
        db.session.merge(entity)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        abort(403)
    return '', 204


@app.route('/bios-setup-api/usuario/<int:id>', methods=['DELETE'])
def delete_usuario(id):
    entity = models.Usuario.query.get(id)
    if not entity:
        abort(404)
    db.session.delete(entity)
    db.session.commit()
    return '', 204


@app.route('/bios-setup-api/config-por-op/etapas/<int:id_placa_mae>/<int:id_versao_bios>', methods=['GET'])
def get_etapas_of_config_por_op(id_placa_mae, id_versao_bios):
    entities = db.session.query(models.Etapa) \
        .join(models.Configuracao) \
        .filter(models.Configuracao.id_placa_mae == id_placa_mae, models.Configuracao.id_codigo_bios == id_versao_bios) \
        .with_entities(models.Etapa.id, models.Etapa.descricao) \
        .distinct()

    return json.dumps(
        [dict(id_etapa=entity[0], descricao_etapa=entity[1]) for entity in entities])


@app.route('/bios-setup-api/config-por-op/instrucoes/<int:id_placa_mae>/<int:id_versao_bios>/<int:id_etapa>', methods=['GET'])
def get_instrucoes_of_config_por_op(id_placa_mae, id_versao_bios, id_etapa):
    entities = db.session.query(models.Configuracao) \
        .with_entities(models.Configuracao.descricao_instrucao, models.Configuracao.posicao) \
        .filter(models.Configuracao.id_placa_mae==id_placa_mae, models.Configuracao.id_codigo_bios==id_versao_bios, models.Configuracao.id_etapa==id_etapa)

    return json.dumps(
        [dict(descricao_instrucao=entity[0], posicao=entity[1]) for entity in entities])
