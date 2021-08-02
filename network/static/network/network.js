document.addEventListener('DOMContentLoaded', function() {

    let buttons = document.querySelectorAll("button")
    
    buttons.forEach(element => {
        
        element.addEventListener("click", function(){
            
            element.closest("div").querySelector("textarea").removeAttribute("readonly")

        });
    });
})
