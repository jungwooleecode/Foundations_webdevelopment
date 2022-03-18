const eyecontainer=document.querySelector(".eye-container");
const noEyebtn=document.querySelector(".noEye");
const eyebtn=document.querySelector(".eye");

noEyebtn.addEventListener("click",() =>{
    eyecontainer.classList.add("active");
});

eyebtn.addEventListener("click",() =>{
    eyecontainer.classList.remove("active");
});