function addComponent(oFormElement) {
    var xhr = new XMLHttpRequest();
    xhr.onload = function () {
        alert(xhr.responseText);
    }
    xhr.open(oFormElement.method, oFormElement.action, true);
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    var product_in = encodeURIComponent(document.getElementById("product_in").value);
    var quantity = encodeURIComponent(document.getElementById("quantity").value);
    var comment = encodeURIComponent(document.getElementById("comment").value);

    xhr.send("product_in=" + product_in + "&quantity=" + quantity + "&comment=" + comment);
    xhr.onreadystatechange = function () {
        if (this.readyState == 2 && this.status == 201) {
            console.log("Success")
        }
    };
    return false;
}


function loadUnit() {
    var select_product = document.getElementById("product_out");
    var product_id = select_product.options[select_product.selectedIndex].value;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("add_on_product_in").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "/product/get_unit/" + product_id, true);
    xhttp.send();
}


function getSelectedValue(selection_combo){
    var e = document.getElementById(selection_combo);
    return [e.options[e.selectedIndex].value, e.options[e.selectedIndex].text]
}