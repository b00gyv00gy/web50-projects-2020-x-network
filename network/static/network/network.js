
document.addEventListener('DOMContentLoaded', function() {

    document.querySelectorAll(".edit").forEach(element => {
        
        element.addEventListener("click", function(){
            
            let post = element.closest("div");
            post.querySelector("textarea").removeAttribute("readonly");
            
            let btn = document.createElement("button");
            btn.innerHTML = "SAVE";
            post.appendChild(btn);
            
            btn.addEventListener("click", function(){
                fetch(`/posts/${post.id}`, {
                    method: 'PUT',
                    body: JSON.stringify({
                        content: post.querySelector("textarea").value
                    })
                  });
                btn.remove();
            }
            )
        });
    });

    document.querySelectorAll(".like").forEach(element => {
        
        let post = element.closest("div");
        
        
        element.addEventListener("click", function(){

            fetch(`/like_post/${post.id}`, {
                method: 'PUT',
                body: JSON.stringify({
                    post: post.id
                })
              });
        });
    });
    
    //fetch(`/likes/`)
    //.then(response => response.json())
    //.then(like => {
    //
    //})
})



