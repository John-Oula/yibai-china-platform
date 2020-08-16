


var start_time;
var end_time;
 var coverImgSrc = '../static/coverImages/';
 var userImgSrc = '../static/profile_pics/';
 var videoSrc = '../static/videos/';

function popover(msg,statusType){
  if (statusType == 'success'){
    statusType = 'green'
  }
  else if (statusType == 'error')
    statusType = '#e74525'
  $('.flash-msg').text(msg);
  $('.flash-msg').css('color',statusType);

  $(".flash-msg").animate({marginTop: "30px"});
  $('.navbar-brand').css('zIndex','0');
  $('.flash-msg').slideDown(function() {

    setTimeout(function() {

        $('.flash-msg').slideUp();
        $(".flash-msg").animate({marginTop: "0px"});
        $('.navbar-brand').css('zIndex','0');
        $('.navbar-brand').css('zIndex','100');
    }, 2000);


});

}

document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');

  var calendar = new FullCalendar.Calendar(calendarEl, {
    plugins: [ 'interaction', 'dayGrid', 'timeGrid','bootstrap' ,'interactionPlugin'],

    select: function( selectionInfo ){
       start_time = selectionInfo.startStr;
      document.getElementById('start-time').value = new Date(start_time).valueOf();
       end_time = selectionInfo.endStr;
      document.getElementById('end-time').value = new Date(end_time).valueOf();

    },
    dateClick: function(info){},
    longPressDelay:'1000',
    defaultTimedEventDuration: '01:45:00',
    forceEventDuration: true,
    themeSystem: 'bootstrap',
    defaultView: 'dayGridMonth',
    defaultDate: Date.now(),
    navLinks: true,
    selectable: true,
    selectMirror: true,
    unselectAuto: true,
    nowIndicator: true,
    editable: true,
    eventBackgroundColor: '#E74525',
    eventBorderColor: '#E74525',
    eventTextColor: 'white',
    eventTimeFormat:{
      hour: 'numeric',
      minute:'2-digit',
      meridiem: false,

    },

    header: {
      left: 'prev,next today',
      center: 'title',

      right: 'dayGridMonth,timeGridWeek,timeGridDay'
    },
    height: 650,

    slotDuration: '00:05' ,
    allDayDefault: false,

    displayEventEnd: true,
  });


  calendar.render();

});




$(function(){

$('.btn-add').click(function(){
    $('.wrapper:first').clone().appendTo('.series-div');
});

});

$(document).ready(function(){
  $("#addclass").click(function(){
    $("button#addclass")
        .after("<div class\"row\"  > <form action='' method='POST'><input name='title' class='input_class' style='font-family: Josefin Sans,sans-serif;background-color: #E74525;color:white;margin-top:10px;width: 200px;border-style: none' type='text'></form> </div>");
  });
  });

function myFunction() {
  var x = document.getElementById("myDIV");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

$('#play-btn').on('click', function () {
    wavesurfer.play();
    $('#pause-btn').css('display','flex')
    $('#play-btn').css('display','none')
    });
$('#pause-btn').on('click', function () {
    wavesurfer.pause();
    $('#play-btn').css('display','flex')
    $('#pause-btn').css('display','none')
    });

$(document).ready(function(){
$('.like-btn').click(function(e){
  e.preventDefault();

  var likeURL = $(this).attr("data-href");


  req = $.ajax({
    url:likeURL,
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")
      popover('Log in to Like the video','error')

    }

  });
  req.done(function(data){
    $('.likes').text(data.likes);
    $('#video-likes').text(data.likes);
    $('.like-btn').css("display","none");
    $('#unlike-btn').css("display","flex");
  })


})

  });



