
alert("Hello! I am an alert box!!");


console.log(products_json_id);
const products_json = JSON.parse(document.getElementById('products_json_id').textContent)
console.log(products_json)


function create_product_card(product) {
    // creating whole card
    const card_container = document.createElement('div');
    card_container.className = 'card col-3';

    const image = document.createElement('img');
    image.src = '/media/' + product.product_image;
    image.className = 'd-block w-100';
    image.alt = "Product Image";

    const card_body = document.createElement("div");
    card_body.className = "card-body";

    const title = document.createElement("h5");
    title.textContent = product.product_name;

    const card_text = document.createElement("p");
    card_text.className = "card-text";
    card_text.textContent =  product.product_description;

    const link = document.createElement("a");
    link.href = "#";
    link.className = "btn btn-primary mycart";
    link.textContent = "Add to cart";


    // appending created elelments to card container
    card_body.appendChild(title);    
    card_body.appendChild(card_text);    
    card_body.appendChild(link);
    card_container.appendChild(image);
    card_container.appendChild(card_body);
        

    return card_container;


}

const carouselInner = document.querySelector("#carousal_inner2");
const carousalIndicatorsButtons = document.querySelector("#carousel_indicators_buttons2");
// const carouselInner = document.getElementById('carousal_inner2');
// const carousalIndicatorsButtons = document.getElementById("carousel_indicators_buttons2")
console.log(carouselInner)
console.log(carousalIndicatorsButtons)
var slide_count =0

for (let index = 0; index < products_json.length; index++) {

    if (index % 4 ==0){
        console.log("in ",products_json,products_json[index].id);
        //buttons code
        slide_count +=1;
        const button = document.createElement("button");
        button.setAttribute("data-bs-target","#carouselExampleIndicators2");
        button.setAttribute("data-bs-slide-to",slide_count);
        button.setAttribute("aria-label", `Slide ${slide_count}`);

        //carousal item code
        var carousal_item = document.createElement("div");

        if (index ==0){
            button.className = "active";
            carousal_item.className = "carousel-item my-2 active";
            
        }//inner if
        else{
            carousal_item.className = "carousel-item my-2";
        }//else_closure

        carousalIndicatorsButtons.appendChild(button);

        // carousal_item.className = "carousel-item my-2 ";
        var carousal_item_row = document.createElement("div");
        }//outer if

        const product = products_json[index];
        const product_card = create_product_card(product);
        carousal_item_row.appendChild(product_card);


        if (index % 4 ==0){
        carousal_item.appendChild(carousal_item_row);
        carouselInner.appendChild(carousal_item);
        }



    
}


//code for cart

if(localStorage.getItem('cart') == null){
    var cart = {};
}
else{
    cart = JSON.parse(localStorage.getItem('cart'));
}

//jquery code
$('.mycart').click(function(){
    alert('add to cart this.id clicked');
    var clicked_pid = this.id.toString();
    if(cart[clicked_pid] != undefined){
        cart[clicked_pid] = cart[idstr] + 1;
    }

})