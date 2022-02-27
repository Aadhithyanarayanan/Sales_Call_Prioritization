        var main_profiles=document.getElementsByClassName("Main_profiles");
        var main_customer=document.getElementsByClassName("Main_customer");
        var main_leadquality=document.getElementsByClassName("Main_leadquality");

        var profiles=document.getElementById("profiles");
        var customer=document.getElementById("customer");
        var leadquality=document.getElementById("leadQuality");



        profiles.onclick=function(){
            for(i=0;i<main_profiles.length;i++){
                main_profiles[i].style.visibility="visible";
                main_customer[i].style.visibility="collapse";
                main_leadquality[i].style.visibility="collapse";
            }
            profiles.style.backgroundColor="#2b384e"
            customer.style.backgroundColor="#34425a"
            leadquality.style.backgroundColor="#34425a"
        }

        customer.onclick=function(){
            for(i=0;i<main_customer.length;i++){
                main_profiles[i].style.visibility="collapse";
                main_customer[i].style.visibility="visible";
                main_leadquality[i].style.visibility="collapse";
            }
            profiles.style.backgroundColor="#34425a"
            customer.style.backgroundColor="#2b384e"
            leadquality.style.backgroundColor="#34425a"
        }

        leadquality.onclick=function(){
            for(i=0;i<main_leadquality.length;i++){
                main_profiles[i].style.visibility="collapse";
                main_customer[i].style.visibility="collapse";
                main_leadquality[i].style.visibility="visible";
            }
            profiles.style.backgroundColor="#34425a"
            customer.style.backgroundColor="#34425a"
            leadquality.style.backgroundColor="#2b384e"
            }

        

        

        
