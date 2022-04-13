window.addEventListener("load", (e)=>{
    // Create our number formatter.
    console.log('hi')
    var formatter = new Intl.NumberFormat('en-JM', {
        style: 'currency',
        currency: 'JMD',
    });

    var currency = document.getElementsByClassName('money')

    for(var i=0; i< currency.length;i++){
        console.log(currency[i].innerHTML)
        currency[i].innerHTML = formatter.format(currency[i].innerHTML)
    }


})


function addCocktail(){
    var itemTypeDiv = document.getElementById('itemTypeDiv')
    itemTypeDiv.style.display = "block";

    var itemDiscriptionDiv = document.getElementById('itemDiscriptionDiv')
    itemDiscriptionDiv.style.width= '95%';
    
    var itemPrice2Div = document.getElementById('itemPrice2Div')
    itemPrice2Div.style.display = "none";

    var itemAdditionalDetailsDiv = document.getElementById('itemAdditionalDetailsDiv')
    itemAdditionalDetailsDiv.style.display = "none";


    var itemPrice2 = document.getElementById('itemPrice2')
    itemPrice2.value = 0

    var itemAdditionalDetails = document.getElementById('itemAdditionalDetails')
    itemAdditionalDetails.value = " "

    


    activateLightBox()
    hideDeleteForm()
    

    document.getElementById('itemType')
    const $select = document.querySelector('#itemType').value = 'cocktail';
}


function addMizerSparkling(){

    var itemPrice1Div = document.getElementById('itemPrice1Div')
    itemPrice1Div.style.display = "block";

    var itemDiscriptionDiv = document.getElementById('itemDiscriptionDiv')
    itemDiscriptionDiv.style.display = "none";

    var itemPrice2Div = document.getElementById('itemPrice2Div')
    itemPrice2Div.style.display = "none";

    var itemAdditionalDetailsDiv = document.getElementById('itemAdditionalDetailsDiv')
    itemAdditionalDetailsDiv.style.display = "none";


    var itemDiscription = document.getElementById('itemDiscription')
    itemDiscription.value = " "

    var itemPrice2 = document.getElementById('itemPrice2')
    itemPrice2.value = 0

    var itemAdditionalDetails = document.getElementById('itemAdditionalDetails')
    itemAdditionalDetails.value = " "


    activateLightBox()
    hideDeleteForm()

    const $select = document.querySelector('#itemType').value = 'mixer';
}


function addWine(){

    var itemDiscriptionDiv = document.getElementById('itemDiscriptionDiv')
    itemDiscriptionDiv.style.display = "none"; 

    var itemAdditionalDetailsDiv = document.getElementById('itemAdditionalDetailsDiv')
    itemAdditionalDetailsDiv.style.display = "none";

    var itemDiscription = document.getElementById('itemDiscription')
    itemDiscription.value = " "

    var itemAdditionalDetails = document.getElementById('itemAdditionalDetails')
    itemAdditionalDetails.value = " "

    activateLightBox()
    hideDeleteForm()

    const $select = document.querySelector('#itemType').value = 'red-wine';
}


function bodyContainer(){

    var revert = document.getElementById('uploadForm')

    for(var i=0; i< revert.children.length;i++){
        revert.children[i].style.display="block"        
    }
    
    var formContainer = document.getElementsByClassName('lightbox')[0]
    formContainer.style.display = "none";

    $('#uploadForm')[0].reset()
    $('#deleteItemForm')[0].reset()
        
}

function deleteItem(id){
    activateLightBox()
    showDeleteForm()

    var deleter = document.getElementById('delete')
    deleter.value = id
}

function updateItem(){
    activateLightBox()
}


function hideDeleteForm(){
    var uploadForm = document.getElementById('uploadForm')
    uploadForm.style.display = "block";
    var deleteItemForm = document.getElementById('deleteItemForm')
    deleteItemForm.style.display = "none";
}

function showDeleteForm(){
    var uploadForm = document.getElementById('uploadForm')
    uploadForm.style.display = "none";
    var deleteItemForm = document.getElementById('deleteItemForm')
    deleteItemForm.style.display = "block";
}


function activateLightBox(){
    var formContainer = document.getElementsByClassName('lightbox')[0]
    formContainer.style.display = "block";
}


function updateReservation(id){ 
    activateLightBox()
    hideDeleteForm()

    var uploadForm = document.getElementById('updateid')
    uploadForm.style.display = "none";
    uploadForm.value = id
}