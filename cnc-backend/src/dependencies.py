import json
from bson import json_util


from .settings import (
    preguntas
)

def parse_json(data):
    return json.loads(json_util.dumps(data))

def get_sectores():
    sectores = list(preguntas.distinct("Sector"))
    return sectores

def get_segmentos():
    segmentos = list(preguntas.distinct("Segmento"))
    return segmentos

def get_clientes():
    clientes = list(preguntas.distinct("Cliente"))
    return clientes

def incluir_cliente_preguntas(preguntas, cliente):

    for pregunta in preguntas:

        if 'cliente' in pregunta['Preguntas']:
                
                pregunta['Preguntas'] = pregunta['Preguntas'].replace('cliente', cliente)

    return preguntas

def incluir_competidor_preguntas(preguntas, competidor):

    for pregunta in preguntas:

        if 'competidor' in pregunta['Preguntas']:
                
            pregunta['Preguntas'] = pregunta['Preguntas'].replace('competidor', competidor)

    return preguntas

def excluir_preguntas_competidor(preguntas):

    result = []

    for pregunta in preguntas:

        if 'competidor' not in pregunta['Preguntas']:
                
            result.append(pregunta)  

    return result


def obtener_preguntas(sector  = '', segmento = '', cliente = '', competidor = '', solo_historicos = True, sin_competidor = False):
    """
    print('-'*10)
    print('sector: ' + sector)
    print('segmento: ' + segmento)
    print('cliente: ' + cliente)
    print('competidor: ' + competidor)
    print('solo_historicos: ' + str(solo_historicos))
    print('sin_competidor: ' + str(sin_competidor))
    print('-'*10)
    """
    ###############################################################################################
    if sector and segmento and solo_historicos:

        #print('sector and segmento and solo_historico')

        preguntas_busqueda = list(preguntas.aggregate([
            { "$match":{
                    "$and": [
                        {"Sector": { "$eq" : sector}},
                        {"Segmento" : { "$eq" : segmento}},
                        {"Cliente" : { "$eq" : cliente}}
                    ]
                }
            },
            { "$sort": { "Grupos" : 1 }}
        ]))

        preguntas_busqueda = parse_json(preguntas_busqueda)

        preguntas_busqueda = incluir_cliente_preguntas(preguntas_busqueda, cliente)
        
        if sin_competidor:
            preguntas_busqueda = excluir_preguntas_competidor(preguntas_busqueda)
        else: 
            preguntas_busqueda = incluir_competidor_preguntas(preguntas_busqueda, competidor)

        return preguntas_busqueda

    ###############################################################################################
    if sector and solo_historicos:

        #print('sector and solo_historico')

        preguntas_busqueda = list(preguntas.aggregate([
            { "$match":{
                    "$and": [
                        {"Sector": { "$eq" : sector}},
                        {"Cliente" : { "$eq" : cliente}}
                    ]
                }
            },
            { "$sort": { "Grupos" : 1 }}
        ]))

        preguntas_busqueda = parse_json(preguntas_busqueda)

        preguntas_busqueda = incluir_cliente_preguntas(preguntas_busqueda, cliente)

        if sin_competidor:
            preguntas_busqueda = excluir_preguntas_competidor(preguntas_busqueda)
        else: 
            preguntas_busqueda = incluir_competidor_preguntas(preguntas_busqueda, competidor)

        return preguntas_busqueda

    ###############################################################################################
    if segmento and solo_historicos:

        #print('segmento and solo_historico')

        preguntas_busqueda = list(preguntas.aggregate([
            { "$match":{
                    "$and": [
                        {"Segmento" : { "$eq" : segmento}},
                        {"Cliente" : { "$eq" : cliente}}
                    ]
                }
            },
            { "$sort": { "Grupos" : 1 }}
        ]))

        preguntas_busqueda = parse_json(preguntas_busqueda)

        preguntas_busqueda = incluir_cliente_preguntas(preguntas_busqueda, cliente)

        if sin_competidor:
            preguntas_busqueda = excluir_preguntas_competidor(preguntas_busqueda)
        else: 
            preguntas_busqueda = incluir_competidor_preguntas(preguntas_busqueda, competidor)

        return preguntas_busqueda

    ###############################################################################################
    if sector and segmento:

        #print('sector and segmento')

        preguntas_busqueda = list(preguntas.aggregate([
            { "$match":{
                    "$and": [
                        {"Sector": { "$eq" : sector}},
                        {"Segmento" : { "$eq" : segmento}}
                    ]
                }
            },
            { "$sort": { "Grupos" : 1 }}
        ]))

        preguntas_busqueda = parse_json(preguntas_busqueda)

        preguntas_busqueda = incluir_cliente_preguntas(preguntas_busqueda, cliente)

        if sin_competidor:
            preguntas_busqueda = excluir_preguntas_competidor(preguntas_busqueda)
        else: 
            preguntas_busqueda = incluir_competidor_preguntas(preguntas_busqueda, competidor)

        return preguntas_busqueda

    ###############################################################################################
    if sector:

        #print('sector')

        preguntas_busqueda = list(preguntas.aggregate([
            { "$match":{
                    "$and": [
                        {"Sector": { "$eq" : sector}}
                    ]
                }
            },
            { "$sort": { "Grupos" : 1 }}
        ]))

        preguntas_busqueda = parse_json(preguntas_busqueda)

        preguntas_busqueda = incluir_cliente_preguntas(preguntas_busqueda, cliente)

        if sin_competidor:
            preguntas_busqueda = excluir_preguntas_competidor(preguntas_busqueda)
        else: 
            preguntas_busqueda = incluir_competidor_preguntas(preguntas_busqueda, competidor)

        return preguntas_busqueda

    ###############################################################################################
    if segmento:

        #print('segmento')

        preguntas_busqueda = list(preguntas.aggregate([
            { "$match":{
                    "$and": [
                        {"Segmento" : { "$eq" : segmento}}
                    ]
                }
            },
            { "$sort": { "Grupos" : 1 }}
        ]))

        preguntas_busqueda = parse_json(preguntas_busqueda)

        preguntas_busqueda = incluir_cliente_preguntas(preguntas_busqueda, cliente)

        if sin_competidor:
            preguntas_busqueda = excluir_preguntas_competidor(preguntas_busqueda)
        else: 
            preguntas_busqueda = incluir_competidor_preguntas(preguntas_busqueda, competidor)

        return preguntas_busqueda


def generar_documento_word(metadatos, preguntas_seleccionadas):

    pass
