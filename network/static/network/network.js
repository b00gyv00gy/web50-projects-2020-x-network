document.addEventListener('DOMContentLoaded', function() {

    document.querySelectorAll(".edit").forEach(element => {
        
        element.addEventListener("click", function(){
            
            let post = element.closest("div");
            post.querySelector("textarea").removeAttribute("readonly");
            
            let btn = document.createElement("button");
            btn.className = "save";
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
        let like_btn = post.querySelector('.like')
        let num_of_likes = post.querySelector('.num_of_likes')

        fetch(`/count_likes/${post.id}`)
            .then((response) => {
                return response.json();
            })
            .then(data => {
                num_of_likes.innerHTML = data.num_of_likes 
                
                if (data.like_status){
                    like_btn.innerHTML = 'UNLIKE'
                }
                else{
                    like_btn.innerHTML = 'LIKE'
                }
            });
        
        
                
        element.addEventListener("click", function(){
            
            

            fetch(`/like_unlike_post/${post.id}`)
            if (like_btn.innerHTML== 'LIKE') {
                like_btn.innerHTML = 'UNLIKE'
                num_of_likes.innerHTML++
                }
            else{
                like_btn.innerHTML = 'LIKE'
                num_of_likes.innerHTML--
            }

            });
        });
        
        if (document.getElementById("username") != false && document.querySelector(".follow_btn") != false){
        
            try {
                let follow_btn = document.querySelector(".follow_btn")
                let username = document.getElementById("username").innerHTML
                fetch(`/follow_status/${username}`)
                .then((response) => {
                return response.json();
                })
                .then(data => {
                    
                    if (data.hide_follow_btn){
                        follow_btn.style.display = 'none'
                    }
                    if (data.follow_status){
                        follow_btn.innerHTML = "UNFOLLOW"
                        
                    }
                    else{
                        follow_btn.innerHTML = "FOLLOW"
                    }
                });

                follow_btn.addEventListener("click", function(){
            
                    let num_of_followers = document.getElementById("num_of_followers")
                    
                    fetch(`/follow/${username}`)
                    if (follow_btn.innerHTML == 'FOLLOW') {
                        follow_btn.innerHTML = 'UNFOLLOW'
                        num_of_followers.innerHTML++
                        }
                    else{
                        follow_btn.innerHTML = 'FOLLOW'
                        num_of_followers.innerHTML--
                    }
                
                });
            } catch (error) {
            
            }    
        }
    
})


