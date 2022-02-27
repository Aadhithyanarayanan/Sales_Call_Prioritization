var main_profiles=document.getElementsByClassName("Main_profiles");
var main_prioritize=document.getElementsByClassName("Main_prioritize");
var profiles=document.getElementById("profiles");
var prioritize=document.getElementById("prioritize");




profiles.onclick=function(){
    for(i=0;i<main_profiles.length;i++){
        main_profiles[i].style.visibility="visible";
        main_prioritize[i].style.visibility="collapse";
     
    }
    profiles.style.backgroundColor="#2b384e"
    prioritize.style.backgroundColor="#34425a"
   
}

prioritize.onclick=function(){
    for(i=0;i<main_prioritize.length;i++){
        main_profiles[i].style.visibility="collapse";
        main_prioritize[i].style.visibility="visible";
    }
    profiles.style.backgroundColor="#34425a"
    prioritize.style.backgroundColor="#2b384e"
}




