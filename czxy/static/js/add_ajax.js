function ajax_request() {
    var xmlhttp;
    if (window.XMLHttpRequest) {
        //code for IE7+ , Firfox, Chrome, Opera, Safari
        xmlhttp = new XMLHttpRequest();
    } else {
        //code for IE6, IE5
        xmlhttp = new ActiveXObject('Microsoft.XMLHTTP');
    }

    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState === 4 && xmlhttp.state === 200) {
            document.getElementById('result_ajax').innerText = xmlhttp.responseText;
        }
    }
    var c = document.getElementById('c').value;
    var d = document.getElementById('d').value;
    xmlhttp.open('get', '/app/add_ajax/', true);
    xmlhttp.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    xmlhttp.send(null);
}