        var main_profiles=document.getElementsByClassName("Main_profiles");
        var main_prioritize=document.getElementsByClassName("Main_prioritize");
        var main_leadquality=document.getElementsByClassName("Main_leadquality");

        var main_contact_us=document.getElementsByClassName("Main_contact_us");
        var profiles=document.getElementById("profiles");
        var prioritize=document.getElementById("prioritize");
        var contact_us=document.getElementById("contact_us");
        var leadquality=document.getElementById("leadQuality");



        profiles.onclick=function(){
            for(i=0;i<main_profiles.length;i++){
                main_profiles[i].style.visibility="visible";
                main_prioritize[i].style.visibility="collapse";
                main_leadquality[i].style.visibility="collapse";
                main_contact_us[i].style.visibility="collapse";
            }
            profiles.style.backgroundColor="#2b384e"
            prioritize.style.backgroundColor="#34425a"
            contact_us.style.backgroundColor="#34425a"
            leadquality.style.backgroundColor="#34425a"
        }

        prioritize.onclick=function(){
            for(i=0;i<main_prioritize.length;i++){
                main_profiles[i].style.visibility="collapse";
                main_prioritize[i].style.visibility="visible";
                main_leadquality[i].style.visibility="collapse";
                main_contact_us[i].style.visibility="collapse";
            }
            profiles.style.backgroundColor="#34425a"
            prioritize.style.backgroundColor="#2b384e"
            contact_us.style.backgroundColor="#34425a"
            leadquality.style.backgroundColor="#34425a"
        }

        leadquality.onclick=function(){
            for(i=0;i<main_leadquality.length;i++){
                main_profiles[i].style.visibility="collapse";
                main_prioritize[i].style.visibility="collapse";
                main_contact_us[i].style.visibility="collapse";
                main_leadquality[i].style.visibility="visible";
            }
            profiles.style.backgroundColor="#34425a"
            prioritize.style.backgroundColor="#34425a"
            contact_us.style.backgroundColor="#34425a"
            leadquality.style.backgroundColor="#2b384e"
            }

        contact_us.onclick=function(){
            for(i=0;i<main_contact_us.length;i++){
                main_profiles[i].style.visibility="collapse";
                main_prioritize[i].style.visibility="collapse";
                main_leadquality[i].style.visibility="collapse";
                main_contact_us[i].style.visibility="visible";
                
            }
            profiles.style.backgroundColor="#34425a"
            prioritize.style.backgroundColor="#34425a"
            contact_us.style.backgroundColor="#2b384e"
            leadquality.style.backgroundColor="#34425a"
        }

        

        
