document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#following').addEventListener('click', hide_new_post);
    document.querySelector('#all_posts').addEventListener('click', show_new_post);

  });

  function hide_new_post() {
    document.querySelector('#new_post').style.display = 'none'
  }

  function show_new_post() {
    document.querySelector('#new_post').style.display = 'block'
  }