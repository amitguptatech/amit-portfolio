const roles = [

"Technical Lead",
"Java Backend Developer",
"DevOps Engineer",
"AWS Cloud Engineer",
"Solution Designer"

];

let roleIndex = 0;
let charIndex = 0;

const typingElement =
document.getElementById("typing");

function typeEffect(){

if(charIndex <
roles[roleIndex].length){

typingElement.textContent +=
roles[roleIndex].charAt(charIndex);

charIndex++;

setTimeout(typeEffect,100);

}else{

setTimeout(eraseEffect,1500);

}

}

function eraseEffect(){

if(charIndex > 0){

typingElement.textContent =
roles[roleIndex].substring(
0,
charIndex - 1
);

charIndex--;

setTimeout(eraseEffect,50);

}else{

roleIndex++;

if(roleIndex >= roles.length){
roleIndex = 0;
}

setTimeout(typeEffect,500);

}

}

typeEffect();
