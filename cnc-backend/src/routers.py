from fastapi import APIRouter, Query
from fastapi.responses import FileResponse
from typing import Optional

import io
from datetime import datetime


from .dependencies import(
    get_clientes,
    get_sectores,
    get_segmentos,
    obtener_preguntas,
    generar_documento_word
)

from .models import (
    Request_Preguntas,
    Request_Documento
)

router = APIRouter()

@router.get("/get_clientes")
async def obtener_clientes():
    return get_clientes()

@router.get("/get_sectores")
async def obtener_sectores():
    return get_sectores()

@router.get("/get_segmentos")
async def obtener_segmentos():
    return get_segmentos()

@router.post("/obterner_preguntas")
async def obterner_preguntas(request: Request_Preguntas):

    response = obtener_preguntas(request.sector, request.segmento, request.cliente, request.competidor, request.solo_historicos, request.sin_competidor)
    return response

@router.post("/procesar_preguntas")
async def procesar_preguntas_generar_word(request: Request_Documento):

    print(request.datos_busqueda)
    print(request.datos_busqueda.segmento)
    print(len(request.preguntas_seleccionadas))
    print(request.preguntas_seleccionadas[0])

    documento_word = generar_documento_word(request.datos_busqueda, request.preguntas_seleccionadas)
    
    
    return documento_word