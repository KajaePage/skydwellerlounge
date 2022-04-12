function show(id){
    var test = document.getElementById(id)
    if(test.style.display === "block"){
        test.style.display = "none"
    }else{
        test.style.display = "block"
    }
}


function animatecarticon(id){
        document.getElementById(id).style.height = "25px"
}

function removeanimatecarticon(id){
        document.getElementById(id).style.height = "0px"
}