function formTemplate(product) {
    return "<form id=\"component\" action=\"/add/component/" + product + "\" method=\"POST\">"
        + "<div class=\"form-group\">"
        + "<label for=\"product_in\">Producto</label>"
        + "<select id=\"product_in\" class=\"form-control\" onchange='loadUnit()'></select></div>"
        + "<div class=\"form-group\">"
        + "<input type=\"number\" id=\"quantity\" class=\"form-control\" placeholder=\"Cantidad\">"
        + "<label id=\"label_quantity\" for=\"quantity\"></label></div>"
        + "<input type=\"submit\" class=\"btn btn-primary\" value=\"Agregar\"></form>";
    
}

function loadForm(div, product){
    if (document.getElementById("component")){
        // TODO error
    }else{
        document.getElementById(div).innerHTML = formTemplate(product);
        loadProducts();
    }
}


function loadUnit() {
    var select_product = document.getElementById("product_out");
    var product_id = select_product.options[select_product.selectedIndex].value;

      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
         document.getElementById("label_quantity").innerHTML = this.responseText;
        }
      };
      xhttp.open("GET", "/product/get_unit/" + product_id, true);
      xhttp.send();
}

function loadProducts() {
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
         document.getElementById("product_in").innerHTML = this.responseText;
        }
      };
      xhttp.open("GET", "/product/get_all_choices", true);
      xhttp.send();
}