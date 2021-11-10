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

async function main() {
    grupos = [];
    var root_url = "http://209.50.62.200:8080/obterner_preguntas";
    var parameters = sessionStorage.getItem('parameters');
    console.log(parameters);
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
            newDiv.className = "card boxshadow p-3 mb-3 bg-white rounded";
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
                    <h3><span class="verticalsector-dos"></span>&nbsp;&nbsp;&nbsp;${dataDiv[0].Categorias}</h3>`
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

enviar = () => {
    console.log(arrayCheckbox);

    let arrayJSON = dataGlobal.filter(element => {
        if (arrayCheckbox.includes(element._id.$oid)) {
            return element
        }
    });

    let dataRequest = {
        "datos_busqueda": parameters,
        "preguntas_seleccionadas": arrayJSON
    }
    var parameters = sessionStorage.getItem('parameters');
    console.log(dataRequest);
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
