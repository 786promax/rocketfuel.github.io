function popsicle(ar){
    const int = ar.length

    return ar[int-1]
}



function darkmode(){
    
    const html = document.getElementById("Html")

    if (html.className == "dark"){
        html.className = ''
    }
    else{
        html.className = "dark"
    }

    const button = document.getElementById("darkmode-btn")

    if (button.innerHTML === `<img class="w-8" src="dark.svg">`){
        button.innerHTML = `<img class="w-8" src="light.svg">`
    }
    else{
        button.innerHTML = `<img class="w-8" src="dark.svg">`
    }
    
    const user = document.getElementById("user")
    const star = document.getElementById("star")
    const train = document.getElementById("train")
    if (popsicle(user.src.split('/')) == "user.svg"){
        user.src = "white_user.svg"
    }
    else{
        user.src = "user.svg"
    }


    if (popsicle(star.src.split('/')) == "star.svg"){
        star.src = "white_star.svg"
    }
    else{
        star.src = "star.svg"
    }


    if (popsicle(train.src.split('/')) == "train.svg"){
        train.src = "white_train.svg"
    }
    else{
        train.src = "train.svg"
    }

}