$(document).ready(function(){
  $('#unlike-btn').click(function(e){
  e.preventDefault();
  var unlikeURL = $(this).attr("data-href");


  req = $.ajax({
    url:unlikeURL,
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
  req.done(function(data){
    $('.likes').text(data.likes);
    $('#video-likes').text(data.likes);
    $('.like-btn').css("display","flex");
    $('#unlike-btn').css("display","none");

  })


})
  });


function updateText(word,verb){
  word.text(verb)
}


$(document).ready(function(){
$('#main').on('click','.click-book',function(e){
  e.preventDefault();

  var bookURL = $(this).attr("data-href");


  req = $.ajax({
    url:bookURL,
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")
      popover('Login to Book a seat','error')

    }

  });
  req.done(function(data){
    popover('Booked successfully','green')
    $('.click-book').css("display","none");
    $('.click-unbook').css("display","flex");
  })


})
$('#main').on('click','.click-unbook',function(e){
  e.preventDefault();

  var unbookURL = $(this).attr("data-href");


  req = $.ajax({
    url:unbookURL,
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
  req.done(function(data){
    $('.click-book').css("display","flex");
    $('.click-unbook').css("display","none");
  })


})



  });


function openCity(evt, cityName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the button that opened the tab
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " none";
}

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}



function Event(new_event){
  alert(new_event.toString())
  return new_event
}

$(document).ready(function(){
$('#follow').click(function(e){
  e.preventDefault();

  var followURL = $(this).attr("data-href");
  var username = $('#user-username').text()


  req = $.ajax({
    url:followURL,
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      popover('Log in to follow '+username+'','red');

      console.log(error)
      console.log("error")

    }

  });
  req.done(function(data){
    popover('You are now following '+username+'','green');
    $('#followers-count').text(data.followers);
    $('#user-followers').text(data.followers);
    popover('You are now following '+username+'');
    $('#follow').css("display","none");
    $('#unfollow').css("display","inline-block");
  })


})
$('#unfollow').click(function(e){
  e.preventDefault();

  var unfollowURL = $(this).attr("data-href");


  req = $.ajax({
    url:unfollowURL,
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
  req.done(function(data){
    $('#followers-count').text(data.followers);
    $('#user-followers').text(data.followers);
    $('#follow').css("display","inline-block");
    $('#unfollow').css("display","none");
  })


})

  });

$(document).ready(function(){
  $('#sessions-btn').click(function(e){
  e.preventDefault();
    var sessionURL = $(this).attr("data-href");

  req = $.ajax({
    url:sessionURL,
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
  req.done(function(data){
    $('#feed-content').css('display','none');
$('#session-content').css('display','block');
});


});
$('#posts-btn').click(function(e){
  e.preventDefault();
      var postsURL = $(this).attr("data-href");

  req = $.ajax({
    url:postsURL,
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
  req.done(function(data){
$('#feed-content').css('display','block');
$('#session-content').css('display','none');
});
  });
  });

$(document).ready(function(){
  $('.live-list').on('click','#live-card',function(e){
  e.preventDefault();
    var liveUrl = $(this).attr("data-href");
    var userImgUrl = '../static/profile_pics/';
    var userUrl = '/userDetails?username=';
    var coverImgUrl = '../static/coverImages/';
    var bookUrl = '/book/';
    var unbookUrl = '/unbook/';

  req = $.ajax({
    url:liveUrl,
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
  req.done(function(data){
    $('.live-list').css('display','none');
$('.live-details').css('display','block');
$('#profile-btn').attr('data-href',userUrl+data.host);
$('.live-profile-pic-wrapper').attr('data-href',userUrl+data.host);
$('.live-title').html(data.title);
$('#live-startTime').html(data.startTime);
$('#live-endTime').html(data.endTime);
$('#live-date').html(data.date);
$('#live-description').html(data.description);
$('img.live-img').attr('src',coverImgUrl+data.coverImage);
$('img#profilepic').attr('src',userImgUrl+data.userImg);
$('.click-book').attr('data-href',bookUrl+data.id);
$('.click-unbook').attr('data-href',unbookUrl+data.id);
$('#live-username').html(data.host);
$('.profile').css('display','none');
$('#user-profile').css('display','none');
      $('.checkout').css('display','none')
});


});

  });
$('#posts-btn').click(function(e){
  e.preventDefault();
      var postsURL = $(this).attr("data-href");

  req = $.ajax({
    url:postsURL,
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
  req.done(function(data){
$('#feed-content').css('display','block');
$('#session-content').css('display','none');
});
  });
$(document).ready(function(){
  $('.live').click(function(e){
  e.preventDefault();
  var liveUrl= '/liveDetails?liveId=';
  var userUrl = '/userDetails?username='

  req = $.ajax({
    url:'/liveSession',
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
  req.done(function(data){
    var obj = data.result;
    $('.live-list').empty();
    $.each(obj, function(key,value) {


      $('.live-list').append('<card class="card shadow-sm" id="live-card" data-href="'+liveUrl+value.id+'"> <card > <div class="live-img-wrapper"><img class="live-img" src="../static/coverImages/'+value.coverImg+'" alt=""></div> <div class="live-profile-pic-wrapper click-pro-pic"  data-href="'+userUrl+value.host+'"><span><a  class="user-profile-pic border-light" href="#"><img id="profilepic"  src="../static/profile_pics/'+ value.userImg +'" alt=""></a></span> </div><div class="p-2 row no-gutters"><span class="live-info col-8 flex-content flex-column no-gutters"><span class="live-title">'+ value.title +'</span><span class="">Hosted by:'+ value.host +' </span><span class="">Category:'+ value.category +'</span><span class=""> </span></span>  <span class="live-info col-4 flex-content flex-column no-gutters">           <span class="text-right">'+ value.startTime + '-'+ value.endTime +'</span><span class="text-right">'+ value.date +'</span>  <div class="circle-icon text-right text-center mt-2  p-2 shadow-sm"> <img class="rounded-circle" src="../static/share.svg" alt=""> </div> </span> </div> </card> </card>');

});
$('#live').css('display','block');
$('.live-list').css('display','block');
$('.live-details').css('display','none');
$('.profile').css('display','none');
$('.video-details').css('display','none');
$('.upload-list').css('display','none');
$('#user-profile').css('display','none');
$('.checkout').css('display','none')
  });



});



  });

$(document).ready(function(){
  $('.profile-nav').click(function(e){
  e.preventDefault();
  $('#user-profile').css('display','block');
  $('.upload-list').css('display','none');
  $('#live').css('display','none');
$('.live-list').css('display','none');
$('.live-details').css('display','none');
$('.profile').css('display','none');
$('.video-details').css('display','none');
$('#create-course').css('display','none');
$('#course-update').css('display','none');
$('#live-update').css('display','none');
$('.checkout').css('display','none')





});

$('#posts-btn').click(function(e){
  e.preventDefault();
      var postsURL = $(this).attr("data-href");

  req = $.ajax({
    url:postsURL,
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
  req.done(function(data){
$('#feed-content').css('display','block');
$('#session-content').css('display','none');
});
  });
  });


$(document).ready(function(){

  $('.home-icon').click(function(e){
  e.preventDefault();
  var arg = 'videoId=';
  var videoUrl = '/videoDetails?'+arg;
  var userUrl = '/userDetails?username='

  req = $.ajax({
    url:'/videos',
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
  req.done(function(data){
    var obj = data.result;
    $('.upload-list').empty();
    $.each(obj, function(key,value) {


      $('.upload-list').append('<div class="thumb-wrapper" data-href="'+videoUrl+ value.id +'"><li><a  class="video"   video-id="'+ value.id +'" href="#"><img class="video-feed" src="../static/profile_pics/'+ value.userImg +'" alt=""></a></li></div><div class="video-info"><div class="row no-gutters"><div class="col-2 col-sm-2 col-md-2 no-gutters">     <div class="profile-pic-wrapper click-pro-pic"  data-href=" '+userUrl+ value.username +'">     <span><a  class="user-profile-pic"   user-id="" href="#"><img id="profilepic"  src="../static/profile_pics/'+ value.userImg +'" alt=""></a></span> </div> </div><div class="col no-gutters"><div class="inner-info"> <div class="flex-fill flex-column">    <h6>'+ value.title +'</h6>     <div class="upload-username">'+ value.username +'</div>     <span class="upload-username">'+ value.category +'</span> <span>     <p class="likes-comments"  class="text-justify text-left " data-likes="">     <span>'+ value.likes +'</span>     <img     src="../static/heart.png" alt="" width="16">     <span>'+ value.comments +'</span>     <img  src="../static/comment.svg" alt="" width="16"> </p> </span></div>          </div> </div></div></div>');

});
$('#live').css('display','none');
$('.live-list').css('display','none');
$('.profile').css('display','none');
$('.video-details').css('display','none');
$('.upload-list').css('display','block');
$('#user-profile').css('display','none');
$('.checkout').css('display','none')
  });


});


  });



function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginRight = "250px";
    $('#main').css('display','none');
    $('.navbar-brand').css('display','none');
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginRight= "0";
    document.body.style.backgroundColor = "white";
    $('#main').css('display','block');
        $('.navbar-brand').css('display','block');


}


function openLeftNav() {
    document.getElementById("leftSidenav").style.width = "80%";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
    $('#main').css('display','none');
    $('.navbar-brand').css('display','none');
}

function closeLeftNav() {
    document.getElementById("leftSidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.body.style.backgroundColor = "white";
        $('#main').css('display','block');
        $('.navbar-brand').css('display','block');

}



$(document).ready(function(){
        $('.upload-list').on("click",'.thumb-wrapper',function(e){
  e.preventDefault();
    var url = $(this).attr("data-href");
    var videoSrc = "../static/videos/";
    var userImgSrc = "../static/profile_pics/";
    var userUrl = "/userDetails?username=";
    var courseUrl = "/editSeries?series_id=";
    var currency = "￥";
    var coverImgUrl = '../static/coverImages/';

  req = $.ajax({
    url:url,
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
  req.done(function(data){
    var obj  = data.result;
    $('#episode').empty();
            if (obj.isSeries === true){

              $('#episode-tab').css('display','block');

                    $.each(obj.episode, function(key,value) {
            $('#episode').append('<div class="card shadow-sm click-episode" data-href="/getEpisode?episode_id='+value.episodeId +'" ><div class="p-2"><span><img src="../static/play.svg" alt="" width="12"><span id="episode-title" class="mr-2 ml-5">'+value.subtitle+'</span><span id="episode-duration"></span></span></div></div>')
         });
        }
            else if (obj.isSeries === false){

              $('#episode-tab').css('display','none');

            }
        if (obj.type == 'video'){
                  $('video').attr("src",videoSrc + obj.videoRef);
                  $('video').css('display','block');
        $('.video-js').attr("src",videoSrc + obj.videoRef);
          $('.controls').css('display','none');
          $('video').css('display','block');
          $('.course-img').css('display','none');
        }
        else if (obj.type == 'audio'){

          $('#audiofile').attr("audioFile",obj.videoRef);
          $('.controls').css('display','block');
          $('video').css('display','none');
          $('.course-img').css('display','block');
          $('.course-img').attr("src",coverImgUrl+ obj.coverImg);

        }
        else if (obj.videoRef == null){
          $('.course-img').attr("src",coverImgUrl+ obj.coverImg);
          $('.controls').css('display','none');
          $('.course-img').css('display','block');
          $('video').css('display','none');
        }

        if (obj.price == null){
          $('#video-price').css('display','none');
          $('.addCart').css('display','none');
          $('#buy').css('display','none');
        }

        $('.upload-list').css('display','none');
        $('.video-details').css('display','block');
        $('.addCart').attr('data-href','/addCart?upload_id='+obj.id);
        $('.like-btn').attr('data-href','/like/video'+obj.id);
        $('#unlike-btn').attr('data-href','/unlike/video'+obj.id);

        if (obj.hasLiked == true){
          $('#unlike-btn').css('display','flex');

          $('.like-btn').css('display','none');
        }
        else if (obj.hasLiked == false){
          $('.like-btn').css('display','flex');

          $('#unlike-btn').css('display','none');
        }



        $('.profile-pic-wrapper').attr("data-href",userUrl+obj.username);
        $('#buy').attr("data-href",courseUrl+obj.id);
        $('#video-title').html(obj.title);
        $('#video-author').html(obj.username);
        $('#video-likes').html(obj.likes);
        $('#video-comments').html(obj.comments);
        $('#video-description').html(obj.description);
        $('#video-description img').css('width','100%');
        $('#video-price').html(currency + obj.price);
        $('#video-price').css("fontSize","17px");
        $('img#profilepic').attr("src",userImgSrc + obj.userImg);
        $('#user-profile').css('display','none');
        $('.checkout').css('display','none')



});
});

      $('#main').on("click",".click-pro-pic",function(e){
  e.preventDefault();
    var url = $(this).attr("data-href");
    var videoSrc = "../static/videos/";
    var userImgSrc = "../static/profile_pics/";
    var currency = "￥";
    var followUrl = "/follow";
    var unfollowUrl = "/unfollow";
    var userUrl = "/userDetails?username=";

  req = $.ajax({
    url:url,
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
  req.done(function(data){

        $('.upload-list').css('display','none');
        $('.profile').css('display','block');
        $('#book-schedule-btn').attr('data-href',userUrl+data.username);
        $('#unfollow').attr('data-href',unfollowUrl+"/"+data.username);
         $('#follow').attr('data-href',followUrl+"/"+data.username);
        if (data.Isfollowing === true){

                  $('#unfollow').css('display','inline-block');
                  $('#follow').css('display','none');


        }


        else{


                  $('#follow').css('display','inline-block');
                  $('#unfollow').css('display','none');


        }


        $('#user-username').html(data.username);
        $('#user-videos').html(data.videos);
        $('#user-followers').html(data.followers);
        $('#user-live-sessions').html(data.liveSessions);
        $('#user-introduction').html(data.description);
        $('img#profilepic').attr("src",userImgSrc + data.userImage);
        $('#user-profile').css('display','none');
        $('#live').css('display','none');
        $('.video-details').css('display','none');
        $('.checkout').css('display','none');

});


});
      $('.video-details').on("click",".click-episode",function(e){
  e.preventDefault();
    var url = $(this).attr("data-href");
    var videoSrc = "../static/videos/";
    var userImgSrc = "../static/profile_pics/";
    var currency = "￥";
    var followUrl = "/follow";
    var unfollowUrl = "/unfollow";

  req = $.ajax({
    url:url,
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
  req.done(function(data){
    var obj  = data.result;
            if (obj.type == 'video'){
                  $('video').attr("src",videoSrc + obj.video);
                  $('video').css('display','block');
        $('.video-js').attr("src",videoSrc + obj.video);
          $('.audio').css('display','none');
          $('video').css('display','block');
          $('.course-img').css('display','none');
        }
        else if (obj.type == 'audio'){
          $('source').attr("src",videoSrc + obj.video);
          $('.audio').css('display','block');
          $('video').css('display','none');
          $('.course-img').css('display','block');

        }
        else if (obj.videoRef == null){
          $('.course-img').attr("src",coverImgSrc+ obj.coverImg);
          $('.audio').css('display','none');
          $('.course-img').css('display','block');
          $('video').css('display','none');
        }

        $('.upload-list').css('display','none');
        $('.profile').css('display','none');

        $('#user-profile').css('display','none');
        $('#video-description').text(obj.description);
        $('.checkout').css('display','none')

});


});



      $('#schedule-create').on("click",function(e){
        e.preventDefault();
        closeNav()
            $('.schedule').css('display','block');
        $(".calendar-source").detach().prependTo("#schedule-form");


        $('#calendar').css('display','block');
        $('.schedule-btn').css('display','block');
        $('#live').css('display','none');
        $('.live-list').css('display','none');
        $('.profile').css('display','none');
        $('#create-course').css('display','none');
        $('.video-details').css('display','none');
        $('.upload-list').css('display','none');
        $('#user-profile').css('display','none');
        $('#live-update').css('display','none');
        $('.schedule-container').css('display','none');
        $('.checkout').css('display','none')


});

      $('#live-update').on("click",".edit-live",function(e){
        e.preventDefault();
        closeNav()
        req = $.ajax({
    url:$(this).attr('data-href'),
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });

        req.done(function(data){
        $('#update_session_title').val(data.result.title);
        $('#update_session_description').val(data.result.description);
        $('#update_session_category').val(data.result.category);

            $('.schedule').css('display','none');
        $(".calendar-source").detach().appendTo(".append-edit-calendar");


        $('#calendar').css('display','block');
        $('#edit-live').css('display','block');
        $('#live').css('display','none');
        $('#live-update').css('display','none');
        $('.live-list').css('display','none');
        $('.profile').css('display','none');
        $('#create-course').css('display','none');
        $('.video-details').css('display','none');
        $('.upload-list').css('display','none');
        $('#user-profile').css('display','none');
        $('.checkout').css('display','none')
        });



});
      $('.schedule-container').on("click",".edit-schedule",function(e){
        e.preventDefault();
        closeNav()
        req = $.ajax({
    url:$(this).attr('data-href'),
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });

        req.done(function(data){


            $('.schedule').css('display','none');
        $(".calendar-source").detach().appendTo(".append-edit-schedule");


        $('#calendar').css('display','block');
        $('#edit-live').css('display','none');
        $('#live').css('display','none');
        $('#live-update').css('display','none');
        $('.live-list').css('display','none');
        $('.profile').css('display','none');
        $('#create-course').css('display','none');
        $('.video-details').css('display','none');
        $('.upload-list').css('display','none');
        $('#user-profile').css('display','none');
        $('.schedule-container').css('display','none');
        });



});
      $('.schedule-container').on("click",".delete-schedule",function(e){
        e.preventDefault();
        closeNav()
        req = $.ajax({
    url:$(this).attr('data-href'),
    type:'DELETE',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });

        req.done(function(data){


            $('.schedule').css('display','none');


        $('#calendar').css('display','none');
        $('#edit-live').css('display','none');
        $('#live').css('display','none');
        $('#live-update').css('display','none');
        $('.live-list').css('display','none');
        $('.profile').css('display','none');
        $('#create-course').css('display','none');
        $('.video-details').css('display','none');
        $('.upload-list').css('display','none');
        $('#user-profile').css('display','none');
        $('#update-schedule').css('display','none');
        $('.schedule-container').css('display','block');
        });



});

      $('#course-create').on("click",function(e){
        e.preventDefault();
        closeNav()
        $(".editor-source").detach().appendTo(".form-editor");
        $('.editor-source').css('display','none')
        $('#live').css('display','none');
        $('.live-list').css('display','none');
        $('#create-live').css('display','none');
        $('.schedule').css('display','none');
        $('#course-upload').css('display','none');
        $('#create-series').css('display','none');
        $('.profile').css('display','none');
        $('#create-course').css('display','none');
        $('.video-details').css('display','none');
        $('.upload-list').css('display','none');
        $('#user-profile').css('display','none');
        $('#live-create').css('display','none');
        $('.schedule-container').css('display','none');
        $('#live-update').css('display','none');
        $('.upload-option').css('display','block');

});

      $('#live-create').on("click",function(e){
        e.preventDefault();
        closeNav()
        $(".calendar-source").detach().appendTo(".append-calendar");
        $('#live').css('display','none');
        $('.live-list').css('display','none');
        $('#create-live').css('display','block');
        $('#calendar').css('display','block');
        $('.schedule').css('display','none');
        $('#course-upload').css('display','none');
        $('#create-series').css('display','none');
        $('.profile').css('display','none');
        $('#create-course').css('display','block');
        $('.video-details').css('display','none');
        $('.upload-list').css('display','none');
        $('#user-profile').css('display','none');
        $('.schedule-container').css('display','none');
        $('#live-update').css('display','none');

});
      $('#single-click').on("click",function(e){
        e.preventDefault();

        $(".editor-source").detach().appendTo(".form-editor");
        $('.editor-source').css('display','block')
        $('#live').css('display','none');
        $('.live-list').css('display','none');
        $('#create-live').css('display','none');
        $('.schedule').css('display','none');
        $('#course-upload').css('display','block');
        $('#create-series').css('display','none');
        $('.profile').css('display','none');
        $('#create-course').css('display','block');
        $('.video-details').css('display','none');
        $('.upload-list').css('display','none');
        $('#user-profile').css('display','none');
        $('#live-create').css('display','none');
        $('.schedule-container').css('display','none');
        $('#live-update').css('display','none');
        $('.upload-option').css('display','none');

});
      $('#series-click').on("click",function(e){
        e.preventDefault();

        $(".editor-source").detach().appendTo(".form-editor");
        $('.editor-source').css('display','block')
        $('#live').css('display','none');
        $('.live-list').css('display','none');
        $('#create-live').css('display','none');
        $('.schedule').css('display','none');
        $('#course-upload').css('display','none');
        $('#create-series').css('display','block');
        $('.profile').css('display','none');
        $('#create-course').css('display','block');
        $('.video-details').css('display','none');
        $('.upload-list').css('display','none');
        $('#user-profile').css('display','none');
        $('#live-create').css('display','none');
        $('.schedule-container').css('display','none');
        $('#live-update').css('display','none');
        $('.upload-option').css('display','none');

});

      $('#update-course').on("click",function(e){
        e.preventDefault();
        closeNav()
        seriesUrl = '/editSeries?series_id='
          req = $.ajax({
    url:$(this).attr('data-href'),
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
        $('#course-update').empty();

        req.done(function(data){
          console.log(data.length)
          if (data.length == 0 )
            $('#course-update').append('<p>No contents</p>')

           else
             $.each(data.result, function(key,value) {


      $('#course-update').append('<card class="mt-2 mb-2 flex-fill flex-row shadow-lg row no-gutters user-course card"><div class="col-3 no-gutters cover-wrapper"><img id="course-img" src="../static/coverImages/'+value.coverImg+'" alt=""></div><div class="col-8 p-2 flex-fill flex-column no-gutters "><h6 id="course-title">'+value.title+'</h6><div id="total-episodes">Episodes : '+value.totalEpisodes+'</div><span id="course-price">Price : '+value.price+'</span><div class=""><div class=""><a type="button" class="add-ep-btn" data-href="/addEpisode?series_id='+value.id+'"  data-toggle="modal" data-target="#episode-modal" href=""><img src="../static/add.svg"  alt=""><span>Add</span></div><div class=""><a type="button"  data-toggle="modal" data-target="#myModal" href=""><img src="../static/delete.svg" alt=""></a><span>Delete</span></div><div class=""><a type="button"  data-href="'+seriesUrl +value.id+'"class="edit-series" data-toggle="modal" data-target="#series-modal" href=""><img src="../static/edit.svg" alt=""></a><span>Edit</span></div></div></div></card></div>');

});



        $('#course-update').css('display','block');
        $('#live').css('display','none');
        $('.live-list').css('display','none');
        $('#create-live').css('display','none');
        $('#live-update').css('display','none');
        $('.schedule').css('display','none');
        $('#course-upload').css('display','none');
        $('#create-series').css('display','none');
        $('.profile').css('display','none');
        $('#create-course').css('display','block');
        $('.video-details').css('display','none');
        $('.upload-list').css('display','none');
        $('#user-profile').css('display','none');


});


});
      $('#book-schedule-btn').on("click",function(e){
        e.preventDefault();
        $('#book-schedule').modal('toggle')
        scheduleUrl = '/userDetails?username=';
        bookUrl = '/book/';
        unbookUrl = '/unbook/';
        param = '?type=';
        type = 'schedule';
          req = $.ajax({
    url:$(this).attr('data-href'),
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
        $('.modal-body.append-schedule').empty();

        req.done(function(data){
          var details = data.schedule
                $.each(details, function(key,value) {
                  if (details.includes())
                    $('.modal-body.append-schedule').append('<div class=" text-center p-2 bg-dark text-light schedule-box"><h4>'+value.date +'</h4><span>'+value.startTime+' - '+ value.endTime+'</span><span class="mt-1"><a  class="click-book" data-href="'+bookUrl+value.id+param+type+'"><button type="button" id="book-btn" class="fixed-btn" >Book</button></a><a  class="click-unbook" data-href="'+unbookUrl+value.id+param+type+'" ><button type="button" id="unbook-btn" class="fixed-btn" >Unbook</button></a></span></div>');
});





        $('#course-update').css('display','block');
        $('#live').css('display','none');
        $('.live-list').css('display','none');
        $('#create-live').css('display','none');
        $('#live-update').css('display','none');
        $('.schedule').css('display','none');
        $('#course-upload').css('display','none');
        $('#create-series').css('display','none');
        $('.profile').css('display','block');
        $('#create-course').css('display','block');
        $('.video-details').css('display','none');
        $('.upload-list').css('display','none');
        $('#user-profile').css('display','none');


});


});

      $('#edit-schedule').on("click",function(e){
        e.preventDefault();
        closeNav()
        scheduleUrl = '/editSchedule?schedule_id='
          req = $.ajax({
    url:$(this).attr('data-href'),
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
$('.append-schedule').empty();
        req.done(function(data){


      $.each(data.result, function(key,value) {
                    $('.append-schedule').append('<div class=" text-center p-2 bg-dark text-light schedule-box"><h4>'+value.date +'</h4><span>'+value.start_time+' - '+ value.end_time+'</span><a type="button" data-href="'+scheduleUrl +value.id+'" class="edit-schedule" data-toggle="" data-target="" href=""><img src="../static/edit_w.svg" alt=""></a><span>Edit</span><a type="button" data-href="'+scheduleUrl +value.id+'" class="delete-schedule" data-toggle="" data-target="" href=""><img src="../static/delete_w.svg" alt=""></a><span>Delete</span></div>');



});
            $('.update-schedule').css('display','block');



        $('#calendar').css('display','none');
        $('.update-schedule-btn').css('display','none');
        $('#live').css('display','none');
        $('.live-list').css('display','none');
        $('.profile').css('display','none');
        $('#create-course').css('display','none');
        $('.video-details').css('display','none');
        $('.upload-list').css('display','none');
        $('#user-profile').css('display','none');
        $('.schedule-container').css('display','block');
        $('#live-update').css('display','none');

});


});

      $('#course-update').on("click",".edit-series",function(e) {
        e.preventDefault();
                  req = $.ajax({
    url:$(this).attr('data-href'),
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
        req.done(function(data){
        var object = data.result;
          $(".editor-source").detach().appendTo(".update-series-editor");
        $('.editor-source').css('display','block')
          $('[name="update_title"]').attr('value',object.title)


});

      });

      $('#update-live').on("click",function(e){
        e.preventDefault();
        closeNav()
        liveUrl = '/editLive?live_id='
          req = $.ajax({
    url:$(this).attr('data-href'),
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
        req.done(function(data){

          $('#live-update').empty();
                  $.each(data.result, function(key,value) {


      $('#live-update').append('<card class="mt-2 mb-2 flex-fill flex-row shadow-lg row no-gutters user-course card live-url" id="'+value.id+'"><div class="col-3 no-gutters cover-wrapper"><img id="course-img" src="'+coverImgSrc+value.coverImg+'" alt=""></div><div class="col-8 p-2 flex-fill flex-column no-gutters "><h6 id="course-title">'+value.title+'</h6><div id="live-date">Date : '+value.date+'</div><div id="live-time">Time : '+value.startTime +'-'+value.endTime +'</div><a type="button" data-href="'+liveUrl +value.id+'" class="edit-live" data-toggle="" data-target="" href=""><img src="../static/edit.svg" alt=""></a><span>Edit</span></div></card>');

});
          $('#live-update').css('display','block');
          $('#course-update').css('display','none');

        $('#live').css('display','none');
        $('.live-list').css('display','none');
        $('#create-live').css('display','none');
        $('.schedule').css('display','none');
        $('#course-upload').css('display','none');
        $('#create-series').css('display','none');
        $('.profile').css('display','none');
        $('#create-course').css('display','block');
        $('.video-details').css('display','none');
        $('.upload-list').css('display','none');
        $('#user-profile').css('display','none');
        $('.schedule-container').css('display','none');


});


});
      $('.yes-btn').on("click",function(e){
        e.preventDefault();
        closeNav()
        liveUrl = '/editLive?live_id='
          req = $.ajax({
    url:$('.edit-series').attr('data-href'),
    type:'DELETE',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
        req.done(function(data){});
          $('#live-update').css('display','block');
          $('#course-update').css('display','none');

        $('#live').css('display','none');
        $('.live-list').css('display','none');
        $('#create-live').css('display','none');
        $('.schedule').css('display','none');
        $('#course-upload').css('display','none');
        $('#create-series').css('display','none');
        $('.profile').css('display','none');
        $('#create-course').css('display','block');
        $('.video-details').css('display','none');
        $('.upload-list').css('display','none');
        $('#user-profile').css('display','none');
        $('.schedule-container').css('display','none');


});


});

    function pageRedirect(url) {
      window.location.href = url ;
    }

$(document).ready(function(){
      $('.addCart').on("click",function(e){
  e.preventDefault();
    var url = $(this).attr("data-href");
    var videoSrc = "../static/videos/";
    var userImgSrc = "../static/profile_pics/";
    var currency = "￥"

  req = $.ajax({
    url:url,
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")
      popover('Log in to add to cart','error')

    }

  });
  req.done(function(data){
  popover('Added to cart','green')

});
});

});
$(document).ready(function(){
      $('.cart').on("click",function(e){
  e.preventDefault();
    var url = $(this).attr("data-href");
    var videoSrc = "../static/videos/";
    var userImgSrc = "../static/profile_pics/";
    var currency = "￥"

  req = $.ajax({
    url:url,
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")


    }

  });
  req.done(function(data){
    $('.cart-list').empty();
        $.each(data.result, function(key,value) {


      $('.cart-list').append('<div><img id="cart-coverImg" src="" alt=""><p id="cart-title">'+value.title+'</p><span id="cart-price">'+value.price+'</span></div>');

});

});
});
      $('#buy').on("click",function(e){
  e.preventDefault();
    var url = $(this).attr("data-href");
    var userId = $(this).attr("user-id");

    var videoSrc = "../static/videos/";
    var userImgSrc = "../static/profile_pics/";
    var currency = "￥"

  req = $.ajax({
    url:url,
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
  req.done(function(data){
      var checkoutUrl = "/checkout?price="+data.price+"&subject="+data.title+"&course_id="+data.id+"&user="+userId;
      $('.checkout').css('display','block')
      $('#total-price').text(currency+data.price)
      $('.click-pay').attr('data-href',checkoutUrl)
      $('#original-price').text(currency+data.price)
      $('#checkout-title').text(data.title)
      $('#live-update').css('display','none');
      $('#course-update').css('display','none');

        $('#live').css('display','none');
        $('.live-list').css('display','none');
        $('#create-live').css('display','none');
        $('.schedule').css('display','none');
        $('#course-upload').css('display','none');
        $('#create-series').css('display','none');
        $('.profile').css('display','none');
        $('#create-course').css('display','none');
        $('.video-details').css('display','none');
        $('.upload-list').css('display','none');
        $('#user-profile').css('display','none');
        $('.schedule-container').css('display','none');



});
});

            $('.click-pay-login').on("click",function(e) {
              e.preventDefault();
              popover('Login to complete Payment','error')
            });
      $('.click-pay').on("click",function(e){
  e.preventDefault();
    var url = $(this).attr("data-href");
    var videoSrc = "../static/videos/";
    var userImgSrc = "../static/profile_pics/";
    var currency = "￥"

  req = $.ajax({
    url:url,
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
  req.done(function(data){


  pageRedirect(data)



});
});

});


$('#main').ready(function(){
      var arg = 'videoId=';
  var videoUrl = '/videoDetails?'+arg;
  var userUrl = '/userDetails?username='

  req = $.ajax({
    url:'/videos',
    type:'GET',
    data:{},
    success:function (data) {
      console.log(data)
    },error:function (error) {
      console.log(error)
      console.log("error")

    }

  });
  req.done(function(data){
    var obj = data.result;
    $.each(obj, function(key,value) {


      $('.upload-list').append('<div class="thumb-wrapper" data-href="'+videoUrl+ value.id +'"><li><a  class="video"   video-id="'+ value.id +'" href="#"><img class="video-feed" src="../static/profile_pics/'+ value.userImg +'" alt=""></a></li></div><div class="video-info"><div class="row no-gutters"><div class="col-2 col-sm-2 col-md-2 no-gutters">     <div class="profile-pic-wrapper click-pro-pic"  data-href=" '+userUrl+ value.username +'">     <span><a  class="user-profile-pic"   user-id="" href="#"><img id="profilepic"  src="../static/profile_pics/'+ value.userImg +'" alt=""></a></span> </div> </div><div class="col no-gutters"><div class="inner-info"> <div class="flex-fill flex-column">    <h6>'+ value.title +'</h6>     <div class="upload-username">'+ value.username +'</div>     <span class="upload-username">'+ value.category +'</span> <span>     <p class="likes-comments"  class="text-justify text-left " data-likes="">     <span>'+ value.likes +'</span>     <img     src="../static/heart.png" alt="" width="16">     <span>'+ value.comments +'</span>     <img  src="../static/comment.svg" alt="" width="16"> </p> </span></div>          </div> </div></div></div>');

});
$('#live').css('display','none');
$('.live-list').css('display','none');
$('.profile').css('display','none');
$('.video-details').css('display','none');
$('.upload-list').css('display','block');
$('#user-profile').css('display','none');
  });
});

$("form#series-course").on('click','.subtitle',function () {

    $header = $(this);
    //getting the next element
    $content = $header.next();
    //open up the content needed - toggle the slide- if visible, slide up, if not slidedown.
    $content.slideToggle(500, function () {
        //execute this after slideToggle is done
    });

});

var dropdown = document.getElementsByClassName("dropdown-btn");
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}


function progress() {
    var pbar = $('#progressBar'), currentProgress = 0;
    function trackUploadProgress(e)
    {
        if(e.lengthComputable)
        {
            currentProgress = (e.loaded / e.total) * 100; // Amount uploaded in percent
            $(pbar).width(currentProgress+'%');

            if( currentProgress == 100 )
            console.log('Progress : 100%');
        }
    }
    }

$(document).ready(function() {

	$('form#course').on('submit', function(event) {
      var csrf_token = $('#csrf_token').attr('value');



		$.ajax({
          beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        },  enctype: 'multipart/form-data',
			data : new FormData(this),
			type : 'POST',
			url : '/createcourse?status=single',
            processData: false,
            contentType: false,
          xhr: function()
            {
                // Custom XMLHttpRequest
                var appXhr = $.ajaxSettings.xhr();

                // Check if upload property exists, if "yes" then upload progress can be tracked otherwise "not"
                if(appXhr.upload)
                {
                    // Attach a function to handle the progress of the upload
                    appXhr.upload.addEventListener('progress',progress, false);
                }
                return appXhr;
            },


          success: function(response){
          if(response){
            var responseObj = jQuery.parseJSON(response);

            if(responseObj.ResponseData)
              popover('Uploaded successfully','success');

          }
          },
          error: function (error) {
          popover('Error uploading your File','error')

          },


		}).done(function(data) {

        popover(data.msg,'success')

		});

		event.preventDefault();

	});
	$('form#series-course').on('submit', function(event) {
 var csrf_token = $('#csrf_token').attr('value');
		$.ajax({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        },  enctype: 'multipart/form-data',
			data : new FormData(this),
			type : 'POST',
			url : '/createcourse?status=series',
            processData: false,
            contentType: false,

		})
		.done(function(data) {

        console.log('done')

		});

		event.preventDefault();

	});
	$('form#addEpisode').on('submit', function(event) {
 var csrf_token = $('#csrf_token').attr('value');
		$.ajax({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        },  enctype: 'multipart/form-data',
			data : new FormData(this),
			type : 'POST',
			url : $('.add-ep-btn').attr('data-href'),
            processData: false,
            contentType: false,

		})
		.done(function(data) {

        console.log('done')

		});

		event.preventDefault();

	});
	$('form#schedule-form').on('submit', function(event) {
 var csrf_token = $('#csrf-token').attr('value');
		$.ajax({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        },
			data : new FormData(this),
			type : 'POST',
			url : $('#schedule-form').attr('data-href'),
            processData: false,
            contentType: false,

		})
		.done(function(data) {

        console.log('done')

		});

		event.preventDefault();

	});
	$('form.session-form').on('submit', function(event) {
 var csrf_token = $('#csrf_token').attr('value');
		$.ajax({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        },
			data : new FormData(this),
			type : 'POST',
			url : $('.session-form').attr('data-href'),
            processData: false,
            contentType: false,

		})
		.done(function(data) {

        console.log('done')

		});

		event.preventDefault();

	});

});