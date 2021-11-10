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
                            "Tipo de escala": "E1",
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
                            "Tipo de escala": "EBRM",
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
                            "Tipo de escala": "EBRM",
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
                            "Tipo de escala": "MBBJAMA",
                            "Condicionamiento de formulario": "n/a"
                        }
                    ]
            }
        }
