from typing import Optional, Dict, List

from pydantic import BaseModel, EmailStr, Field

class Request_Preguntas(BaseModel):

    sector : Optional[str] = ''
    segmento : Optional[str] = ''
    cliente : str
    solo_historicos : bool
    competidor : Optional[str] = ''
    sin_competidor: bool

    class Config:
        
        schema_extra = {
            "example": {
                "sector": "EMPAQUES",
                "segmento": "CLIENTES DESECHABLES",
                "cliente": "CARVAJAL",
                "solo_historicos": True,
                "competidor": "ACME Inc",
                "sin_competidor": False
            }
        }

class Request_Documento(BaseModel):

    datos_busqueda: Request_Preguntas
    preguntas_seleccionadas: List = []

    class Config:
        
        schema_extra = {
            "example": {
                "datos_busqueda":
                    {
                        "sector": "EMPAQUES",
                        "segmento": "CLIENTES DESECHABLES",
                        "cliente": "CARVAJAL",
                        "solo_historicos": True,
                        "competidor": "ACME Inc",
                        "sin_competidor": False
                    },
                "preguntas_seleccionadas": 
                    [
                        {
                            "_id": {
                                "$oid": "6189585cc869542b502ece92"
                            },
                            "Cliente": "CARVAJAL",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 1,
                            "Grupos": "1 (primeras)",
                            "tipo pregunta": "A la medida",
                            "Sector": "EMPAQUES",
                            "Segmento": "CLIENTES DESECHABLES",
                            "Categorias": "benchmark",
                            "Atributos": "n/a",
                            "sujeto": "n/a",
                            "CNC": "n/a",
                            "Preguntas": "¿Con qué proveedores de empaques desechables trabaja usted o su empresa actualmente?",
                            "Escala": "n/a",
                            "Tipo de escala": "n/a",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                                "$oid": "6189585cc869542b502ece93"
                            },
                            "Cliente": "CARVAJAL",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 2,
                            "Grupos": "1 (primeras)",
                            "tipo pregunta": "A la medida",
                            "Sector": "EMPAQUES",
                            "Segmento": "CLIENTES DESECHABLES",
                            "Categorias": "benchmark",
                            "Atributos": "n/a",
                            "sujeto": "n/a",
                            "CNC": "n/a",
                            "Preguntas": "¿Podría indicarme en qué orden se encuentran según el volumen de compras?",
                            "Escala": "SI",
                            "Tipo de escala": "e1",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                                "$oid": "6189585cc869542b502ece94"
                            },
                            "Cliente": "CARVAJAL",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 3,
                            "Grupos": "2 (segundas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "EMPAQUES",
                            "Segmento": "CLIENTES DESECHABLES",
                            "Categorias": "conceptos generales",
                            "Atributos": "calidad",
                            "sujeto": "cliente",
                            "CNC": "Calidad_Cliente",
                            "Preguntas": "¿Cómo evalúa la calidad en general de CARVAJAL?",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "SI"
                        },
                        {
                            "_id": {
                                "$oid": "6189585cc869542b502ece95"
                            },
                            "Cliente": "CARVAJAL",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 4,
                            "Grupos": "2 (segundas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "EMPAQUES",
                            "Segmento": "CLIENTES DESECHABLES",
                            "Categorias": "conceptos generales",
                            "Atributos": "calidad",
                            "sujeto": "competidor",
                            "CNC": "Calidad_Competidor",
                            "Preguntas": "¿Cómo evalúa la calidad en general de ACME Inc?",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                                "$oid": "6189585cc869542b502ece97"
                            },
                            "Cliente": "CARVAJAL",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 6,
                            "Grupos": "2 (segundas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "EMPAQUES",
                            "Segmento": "CLIENTES DESECHABLES",
                            "Categorias": "conceptos generales",
                            "Atributos": "precios",
                            "sujeto": "cliente",
                            "CNC": "Precios_Cliente",
                            "Preguntas": "¿Cómo califica los precios de los productos  que le provee CARVAJAL?",
                            "Escala": "SI",
                            "Tipo de escala": "mbbjama",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "618b1bff2b3f30d276cffe5c"
                            },
                            "Cliente": "CARVAJAL",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 10,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "EMPAQUES",
                            "Segmento": "CLIENTES DESECHABLES",
                            "Categorias": "imágenes",
                            "Atributos": "lider",
                            "sujeto": "cliente",
                            "CNC": "Cliente_Líder",
                            "Preguntas": "A continuación, voy a leer algunas afirmaciones, usted deberá decir (ESCALA). Cliente es líder",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "618b1bff2b3f30d276cffe5d"
                            },
                            "Cliente": "CARVAJAL",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 11,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "EMPAQUES",
                            "Segmento": "CLIENTES DESECHABLES",
                            "Categorias": "imágenes",
                            "Atributos": "interesa clientes",
                            "sujeto": "cliente",
                            "CNC": "Cliente_Interesa clientes",
                            "Preguntas": "A continuación, voy a leer algunas afirmaciones, usted deberá decir (ESCALA). Cliente Se interesa por sus CARVAJALs",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "618b1bff2b3f30d276cffe6b"
                            },
                            "Cliente": "CARVAJAL",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 25,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "EMPAQUES",
                            "Segmento": "CLIENTES DESECHABLES",
                            "Categorias": "imágenes",
                            "Atributos": "conservar medio ambiente",
                            "sujeto": "competidor",
                            "CNC": "Comeptidor_Medio ambiente",
                            "Preguntas": "Competidor Una empresa preocupada por la conservación del medio ambiente",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "618b1bff2b3f30d276cffe6c"
                            },
                            "Cliente": "CARVAJAL",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 26,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "EMPAQUES",
                            "Segmento": "CLIENTES DESECHABLES",
                            "Categorias": "imágenes",
                            "Atributos": "variedad de producto",
                            "sujeto": "cliente",
                            "CNC": "Cliente_Oferta productos",
                            "Preguntas": "Cliente Ofrece una variedad suficiente de productos",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "618b1bff2b3f30d276cffe6e"
                            },
                            "Cliente": "CARVAJAL",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 28,
                            "Grupos": "4 (cuartas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "EMPAQUES",
                            "Segmento": "CLIENTES DESECHABLES",
                            "Categorias": "lealtad",
                            "Atributos": "lealtad",
                            "sujeto": "cliente",
                            "CNC": "Leal_Cliente",
                            "Preguntas": "Se considera un CARVAJAL leal de CARVAJAL. Usted diría que está…",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "618b1bff2b3f30d276cffe6f"
                            },
                            "Cliente": "CARVAJAL",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 29,
                            "Grupos": "4 (cuartas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "EMPAQUES",
                            "Segmento": "CLIENTES DESECHABLES",
                            "Categorias": "lealtad",
                            "Atributos": "productos afectados",
                            "sujeto": "cliente",
                            "CNC": "Afectación productos_Cliente",
                            "Preguntas": "Le afectaría no tener los productos de CARVAJAL. Usted diría que está…",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "618b1bff2b3f30d276cffe70"
                            },
                            "Cliente": "CARVAJAL",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 30,
                            "Grupos": "5 (quintas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "EMPAQUES",
                            "Segmento": "CLIENTES DESECHABLES",
                            "Categorias": "comportamientos",
                            "Atributos": "recomendar",
                            "sujeto": "cliente",
                            "CNC": "Recomendar_Cliente",
                            "Preguntas": "¿Qué tan probable es que usted recomendara a CARVAJAL?",
                            "Escala": "SI",
                            "Tipo de escala": "epmpapppnp",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "618b1bff2b3f30d276cffe71"
                            },
                            "Cliente": "CARVAJAL",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 31,
                            "Grupos": "5 (quintas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "EMPAQUES",
                            "Segmento": "CLIENTES DESECHABLES",
                            "Categorias": "comportamientos",
                            "Atributos": "recomendar",
                            "sujeto": "competidor",
                            "CNC": "Recomendar_Competidor",
                            "Preguntas": "¿Qué tan probable es que usted recomendara a ACME Inc?",
                            "Escala": "SI",
                            "Tipo de escala": "epmpapppnp",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "618b1bff2b3f30d276cffe74"
                            },
                            "Cliente": "CARVAJAL",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 34,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "EMPAQUES",
                            "Segmento": "CLIENTES DESECHABLES",
                            "Categorias": "procesos",
                            "Atributos": "calificación producto",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "¿Cómo califica los productos de CARVAJAL?",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "SI"
                        },
                        {
                            "_id": {
                            "$oid": "618b1bff2b3f30d276cffe75"
                            },
                            "Cliente": "CARVAJAL",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 35,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "EMPAQUES",
                            "Segmento": "CLIENTES DESECHABLES",
                            "Categorias": "procesos",
                            "Atributos": "calificación producto",
                            "sujeto": "competidor",
                            "CNC": "n/a",
                            "Preguntas": "¿Cómo califica los productos de ACME Inc?",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "SI"
                        },
                        {
                            "_id": {
                            "$oid": "618b1bff2b3f30d276cffe57"
                            },
                            "Cliente": "CARVAJAL",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 5,
                            "Grupos": "7 Septimas",
                            "tipo pregunta": "Estandar",
                            "Sector": "EMPAQUES",
                            "Segmento": "CLIENTES DESECHABLES",
                            "Categorias": "survey for action",
                            "Atributos": "excelencia",
                            "sujeto": "cliente",
                            "CNC": "Falta_Cliente",
                            "Preguntas": "¿Qué le hace falta a CARVAJAL para ser excelente? ",
                            "Escala": "n/a",
                            "Tipo de escala": "n/a",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "618b1bff2b3f30d276cffe96"
                            },
                            "Cliente": "CARVAJAL",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 68,
                            "Grupos": "7 Septimas",
                            "tipo pregunta": "Estandar",
                            "Sector": "EMPAQUES",
                            "Segmento": "CLIENTES DESECHABLES",
                            "Categorias": "survey for action",
                            "Atributos": "fortalezas",
                            "sujeto": "cliente",
                            "CNC": "Fortalezas_Cliente",
                            "Preguntas": "¿Qué fortalezas o qué esta haciendo bien CARVAJAL?",
                            "Escala": "n/a",
                            "Tipo de escala": "n/a",
                            "Condicionamiento de formulario": "n/a"
                        }
                    ]
            }
        }
