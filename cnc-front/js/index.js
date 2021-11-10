// Autocompletar selects
$(document).ready(() => {
    AutocompletarSegmentos();
    AutocompletarSectores();
    AutocompletarClientes();
});

// PETICIÓN PARA LLENAR EL SELECT DE SEGMENTOS
function AutocompletarSegmentos() {
    $.ajax({
        type: "GET",
        url: "http://209.50.62.200:8080/get_segmentos",
    })
        .done((data, textStatus, jqXHR) => {
            const segmentos = data;
            var opcionesHTML = `<option value="">SELECCIONE UNA OPCIÓN</option>`;
            segmentos.forEach(function (segmento, index) {
                //   console.log(`${index} : ${segmento}`);
                opcionesHTML += `<option value="${segmento}">${segmento}</option>`;
            });
            document.getElementById("isegmento").innerHTML = opcionesHTML;
        })
        .fail((jqXHR, textStatus, errorThrow) => {
            console.error(errorThrow);
        });
}

// PETICIÓN PARA LLENAR EL SELECT DE SECTORES
function AutocompletarSectores() {
    $.ajax({
        type: "GET",
        url: "http://209.50.62.200:8080/get_sectores",
    })
        .done((data, textStatus, jqXHR) => {
            const sectores = data;
            var opcionesHTML = `<option value="">SELECCIONE UNA OPCIÓN</option>`;
            sectores.forEach(function (sector, index) {
                //   console.log(`${index} : ${sector}`);
                opcionesHTML += `<option value="${sector}">${sector}</option>`;
            });
            document.getElementById("isector").innerHTML = opcionesHTML;
        })
        .fail((jqXHR, textStatus, errorThrow) => {
            console.error(errorThrow);
        });
}

// PETICIÓN PARA LLENAR EL SELECT DE CLIENTES
function AutocompletarClientes() {
    $.ajax({
        type: "GET",
        url: "http://209.50.62.200:8080/get_clientes",
    })
        .done((data, textStatus, jqXHR) => {
            const clientes = data;
            var opcionesHTML = ``;
            clientes.forEach(function (cliente, index) {
                //   console.log(`${index} : ${sector}`);
                opcionesHTML += `<option value="${cliente}">${cliente}</option>`;
            });
            document.getElementById("listClientes").innerHTML = opcionesHTML;
        })
        .fail((jqXHR, textStatus, errorThrow) => {
            console.error(errorThrow);
        });
}

enviar = () => {
    let historico = false
    let sincompetidor = false
    let competidor = document.getElementById('icompetidor').value;
    if(document.getElementById('historico').checked){
        historico = true
    }
    if(document.getElementById('sincompetidor').checked){
        sincompetidor = true
        competidor = "";
    }
    var parameters = {
        "sector": document.getElementById('isector').value,
        "segmento": document.getElementById('isegmento').value,
        "cliente": document.getElementById('icliente').value,
        "solo_historicos": historico,
        "competidor": competidor,
        "sin_competidor": sincompetidor
    };
    sessionStorage.setItem("parameters", JSON.stringify(parameters));
    window.location.href = "./preguntas.html";
}

competidor = (input) =>{
    let inputCompetidor = document.getElementById('icompetidor');
    if(input.checked){
        inputCompetidor.disabled = true;
        inputCompetidor.value = '';
    }else{
        inputCompetidor.disabled = false;
    }
}