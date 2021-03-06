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
                "sector": "Empaques",
                "segmento": "Clientes desechables",
                "cliente": "Carvajal",
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
                        "sector": "Empaques",
                        "segmento": "Clientes desechables",
                        "cliente": "Carvajal",
                        "solo_historicos": True,
                        "competidor": "ACME Inc",
                        "sin_competidor": False
                    },
                "preguntas_seleccionadas": 
                    [
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6249"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 1,
                            "Grupos": "1 (primeras)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "benchmark",
                            "Atributos": "n/a",
                            "sujeto": "n/a",
                            "CNC": "n/a",
                            "Preguntas": "??Con qu?? proveedores de empaques desechables trabaja usted o su empresa actualmente?",
                            "Escala": "n/a",
                            "Tipo de escala": "n/a",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c624a"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 2,
                            "Grupos": "1 (primeras)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "benchmark",
                            "Atributos": "n/a",
                            "sujeto": "n/a",
                            "CNC": "n/a",
                            "Preguntas": "??Podr??a indicarme en qu?? orden se encuentran seg??n el volumen de compras?",
                            "Escala": "SI",
                            "Tipo de escala": "e1",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c624b"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 3,
                            "Grupos": "2 (segundas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "conceptos generales",
                            "Atributos": "calidad",
                            "sujeto": "cliente",
                            "CNC": "Calidad_Cliente",
                            "Preguntas": "??C??mo eval??a la calidad en general de Carvajal?",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "SI"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c624c"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 4,
                            "Grupos": "2 (segundas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "conceptos generales",
                            "Atributos": "calidad",
                            "sujeto": "competidor",
                            "CNC": "Calidad_Competidor",
                            "Preguntas": "??C??mo eval??a la calidad en general de ACME Inc?",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c624e"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 6,
                            "Grupos": "2 (segundas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "conceptos generales",
                            "Atributos": "precios",
                            "sujeto": "cliente",
                            "CNC": "Precios_Cliente",
                            "Preguntas": "??C??mo califica los precios de los productos  que le provee Carvajal?",
                            "Escala": "SI",
                            "Tipo de escala": "mbbjama",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c624f"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 7,
                            "Grupos": "2 (segundas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "conceptos generales",
                            "Atributos": "precios",
                            "sujeto": "competidor",
                            "CNC": "Precios_Competidor",
                            "Preguntas": "??C??mo califica los precios de los productos  que le provee ACME Inc?",
                            "Escala": "SI",
                            "Tipo de escala": "mbbjama",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6250"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 8,
                            "Grupos": "2 (segundas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "conceptos generales",
                            "Atributos": "precio - beneficio",
                            "sujeto": "cliente",
                            "CNC": "Precios_Beneficios_Cliente",
                            "Preguntas": "Considerando la calidad general de los productos y servicios en relaci??n con los precios de Carvajal ??Usted dir??a que ofrece??? (E: Lea escala) beneficios por su dinero?",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6251"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 9,
                            "Grupos": "2 (segundas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "conceptos generales",
                            "Atributos": "precio - beneficio",
                            "sujeto": "cliente",
                            "CNC": "Precios_Beneficios_Competidor",
                            "Preguntas": "Considerando la calidad general de los productos y servicios en relaci??n con los precios de ACME Inc ??Usted dir??a que ofrece??? (E: Lea escala) beneficios por su dinero?",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6252"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 10,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "im??genes",
                            "Atributos": "lider",
                            "sujeto": "cliente",
                            "CNC": "Cliente_L??der",
                            "Preguntas": "A continuaci??n, voy a leer algunas afirmaciones, usted deber?? decir (ESCALA). Carvajal es l??der",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6253"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 11,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "im??genes",
                            "Atributos": "interesa clientes",
                            "sujeto": "cliente",
                            "CNC": "Cliente_Interesa clientes",
                            "Preguntas": "A continuaci??n, voy a leer algunas afirmaciones, usted deber?? decir (ESCALA). Carvajal Se interesa por sus clientes",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6254"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 12,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "im??genes",
                            "Atributos": "facilidad negocios",
                            "sujeto": "cliente",
                            "CNC": "Cliente_Facilidad negocios",
                            "Preguntas": "A continuaci??n, voy a leer algunas afirmaciones, usted deber?? decir (ESCALA). Con Carvajal es f??cil hacer negocios",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6255"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 13,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "im??genes",
                            "Atributos": "reputacion y prestigio",
                            "sujeto": "cliente",
                            "CNC": "Cliente_Reputaci??n y prestigio",
                            "Preguntas": "A continuaci??n, voy a leer algunas afirmaciones, usted deber?? decir (ESCALA). Carvajal tiene una excelente reputaci??n y prestigio",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6256"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 14,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "im??genes",
                            "Atributos": "crecimiento economico y profesional",
                            "sujeto": "cliente",
                            "CNC": "Cliente_Crecimiento econ??mico y profesional",
                            "Preguntas": "Carvajal Se interesa en ayudarle a crecer econ??mica y profesionalmente a su empresa",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6257"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 15,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "im??genes",
                            "Atributos": "crecimiento economico y profesional",
                            "sujeto": "competidor",
                            "CNC": "Competidor_Crecimiento econ??mico y profesional",
                            "Preguntas": "ACME Inc Se interesa en ayudarle a crecer econ??mica y profesionalmente a su empresa",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6258"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 16,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "im??genes",
                            "Atributos": "agil",
                            "sujeto": "cliente",
                            "CNC": "Cliente_??gil",
                            "Preguntas": "Carvajal Una empresa ??gil",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6259"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 17,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "im??genes",
                            "Atributos": "agil",
                            "sujeto": "competidor",
                            "CNC": "Competidor_??gil",
                            "Preguntas": "ACME Inc Una empresa ??gil",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c625a"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 18,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "im??genes",
                            "Atributos": "continuo mejoramiento",
                            "sujeto": "cliente",
                            "CNC": "Cliente_Continuo mejoramiento",
                            "Preguntas": "Carvajal Una empresa en continuo mejoramiento",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c625b"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 19,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "im??genes",
                            "Atributos": "continuo mejoramiento",
                            "sujeto": "competidor",
                            "CNC": "Competidor_Mejoramiento continuo",
                            "Preguntas": "ACME Inc Una empresa en continuo mejoramiento",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c625c"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 20,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "im??genes",
                            "Atributos": "innovador",
                            "sujeto": "cliente",
                            "CNC": "Cliente_Innovadora",
                            "Preguntas": "Carvajal Una empresa innovadora",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c625d"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 21,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "im??genes",
                            "Atributos": "innovador",
                            "sujeto": "competidor",
                            "CNC": "Competidor_Innovadora",
                            "Preguntas": "ACME Inc Una empresa innovadora",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c625e"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 22,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "im??genes",
                            "Atributos": "confianza",
                            "sujeto": "cliente",
                            "CNC": "Cliente_Confianza",
                            "Preguntas": "Carvajal Refleja una excelente confianza entre sus clientes",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c625f"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 23,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "im??genes",
                            "Atributos": "confianza",
                            "sujeto": "competidor",
                            "CNC": "Competidor_Confianza",
                            "Preguntas": "ACME Inc Refleja una excelente confianza entre sus clientes",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6260"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 24,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "im??genes",
                            "Atributos": "conservar medio ambiente",
                            "sujeto": "cliente",
                            "CNC": "Cliente_Conservaci??n medio ambiente",
                            "Preguntas": "Carvajal es una empresa preocupada por la conservaci??n del medio ambiente",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6261"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 25,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "im??genes",
                            "Atributos": "conservar medio ambiente",
                            "sujeto": "competidor",
                            "CNC": "Comeptidor_Medio ambiente",
                            "Preguntas": "ACME Inc es una empresa preocupada por la conservaci??n del medio ambiente",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6262"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 26,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "im??genes",
                            "Atributos": "variedad de producto",
                            "sujeto": "cliente",
                            "CNC": "Cliente_Oferta productos",
                            "Preguntas": "Carvajal Ofrece una variedad suficiente de productos",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6263"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 27,
                            "Grupos": "3 (terceras)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "im??genes",
                            "Atributos": "variedad de producto",
                            "sujeto": "competidor",
                            "CNC": "Competidor_Variedad productos",
                            "Preguntas": "ACME Inc Ofrece una variedad suficiente de productos",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6264"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 28,
                            "Grupos": "4 (cuartas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "lealtad",
                            "Atributos": "lealtad",
                            "sujeto": "cliente",
                            "CNC": "Leal_Cliente",
                            "Preguntas": "Se considera un cliente leal de Carvajal. Usted dir??a que est?????",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6265"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 29,
                            "Grupos": "4 (cuartas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "lealtad",
                            "Atributos": "productos afectados",
                            "sujeto": "cliente",
                            "CNC": "Afectaci??n productos_Cliente",
                            "Preguntas": "Le afectar??a no tener los productos de Carvajal. Usted dir??a que est?????",
                            "Escala": "SI",
                            "Tipo de escala": "taananddtd",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6266"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 30,
                            "Grupos": "5 (quintas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "comportamientos",
                            "Atributos": "recomendar",
                            "sujeto": "cliente",
                            "CNC": "Recomendar_Cliente",
                            "Preguntas": "??Qu?? tan probable es que usted recomendara a Carvajal?",
                            "Escala": "SI",
                            "Tipo de escala": "epmpapppnp",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6267"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 31,
                            "Grupos": "5 (quintas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "comportamientos",
                            "Atributos": "recomendar",
                            "sujeto": "competidor",
                            "CNC": "Recomendar_Competidor",
                            "Preguntas": "??Qu?? tan probable es que usted recomendara a ACME Inc?",
                            "Escala": "SI",
                            "Tipo de escala": "epmpapppnp",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6268"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 32,
                            "Grupos": "5 (quintas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "comportamientos",
                            "Atributos": "continuar",
                            "sujeto": "cliente",
                            "CNC": "Continuar_Cliente",
                            "Preguntas": "??Qu?? tan probable es que usted en su pr??xima compra de los productos que le ofrece Carvajal, decida adquirirlos con Carvajal? ",
                            "Escala": "SI",
                            "Tipo de escala": "epmpapppnp",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6269"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 33,
                            "Grupos": "5 (quintas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "comportamientos",
                            "Atributos": "continuar",
                            "sujeto": "competidor",
                            "CNC": "Continuar_Competidor",
                            "Preguntas": "??Qu?? tan probable es que usted en su pr??xima compra de los productos que le ofrece ACME Inc, decida adquirirlos con ACME Inc? ",
                            "Escala": "SI",
                            "Tipo de escala": "epmpapppnp",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c626a"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 34,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "calificaci??n producto",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo califica los productos de Carvajal?",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "SI"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c626b"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 35,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "calificaci??n producto",
                            "sujeto": "competidor",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo califica los productos de ACME Inc?",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "SI"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c626c"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 36,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "excelencia",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??Qu?? le hace falta a los productos de Carvajal para que usted los considere excelentes?",
                            "Escala": "n/a",
                            "Tipo de escala": "n/a",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c626d"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 37,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "proceso de compra de los productos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo califica el proceso de compra de los productos de Carvajal?",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "SI"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c626e"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 38,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "proceso de compra de los productos",
                            "sujeto": "competidor",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo califica el proceso de compra de los productos de ACME Inc?",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "SI"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c626f"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 39,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "proceso de compra de los productos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??Qu?? le hace falta al proceso de compra de los productos de Carvajal para que usted lo considere excelente?",
                            "Escala": "n/a",
                            "Tipo de escala": "n/a",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6270"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 40,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "proceso de compra de los productos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo eval??a el proceso de compra de Carvajal en cuanto a Los tiempos que le ofrecen para la entrega de los productos",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6271"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 41,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "proceso de compra de los productos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo eval??a el proceso de compra de Carvajal en cuanto a La capacidad de negociaci??n de los representantes de Carvajal Empaques",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6272"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 42,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "proceso de compra de los productos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo eval??a el proceso de compra de Carvajal en cuanto a La claridad de la informaci??n sobre las caracter??sticas de los producto",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6273"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 43,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "proceso de compra de los productos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo eval??a el proceso de compra de Carvajal en cuanto a La asesor??a que le brindan",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6274"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 44,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "proceso de compra de los productos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo eval??a el proceso de compra de Carvajal en cuanto a Los tiempos que ofrecen para la entrega de productos",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6275"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 45,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "representantes de ventas",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo califica en general a los representantes de ventas de Carvajal?",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "SI"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6276"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 46,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "representantes de ventas",
                            "sujeto": "competidor",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo califica en general a los representantes de ventas de ACME Inc?",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "SI"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6277"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 47,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "representantes de ventas",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??Qu?? le hace falta a los representantes de ventas de Carvajal para que usted los considere excelentes?",
                            "Escala": "n/a",
                            "Tipo de escala": "n/a",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6278"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 48,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "representantes de ventas",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo eval??a los representantes de ventas de Carvajal en cuanto a La actitud de servicio ",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6279"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 49,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "representantes de ventas",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo eval??a los representantes de ventas de Carvajal en cuanto a La facilidad para contactarlo",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c627a"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 50,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "representantes de ventas",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo eval??a los representantes de ventas de Carvajal en cuanto a La coordinaci??n entre las ??reas para atender sus requerimientos",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c627b"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 51,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "representantes de ventas",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo eval??a los representantes de ventas de Carvajal en cuanto a La frecuencia de visitas",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c627c"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 52,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "despachos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo califica los despachos de Carvajal?",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "SI"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c627d"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 53,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "despachos",
                            "sujeto": "competidor",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo califica los despachos de ACME Inc?",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "SI"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c627e"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 54,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "despachos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??Qu?? le hace falta a los despachos de Carvajal para que usted las considere excelentes?",
                            "Escala": "n/a",
                            "Tipo de escala": "n/a",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c627f"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 55,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "despachos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo eval??a los despachos de Carvajal en cuanto a La coordinaci??n de los despachos",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6280"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 56,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "despachos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo eval??a los despachos de Carvajal en cuanto a El cumplimiento en los tiempos de entrega de la mercader??a / mercanc??a",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6281"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 57,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "despachos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo eval??a los despachos de Carvajal en cuanto a El estado en que le entregan su mercader??a / mercancia",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6282"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 58,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "despachos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo eval??a los despachos de Carvajal en cuanto a La exactitud de los despachos",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6283"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 59,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "servicio de pedidos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo califica el servicio que le presta Carvajal ante pedidos de mercancia?",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "SI"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6284"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 60,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "servicio de pedidos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo califica el servicio que le presta ACME Inc ante pedidos de mercancia?",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "SI"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6285"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 61,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "servicio de pedidos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??Por qu?? raz??n dice usted que el servicio que le presta de Carvajal ante pedidos de mercader??a / mercancia es ??(E: Inserte respuesta anterior)?",
                            "Escala": "n/a",
                            "Tipo de escala": "n/a",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6286"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 62,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "atencion de pedidos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo eval??a la atenci??n a pedidos de Carvajal en cuanto a La facilidad para atender sus necesidades de mercader??a / mercancia",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6287"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 63,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "atencion de pedidos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo eval??a la atenci??n a pedidos de Carvajal en cuanto a La atenci??n a sus reclamos sobre la mercader??a / mercancia recibida",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6288"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 64,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "atencion de pedidos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo eval??a la atenci??n a pedidos de Carvajal en cuanto a El compromiso y la responsabilidad ante sus problemas",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c6289"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 65,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "atencion de pedidos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo eval??a la atenci??n a pedidos de Carvajal en cuanto a La preocupaci??n que muestran los funcionarios por resolverle de la mejor manera su problema",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c628a"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 66,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "atencion de pedidos",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??C??mo eval??a la atenci??n a pedidos de Carvajal en cuanto a La prontitud y exactitud para resolver sus problemas",
                            "Escala": "SI",
                            "Tipo de escala": "ebrm",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c628b"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 67,
                            "Grupos": "6 (sextas)",
                            "tipo pregunta": "A la medida",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "procesos",
                            "Atributos": "sugerencias",
                            "sujeto": "cliente",
                            "CNC": "n/a",
                            "Preguntas": "??Qu?? sugerencias tiene o qu?? cambios realizar??a en Carvajal?",
                            "Escala": "n/a",
                            "Tipo de escala": "n/a",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c624d"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 5,
                            "Grupos": "7 (septimas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "survey for action",
                            "Atributos": "excelencia",
                            "sujeto": "cliente",
                            "CNC": "Falta_Cliente",
                            "Preguntas": "??Qu?? le hace falta a Carvajal para ser excelente? ",
                            "Escala": "n/a",
                            "Tipo de escala": "n/a",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c628c"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 68,
                            "Grupos": "7 (septimas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "survey for action",
                            "Atributos": "fortalezas",
                            "sujeto": "cliente",
                            "CNC": "Fortalezas_Cliente",
                            "Preguntas": "??Qu?? fortalezas o qu?? esta haciendo bien Carvajal?",
                            "Escala": "n/a",
                            "Tipo de escala": "n/a",
                            "Condicionamiento de formulario": "n/a"
                        },
                        {
                            "_id": {
                            "$oid": "61965ab593aada07c51c628d"
                            },
                            "Cliente": "Carvajal",
                            "estudio": 1,
                            "Orden cuestionario pregunta": 69,
                            "Grupos": "7 (septimas)",
                            "tipo pregunta": "Estandar",
                            "Sector": "Empaques",
                            "Segmento": "Clientes desechables",
                            "Categorias": "survey for action",
                            "Atributos": "sugerencias",
                            "sujeto": "cliente",
                            "CNC": "Sugerencias_Cliente",
                            "Preguntas": "??Qu?? sugerencias tiene o qu?? cambios realizar??a en Carvajal?",
                            "Escala": "n/a",
                            "Tipo de escala": "n/a",
                            "Condicionamiento de formulario": "n/a"
                        }
                    ]
            }
        }
