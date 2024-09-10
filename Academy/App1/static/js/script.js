function showsidebar()
{
    const sidebar=document.querySelector('.sidebar')
    sidebar.style.display='flex'
}
function hidesidebar()
{
    const sidebar=document.querySelector('.sidebar')
    sidebar.style.display='none'
}

//scroll function

function scrolltotop(){
    window.scroll({
        top:0,
        left:0,
        behavior:'smooth'
    })
}
function scrolltobottom(){
    window.scroll({
        top:document.body.scrollHeight,
        left:0,
        behavior:'smooth'
    })
}
function scrolltoabout()
	{
		document.querySelector('#about-id').scrollIntoView({
			behavior:'smooth'})
	}
function scrolltoreview()
	{
		document.querySelector('#review-id').scrollIntoView({
			behavior:'smooth'})
	}
function scrolltodonations()
    {
        document.querySelector('#donations-id').scrollIntoView({
            behavior:'smooth'})
    }

// document.addEventListener('keydown', function() {
// if (event.keyCode == 123) {
//     alert("You Can not Do This!");
//     return false;
// } else if (event.ctrlKey && event.shiftKey && event.keyCode == 73) {
//     alert("You Can not Do This!");
//     return false;
// } else if (event.ctrlKey && event.keyCode == 85) {
//     alert("You Can not Do This!");
//     return false;
// }
// }, false);

// if (document.addEventListener) {
// document.addEventListener('contextmenu', function(e) {
//     alert("You Can not Do This!");
//     e.preventDefault();
// }, false);
// } else {
// document.attachEvent('oncontextmenu', function() {
//     alert("You Can not Do This!");
//     window.event.returnValue = false;
// });
// }

$('.btn_nav').click(function() {
    // animate content
    $('.page__style').addClass('animate_content');
    $('.page__description').fadeOut(100).delay(2800).fadeIn();
  
    setTimeout(function() {
      $('.page__style').removeClass('animate_content');
    }, 3200);
  
    //remove fadeIn class after 1500ms
    setTimeout(function() {
      $('.page__style').removeClass('fadeIn');
    }, 1500);
  
  });
