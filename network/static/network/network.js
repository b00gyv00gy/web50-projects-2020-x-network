document.addEventListener('DOMContentLoaded', function() {

    document.querySelectorAll("button").forEach(element => {
        
        element.addEventListener("click", function(){
            
            let post = element.closest("div").querySelector("textarea");
            post.removeAttribute("readonly");
            
            let btn = document.createElement("button");
            btn.innerHTML = "SAVE";
            post.appendChild(btn);
            btn.addEventListener("click", save_post())

        });
    });
})

function save_post(post_id){
    fetch(`/posts/${post_id}`, {
        method: 'PUT',
        body: JSON.stringify({
            content: post.value
        })
      });
}
