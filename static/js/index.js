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
// jwt = response.jwt
// localStorage.setItem("token", jwt)

//Use token
// jwt = localStorage.getItem("token")

// Delete Venue
// const deleteSong = async () => {
//     const deleteButton = document.getElementById('delete-song');
  
//     const { id } = deleteButton.dataset;
  
//     const result = await fetch(`/songs/${id}`, {
//       method: 'DELETE'
//     });
  
//     if (result.status === 200) window.location.replace('/');
//   };

//Get token in URL
// https://dive-app.herokuapp.com/#access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhLamhZMXlYOGM0S2dRSHR1MUgzMSJ9.eyJpc3MiOiJodHRwczovL2Rldi1kYzdpOXF1MC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjI5ZjNjOTc2Mzg5ZGUwMDY5M2M3ZGQ5IiwiYXVkIjoiZGl2ZW11c2ljIiwiaWF0IjoxNjU1MjU5NzAxLCJleHAiOjE2NTUyNjY5MDEsImF6cCI6IjZUc3BtajBGUHlkd3pRb0FuSTY2WmRpb3FTZ09vSmNGIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6bXVzaWNpYW4tY3JlYXRlLXBhZ2UiLCJnZXQ6bXVzaWNpYW5zLWRldGFpbCIsInBvc3Q6ZWRpdC1tdXNpY2lhbiIsInBvc3Q6bXVzaWNpYW4iXX0.Lk7N8-RxGwbeIklW6YS8GPqG_soYQ8cn6odgAJY88DqcxEcsemb5Qt16dcRo78GReYMZV8ee4H_Y9KAIGpcJ9I0P5Xu_5FWacd4OSS27oMNr3k1cjoRs6W5z-oMgx22WjmWHmuHJGgkhH6_t6GT9w_l1-oyEOlTrbI_SMtX9W2LTg9vvCRjkAT0QKRkunbFN0Lrvw4CcGfMwcLRWDJIUjQIpu4iKXlCCTuYVeXB4YstShdHdpzD67hSBCJaBm2mxux1K34P0T9TuoA3Xqwv6uduPWoHTIy__UooEjGpHqnhca76SZaU3JAQFjLGh5yHkD6bmwu9v3QsZfFrvPzNzIQ&expires_in=7200&token_type=Bearer

// http://www.medivh.com?ename=right

// var str = 'http://xx.xx.xx.xx:8080/#/activate?token=eyJhbGciOiJIxxx'
// var url = new URL(str.replace('#/', ''))
// console.log(url.searchParams.get('token'))


var url=location.search;
var new_url = new NEW_URL(url.replace('#', ''))
console.log(new_url) 
 
// var ename;
 
// var Request = new Object();
 
// if(url.indexOf("?")!=-1)
 
// {
 
//        var str = url.substr(1);
 
//        strs= str.split("&");
 
//        for(var i=0;i<strs.length;i++)
 
//       {
//           Request[strs[i].split("=")[0]]=(strs[i].split("=")[1]);
//       }
 
// }
 
// ename = Request["ename"]; 
// var url=location.search;
 
// var access_token;
 
// var Request = new Object();
 
// if(url.indexOf("?")!=-1)
 
// {
 
//        var str = url.substr(1);
 
//        strs= str.split("&");
 
//        for(var i=0;i<strs.length;i++)
 
//       {
//           Request[strs[i].split("=")[0]]=(strs[i].split("=")[1]);
//       }
 
// }
 
// ename = Request["ename"]; 

