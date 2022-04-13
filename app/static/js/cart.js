var cart = []
var globalcart = []
var present = false

function addToCart(id, name, cost, type){
    if (sessionStorage.cart !== undefined){
        cart = JSON.parse(sessionStorage.cart)
    }

    let cartItem = {id:id,name:name,cost:parseInt(cost), price:parseInt(cost),amount:1,type:type}
    
    for(var i=0; i<cart.length; i++){
        if (cart[i].id == cartItem.id && cart[i].type == cartItem.type){
            present = true
            cart[i].amount++            
            cart[i].price = cart[i].cost * cart[i].amount
        }
    }

    if (present == false){
        cart.push(cartItem)    
    }

    globalcart = JSON.stringify(cart)
    sessionStorage.setItem("cart", globalcart)
    
    console.log(cart)
    console.log(JSON.stringify(cart))


    present = false
    globalcart = []

    
    updateCart()
}


function openCart(){
    var cartContainer =  document.getElementById("cartContainer") 

    if(cartContainer.style.width === '0vw'){
        cartContainer.style.width = "25vw";
        cartContainer.style.display = "block";
    }else{
        cartContainer.style.width = "0vw";
        cartContainer.style.display = "none";
    }

    updateCart()
    
}

function updateCart(){

    var add = `<h6>Your Cart<h6>`
    var cartContainer =  document.getElementById("cartContainer") 
    
    if (sessionStorage.cart !== undefined){
        cart = JSON.parse(sessionStorage.cart)
        var total = 0
        document.getElementById("notifCountCart").innerHTML = cart.length

        for(var i=0; i<cart.length;i++){
            
            total = total + cart[i].price
            add = add + `
                    <div class="cartItemContainer" id="cartItemContainer${cart[i].id}">
                        <p style="margin: 0;text-align: right;"><i onclick="removefromCart(this,${cart[i].id})" class='bx bx-x' ></i></p>
                        <div>
                            <p class="cartItemContainerName">
                                <span class="cartItemContainername">${cart[i].name} </span>
                            </p>
                            <p class="cartItemContainerCount">
                            <input type="number" min=1 value="${cart[i].amount}" class="cartItemContainercount" onchange="cartChange(this,${cart[i].id})">
                            </p>
                            <p class="cartItemContainerPrice">
                                <span class="cartItemContainerID" id="priceOption${cart[i].id}">${formatMoney(cart[i].price)}</span>
                            </p>
                        </div>
                        <p class="cartItemContainerType">
                            <span class="cartItemContainertype " id="typeOption${cart[i].id}">${cart[i].type}</span>
                        </p>
                        
                    </div>
                
            ` 
        }
    }

    add = add + `</div>
        <hr style="margin: 20px 0px;">
        <div>
            <h6 style="margin: 20px;">Total: <span style="margin-left: 55%;">${formatMoney(total)}</span></h6>
            <a class="nav-link" href="http://localhost:8080/myprofile"><button onclick="placeOrder()" id="placeOrderButton">Place Order</button></a>
        <div>
    `
    cartContainer.innerHTML = add
}


window.addEventListener("load", (e)=>{
    // Create our number formatter.

    var currency = document.getElementsByClassName('money')

    for(var i=0; i< currency.length;i++){
        currency[i].innerHTML = formatMoney(currency[i].innerHTML)
    }

    document.getElementById('clickbait').click();
})

function formatMoney(val){
    var formatter = new Intl.NumberFormat('en-JM', {
        style: 'currency',
        currency: 'JMD',
    });

    return formatter.format(val)
}


function cartChange(e,id){
    
    var tid= 'typeOption'+ id
    type = document.getElementById(tid).innerHTML

    if (sessionStorage.cart !== undefined){
        cart = JSON.parse(sessionStorage.cart)

        for(var i=0; i<cart.length; i++){
            if (parseInt(cart[i].id) == parseInt(id) && cart[i].type == type){
                present = true                
                cart[i].amount = e.value
                cart[i].price = cart[i].cost * cart[i].amount

                var elid = "priceOption" + id
                document.getElementById(elid).innerHTML = cart[i].price 
            }
        }

        globalcart = JSON.stringify(cart)
        sessionStorage.setItem("cart", globalcart)     
        updateCart()   
    }    

}

function removefromCart(e,id){
    
    var tid= 'typeOption'+ id
    type = document.getElementById(tid).innerHTML

    var itemdiv= 'cartItemContainer'+ id
    document.getElementById(itemdiv).innerHTML = " "

    if (sessionStorage.cart !== undefined){
        cart = JSON.parse(sessionStorage.cart)

        for(var i=0; i<cart.length; i++){
            if (parseInt(cart[i].id) == parseInt(id) && cart[i].type == type){
                cart.splice(i, 1)
            }
        }

        globalcart = JSON.stringify(cart)
        sessionStorage.setItem("cart", globalcart)     
        updateCart()   
    }    

}



function placeOrder(){
    
    if (sessionStorage.cart !== undefined){
        console.log('push')
        cart = JSON.parse(sessionStorage.cart)
        $.ajax({
            data : JSON.stringify(cart),
            type: 'POST',
            url : '/placedorder'
        }) 
    }    

    sessionStorage. clear();
    cart = []
    cartContainer.innerHTML = `<h6>Empty Cart<h6>`
    document.getElementById("notifCountCart").innerHTML = " "


}


// $.ajax({
//     data : JSON.stringify(cart),
//     type: 'POST',
//     url : '/process'
// })


//  $.ajax('/process', {
    //     success: function (data, status, xhr) {// success callback function
    //         var test = data
            
    //          console.log(test)
    //     }
    //  });