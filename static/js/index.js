//Selectors
let header = document.querySelector('.header');
let headerSongpage = document.querySelector('.header-songpage');
let hamburgerMenu = document.querySelector('.hamburger-menu');
// var bgaudiocount = 0;

window.addEventListener('scroll', function () {
    let windowPosition = window.scrollY > 0;
    header.classList.toggle('active', windowPosition)
})

hamburgerMenu.addEventListener('click', function () {
    header.classList.toggle('menu-open');
})

hamburgerMenu.addEventListener('click', function () {
    headerSongpage.classList.toggle('menu-open');
})

// function bgplay(){
//     var audio = document.getElementById("bgaudio");
//     audio.play();
    // ++bgaudiocount;
    // if(bgaudiocount % 2 == 1){
    //     document.getElementById(bgaudio).play();
    // }else{
    //     document.getElementById(bgaudio).pause();
    // }
// }

//Store tokens
jwt = response.jwt
localStorage.setItem("token", jwt)

//Use token
jwt = localStorage.getItem("token")

// Delete Venue
// const deleteSong = async () => {
//     const deleteButton = document.getElementById('delete-song');
  
//     const { id } = deleteButton.dataset;
  
//     const result = await fetch(`/songs/${id}`, {
//       method: 'DELETE'
//     });
  
//     if (result.status === 200) window.location.replace('/');
//   };
