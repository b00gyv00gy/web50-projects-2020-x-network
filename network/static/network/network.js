
document.addEventListener('DOMContentLoaded', function() {

    document.querySelectorAll(".edit").forEach(element => {
        
        element.addEventListener("click", function(){
            
            let post = element.closest("div");
            post.querySelector("textarea").removeAttribute("readonly");
            
            let btn = document.createElement("button");
            btn.innerHTML = "SAVE";
            post.appendChild(btn);
            
            btn.addEventListener("click", function(){
                fetch(`/save_post/${post.id}`, {
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
        
        let post = element.closest("div")

        fetch(`/count_likes/${post.id}`)
            .then((response) => {
                return response.json();
            })
            .then(data => {
                post.childNodes[5].innerHTML = data.num_of_likes
                
                if (data.like_status){
                    post.childNodes[7].innerHTML = 'UNLIKE'
                }
                else{
                    post.childNodes[7].innerHTML = 'LIKE'
                }
            });
        
        
                
        element.addEventListener("click", function(){

            fetch(`/like_unlike_post/${post.id}`)
            if (post.childNodes[7].innerHTML == 'LIKE') {
                post.childNodes[7].innerHTML = 'UNLIKE'
                post.childNodes[5].innerHTML++
                }
            else{
                post.childNodes[7].innerHTML = 'LIKE'
                post.childNodes[5].innerHTML--
            }

            });
        });
    
})



