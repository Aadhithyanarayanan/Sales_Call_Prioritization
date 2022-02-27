        var menu = document.getElementById("menu");
        var sidebar = document.getElementsByClassName('sidebar');
        var nav = document.getElementsByTagName("nav");
        var container=document.getElementsByClassName("Container");
        var main_profiles=document.getElementsByClassName("Main_profiles");
        var main_prioritize=document.getElementsByClassName("Main_prioritize");
        var main_contact_us=document.getElementsByClassName("Main_contact_us");

        var pressed = 0;
        menu.onclick = function () {
            if (pressed % 2 == 1) {
                for (var i = 0; i < sidebar.length; i++)
                    sidebar[i].style.visibility = "visible";
                for (var i = 0; i < nav.length; i++)
                    nav[i].style.left = "15%";

                for (var i = 0; i < main_prioritize.length; i++){
                    main_profiles[i].style.left = "15%";
                    main_prioritize[i].style.left = "15%";
                    main_contact_us[i].style.left = "15%";

                
                }

                for(var i=0;i<container.length;i++){
                    container[i].style.width="1000px"; 
                }


            } 
            
            else {
                for (var i = 0; i < sidebar.length; i++)
                    sidebar[i].style.visibility = "collapse";
                for (var i = 0; i < nav.length; i++)
                    nav[i].style.left = "0%";
                for (var i = 0; i < main_prioritize.length; i++){
                    main_profiles[i].style.left = "0%";
                    main_prioritize[i].style.left = "0%";
                    main_contact_us[i].style.left = "0%";
                    
                }

                for(var i=0;i<container.length;i++){
                     container[i].style.width="1200px";
                }

            }
            pressed++;
        };