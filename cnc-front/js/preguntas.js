// Autocompletar selects
// VARIABLES
var grupos = [];
var dataGlobal;
var arrayCheckbox = new Array();
// FIN VARIABLES

async function get_response(input, url) {
    try {
        const response = await fetch(url,
            {
                method: 'POST',
                body: JSON.stringify(input), // data can be `string` or {object}!
                headers: {
                    'Content-Type': 'application/json'
                }
            });
        const result = await response.json();
        return result;
    } catch (error) {
        console.error(error);
    }
}

async function get_document(input, url) {
    try {
        const response = await fetch(url,
            {
                method: 'POST',
                body: JSON.stringify(input), // data can be `string` or {object}!
                headers: {
                    'Content-Type': 'application/json',
                    'responseType': 'arraybuffer'
                }
            });
        const result = await response.blob();
        return result;
    } catch (error) {
        console.error(error);
    }
}

async function main() {
    grupos = [];
    var root_url = "http://localhost:8080/obterner_preguntas";
    var parameters = sessionStorage.getItem('parameters');
    // estructura parameters
    // var parameters = {
    //     "sector": "EMPAQUES",
    //     "segmento": "CLIENTES DESECHABLES",
    //     "cliente": "CARVAJAL",
    //     "solo_historicos": true,
    //     "competidor": "ACME Inc",
    //     "sin_competidor": false
    // };
    var data = await get_response(JSON.parse(parameters), root_url);
    dataGlobal = data;
    data.forEach(element => {
        if (!grupos.includes(element.Categorias)) {
            // Añadir categoria al array para no repetir la creación del div contenedor
            grupos.push(element.Categorias);
            // crear div contenedor (card)
            var newDiv = document.createElement("div");
            newDiv.className = "card boxshadow p-3 mb-3 bg-white rounded scrollbar";
            newDiv.setAttribute('id', `div_${element.Categorias}`);
            newDiv.style.height = "300px";
            newDiv.style.overflowY = "scroll";
            // añadir al div "divPregunta"
            document.getElementById('divPreguntas').appendChild(newDiv);
        }
    });
    // Llamar a la funcion crearBody donde genera el cuerpo de todos los <div class="card">
    crearBody(dataGlobal, grupos);
}

crearBody = (data, grupos) => {
    grupos.forEach(grupo => {
        let dataDiv = data.filter(element => {
            if (element.Categorias == grupo) {
                return element;
            }
        });
        let cadenaHTML = "";
        cadenaHTML += `<div class="card-body">`;
        cadenaHTML += `
                    <div class="row d-flex">
                        <div class="col">
                            <h3><span class="verticalsector-dos"></span>&nbsp;&nbsp;&nbsp;${dataDiv[0].Categorias}</h3>
                        </div>
                        <div class="col">
                            <button class="btn btn-primary btn-lg" style="float: right;">Nueva pregunta</button>
                        </div>
                    </div>
                    `;
        dataDiv.forEach((element, index) => {
            cadenaHTML += `
                    <div class="form-check">
                        <input class="form-check-input preguntas" type="checkbox" value="${element._id.$oid}" name="preguntas[]" onchange="almacenar(this)">
                        <label class="form-check-label">
                            ${element.Preguntas}
                        </label>
                    </div>
                    `;
            if (index < dataDiv.length - 1) {
                cadenaHTML += `<hr style ="width: 90%">`;
            }
        })
        cadenaHTML += `</div>`;
        let idDiv = "div_" + dataDiv[0].Categorias
        document.getElementById(idDiv).innerHTML = cadenaHTML;

    })
}

main();

enviar = async () => {
    let arrayJSON = dataGlobal.filter(element => {
        if (arrayCheckbox.includes(element._id.$oid)) {
            return element
        }
    });
    // debugger;
    var parameters = JSON.parse(sessionStorage.getItem('parameters'));

    let dataRequest = {
        "datos_busqueda": parameters,
        "preguntas_seleccionadas": arrayJSON
    }

    // let test = JSON.parse(dataRequest);

    // console.log(test);

    let headers = {
        'Content-Type': 'application/json'
    }

    var root_url = "http://localhost:8080/procesar_preguntas";
    // var data = await get_document(JSON.parse(dataRequest), root_url);
    var data = await get_document(dataRequest, root_url);
    var link = document.createElement('a');
    link.href = window.URL.createObjectURL(data);
    link.download = "myFileName.docx";
    link.click();
}

// CHECKBOX
almacenar = (input) => {
    if (input.checked) {
        arrayCheckbox.push(input.value);
    } else {
        if (arrayCheckbox.includes(input.value)) {
            var i = arrayCheckbox.indexOf(input.value);
            arrayCheckbox.splice(i, 1);
        }
    }
}
        // END CHECKBOX
