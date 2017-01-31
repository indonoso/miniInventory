server = "http://localhost:5000/";

function formTemplate(product, num_components) {
    return "<div class=\"panel panel-default\"> " +
        "<div class=\"panel-heading\" role=\"tab\" id=\"panel_" + num_components + "\">" +
            "<h4 class=\"panel-title\"> " +
                "<a id=\"panel_title_" + num_components + "\"role=\"button\" data-toggle=\"collapse\" data-parent=\"#components_list\" href=\"#body_" + num_components + "\" ></a>" +
            "</h4>" +
        "</div>" +
        "<div id=\"body_" + num_components + "\" class=\"panel-collapse collapse in\" role=\"tabpanel\" >" +
            "<div class=\"panel-body\">" +
                "<form id=\"component_" + num_components + "\" class=\"form-horizontal\" method=\"POST\" action=\"/add/component/" + product + "\" onsubmit=\"addComponent(this, " + num_components + "); return false;\">"
                + "<div class=\"form-group\">"
                    + "<label for=\"product_in_" + num_components + "\">Producto</label>"
                    + "<select id=\"product_in_" + num_components + "\" class=\"form-control\" onchange='loadUnit()'></select>" +
                "</div>"
                + "<div class=\"form-group\">"
                    + "<input type=\"number\" id=\"quantity_" + num_components + "\" class=\"form-control\" placeholder=\"Cantidad\">"
                    + "<label id=\"label_quantity_" + num_components + "\" for=\"quantity\"></label>" +
                "</div>"
            + "<div class=\"form-group\">"
                    + "<input type=\"number\" id=\"comment_" + num_components + "\" class=\"form-control\" placeholder=\"comment\">"
                    + "<label id=\"label_comment_" + num_components + "\" for=\"comment\"></label>" +
                "</div>"
                + "<input id=\"form_btn_"+ num_components+ "\"type=\"submit\" class=\"btn btn-primary\" value=\"Agregar\">" +
            "</form>"
            + "</div>" +
        "</div>";

}

function addComponent(oFormElement, number_component, product_name) {
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
            document.getElementById("body_" + number_component).classList.toggle("in");
            document.getElementById("panel_title_" + number_component ).innerHTML = document.getElementById("product_in").name;
            document.getElementById("form_btn_" + number_component).classList.remove("btn-primary");
            document.getElementById("form_btn_" + number_component).classList.add("btn-success");
            num_components += 1;
        }
    };
    return false;
}

function loadForm(div, product) {
    if (document.getElementById("component_" + num_components)) {
        document.getElementById("add_component").classList.remove("btn-primary")
        document.getElementById("add_component").classList.add("btn-danger")
    } else {
        document.getElementById(div).innerHTML += formTemplate(product, num_components);
        loadProducts();
        document.getElementById("add_component").classList.add("btn-primary")
        document.getElementById("add_component").classList.remove("btn-danger")

    }
}


function loadUnit() {
    var select_product = document.getElementById("product_out");
    var product_id = select_product.options[select_product.selectedIndex].value;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("label_quantity").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "/product/get_unit/" + product_id, true);
    xhttp.send();
}

function loadProducts() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("product_in").innerHTML = this.responseText;
        }
    };
    xhttp.open("GET", "/product/get_all_choices", true);
    xhttp.send();
}
