
console.log("Hii their ")
const alertBox= document.getElementById('alert-box')
const imageBox= document.getElementById('image-box')
const form= document.getElementById('p-form')

const name= document.getElementById('id_name ')
const image= document.getElementById('id_image')

const csrf = document.getElementById('csrfmiddlewaretoken')
const url= ""

image.addEventListener('change',()=>{
    const img_data = image.files[0]
    const url = URL.createObjectURL(img_data)
    console.log(url)
}

)

console.log(csrf)