
const urlInput = document.querySelector("#url");

document.querySelector("#siteMapButton").addEventListener("click", (e) => {
    e.preventDefault();
    redirect();
});

document.querySelector("#xmlButton").addEventListener("click", (e) => {
    e.preventDefault();
    download_xml();
});

function redirect() {
    var urlValue = urlInput.value;

    // Verificar se urlValue não está vazio
    if (urlValue.trim() !== '') {
        // Redirecionar para a URL correta
        window.location.href = "{% url 'mapGenerator:result' %}";
    } else {
        show_url_alert();
    }
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function download_xml() {
    var urlValue = urlInput.value;

    if (urlValue.trim() !== '') {
        hide_url_alert();
        // window.location.href = "{% url 'mapGenerator:download-xml' 'urlValue' %}".replace('urlValue', urlValue);

        // Create a new XMLHttpRequest object
        var xhr = new XMLHttpRequest();

        // Construct the URL with the parameter
        var requestUrl = '/download-xml?url=' + encodeURIComponent(urlValue);

        // Configure the request
        xhr.open('POST', requestUrl, true);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');

        // Retrieve the CSRF token
        var csrftoken = getCookie('csrftoken');

        // Include the CSRF token in the request headers
        xhr.setRequestHeader('X-CSRFToken', csrftoken);

        // Define the callback function for the response
        xhr.onload = function () {
            if (xhr.status === 200) {
                var blob = new Blob([xhr.responseText], { type: 'application/xml' });
                var link = document.createElement('a');
                link.href = window.URL.createObjectURL(blob);
                link.download = 'arquivo.xml';
                link.click();
            } else {
                console.log('Request failed. Status: ' + xhr.status);
            }
        };

        // Send the request
        xhr.send();
    } else {
        show_url_alert();
    }
}

function show_url_alert() {
    // Exibir popup de alerta
    var alertDiv = document.createElement('div');
    alertDiv.className = 'alert alert-danger';
    alertDiv.innerHTML = 'URL inválida! Por favor, insira uma URL válida.';

    var alertContainer = document.querySelector('#alertConteiner');
    alertContainer.innerHTML = ''; // Limpa o conteúdo atual da div
    alertContainer.appendChild(alertDiv);
    alertContainer.classList.remove('hidden');
}

function hide_url_alert() {
    var alertContainer = document.querySelector('#alertConteiner');
    alertContainer.innerHTML = ''; // Limpa o conteúdo atual da div
    alertContainer.classList.add('hidden');
}