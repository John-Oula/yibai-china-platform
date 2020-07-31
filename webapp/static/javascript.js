
var start_time;
var end_time;
 var coverImgSrc = '../static/coverImages/';
 var userImgSrc = '../static/profile_pics/';
 var videoSrc = '../static/videos/';



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

    }

  });
  req.done(function(data){
    $('.likes').text(data.likes);
    $('.like-btn').css("display","none");
    $('#unlike-btn').css("display","block");
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
    $('.like-btn').css("display","block");
    $('#unlike-btn').css("display","none");

  })


})
  });


function updateText(word,verb){
  word.text(verb)
}


$(document).ready(function(){
$('#book').click(function(e){
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

    }

  });
  req.done(function(data){
    $('#book').css("display","none");
    $('#unbook').css("display","block");
  })


})
$('#unbook').click(function(e){
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
    $('#book').css("display","block");
    $('#unbook').css("display","none");
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
    var coverImgUrl = '../static/coverImages/';

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
$('.live-title').html(data.title);
$('#live-startTime').html(data.startTime);
$('#live-endTime').html(data.endTime);
$('#live-date').html(data.date);
$('#live-description').html(data.description);
$('img.live-img').attr('src',coverImgUrl+data.coverImage);
$('img#profilepic').attr('src',userImgUrl+data.userImg);
$('#live-username').html(data.host);
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
  $('.live').click(function(e){
  e.preventDefault();
  var liveUrl= '/liveDetails?liveId='

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


      $('.live-list').append('<card class="card shadow-sm" id="live-card" data-href="'+liveUrl+value.id+'"> <card > <div class="live-img-wrapper"><img class="live-img" src="../static/coverImages/'+value.coverImg+'" alt=""></div> <div class="live-profile-pic-wrapper"  data-href=""><span><a  class="user-profile-pic border-light" href="#"><img id="profilepic"  src="../static/profile_pics/'+ value.userImg +'" alt=""></a></span> </div><div class="p-2 row no-gutters"><span class="live-info col-8 flex-content flex-column no-gutters"><span class="live-title">'+ value.title +'</span><span class="">Hosted by:'+ value.host +' </span><span class="">Category:'+ value.category +'</span><span class=""> </span></span>  <span class="live-info col-4 flex-content flex-column no-gutters">           <span class="text-right">'+ value.startTime + '-'+ value.endTime +'</span><span class="text-right">'+ value.date +'</span>  <div class="circle-icon text-right text-center mt-2  p-2 shadow-sm"> <img class="rounded-circle" src="../static/share.svg" alt=""> </div> </span> </div> </card> </card>');

});
$('#live').css('display','block');
$('.live-list').css('display','block');
$('.live-details').css('display','none');
$('.profile').css('display','none');
$('.video-details').css('display','none');
$('.upload-list').css('display','none');
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


      $('.upload-list').append('<div class="thumb-wrapper" data-href="'+videoUrl+ value.id +'"><li><a  class="video"   video-id="'+ value.id +'" href="#"><img class="video-feed" src="../static/profile_pics/'+ value.userImg +'" alt=""></a></li></div><div class="video-info"><div class="row no-gutters"><div class="col-2 col-sm-2 col-md-2 no-gutters">     <div class="profile-pic-wrapper"  data-href=" '+userUrl+ value.username +'">     <span><a  class="user-profile-pic"   user-id="" href="#"><img id="profilepic"  src="../static/profile_pics/'+ value.userImg +'" alt=""></a></span> </div> </div><div class="col no-gutters"><div class="inner-info"> <div class="flex-fill flex-column">    <h6>'+ value.title +'</h6>     <div class="upload-username">'+ value.username +'</div>     <span class="upload-username">'+ value.category +'</span> <span>     <p class="likes"  class="text-justify text-left " data-likes="">     <span>'+ value.likes +'</span>     <img     src="../static/heart.png" alt="" width="16">     <span>'+ value.comments +'</span>     <img  src="../static/comment.svg" alt="" width="16"> </p> </span></div>          </div> </div></div></div>');

});
$('#live').css('display','none');
$('.live-list').css('display','none');
$('.profile').css('display','none');
$('.video-details').css('display','none');
$('.upload-list').css('display','block');
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
    var videoSrc = "https://www.100chinaguide.com/static/videos/";
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
        $('.upload-list').css('display','none');
        $('.video-details').css('display','block');
        $('.addCart').attr('data-href','/addCart?upload_id='+data.id);
        $('video').attr("src",videoSrc + data.videoRef);
        $('.video-js').attr("src",videoSrc + data.videoRef);
        $('.video-feed').attr("video-id",data.id);
        $('#video-title').html(data.title);
        $('#video-author').html(data.username);
        $('#video-likes').html(data.likes);
        $('#video-comments').html(data.comments);
        $('#video-description').html(data.description);
        $('#video-price').html(currency + data.price);
        $('#video-price').css("fontSize","17px");
        $('img#profilepic').attr("src",userImgSrc + data.userImg);

});
});

      $('.upload-list').on("click",".profile-pic-wrapper",function(e){
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
            $('#follow').click(function(e){
  e.preventDefault();

  var followURL = followUrl+"/"+data.username;


  req = $.ajax({
    url:followURL,
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
    $('#user-followers').text(data.followers);
    $('#follow').css("display","none");
    $('#unfollow').css("display","inlineBlock");
  })


})
        $('#unfollow').click(function(e){
  e.preventDefault();

  var unfollowURL = unfollowUrl+"/"+data.username;


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
    $('#user-followers').text(data.followers);
    $('#follow').css("display","inline-block");
    $('#unfollow').css("display","none");
  })


})
        $('.upload-list').css('display','none');
        $('.profile').css('display','block');
        if (data.Isfollowing === true){
                  $('#unfollow').attr('data-href',unfollowUrl+"/"+data.username);
                          $('#unfollow').css('display','inline-block');


        }


        else{
                  $('#follow').attr('data-href',followUrl+"/"+data.username);

                  $('#follow').css('display','inline-block');


        }


        $('#user-username').html(data.username);
        $('#user-videos').html(data.videos);
        $('#user-followers').html(data.followers);
        $('#user-live-sessions').html(data.liveSessions);
        $('#user-introduction').html(data.description);
        $('img#profilepic').attr("src",userImgSrc + data.userImage);

});
});


      $('#schedule-create').on("click",function(e){
        e.preventDefault();
        closeNav()
            $('.schedule').css('display','block');
        $(".calendar-source").detach().appendTo(".calendar-container");


        $('#calendar').css('display','block');
        $('#live').css('display','none');
        $('.live-list').css('display','none');
        $('.profile').css('display','none');
        $('#create-course').css('display','none');
        $('.video-details').css('display','none');
        $('.upload-list').css('display','none');


});
      $('#live-update').on("click",".edit-live",function(e){
        e.preventDefault();
        closeNav()
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


});

      $('#course-create').on("click",function(e){
        e.preventDefault();
        closeNav()
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


                  $.each(data.result, function(key,value) {


      $('#course-update').append('<card class="mt-2 mb-2 flex-fill flex-row shadow-lg row no-gutters user-course card"><div class="col-3 no-gutters cover-wrapper"><img id="course-img" src="../static/coverImages/'+value.coverImg+'" alt=""></div><div class="col-8 p-2 flex-fill flex-column no-gutters "><h6 id="course-title">'+value.title+'</h6><div id="total-episodes">Episodes : '+value.totalEpisodes+'</div><span id="course-price">Price : '+value.price+'</span><div class=""><div class=""><a type="button"   data-toggle="modal" data-target="#episode-modal" href=""><img src="../static/add.svg" alt=""><span>Add</span></div><div class=""><a type="button"  data-toggle="modal" data-target="#myModal" href=""><img src="../static/delete.svg" alt=""></a><span>Delete</span></div><div class=""><a type="button"  data-href="'+seriesUrl +value.id+'"class="edit-series" data-toggle="modal" data-target="#series-modal" href=""><img src="../static/edit.svg" alt=""></a><span>Edit</span></div></div></div></card></div>');

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


      $('#live-update').append('<card class="mt-2 mb-2 flex-fill flex-row shadow-lg row no-gutters user-course card"><div class="col-3 no-gutters cover-wrapper"><img id="course-img" src="'+coverImgSrc+value.coverImg+'" alt=""></div><div class="col-8 p-2 flex-fill flex-column no-gutters "><a data-href="'+liveUrl +value.id+'" href=""><h6 id="course-title">'+value.title+'</h6><div id="live-date">Date : '+value.date+'</div><div id="live-time">Time : '+value.startTime +'-'+value.endTime +'</div><a type="button" data-href="" class="edit-live" data-toggle="" data-target="" href=""><img src="../static/edit.svg" alt=""></a><span>Edit</span></div></card>');

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


});


});
});


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

    }

  });
  req.done(function(data){


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


      $('.upload-list').append('<div class="thumb-wrapper" data-href="'+videoUrl+ value.id +'"><li><a  class="video"   video-id="'+ value.id +'" href="#"><img class="video-feed" src="../static/profile_pics/'+ value.userImg +'" alt=""></a></li></div><div class="video-info"><div class="row no-gutters"><div class="col-2 col-sm-2 col-md-2 no-gutters">     <div class="profile-pic-wrapper"  data-href=" '+userUrl+ value.username +'">     <span><a  class="user-profile-pic"   user-id="" href="#"><img id="profilepic"  src="../static/profile_pics/'+ value.userImg +'" alt=""></a></span> </div> </div><div class="col no-gutters"><div class="inner-info"> <div class="flex-fill flex-column">    <h6>'+ value.title +'</h6>     <div class="upload-username">'+ value.username +'</div>     <span class="upload-username">'+ value.category +'</span> <span>     <p class="likes"  class="text-justify text-left " data-likes="">     <span>'+ value.likes +'</span>     <img     src="../static/heart.png" alt="" width="16">     <span>'+ value.comments +'</span>     <img  src="../static/comment.svg" alt="" width="16"> </p> </span></div>          </div> </div></div></div>');

});
$('#live').css('display','none');
$('.live-list').css('display','none');
$('.profile').css('display','none');
$('.video-details').css('display','none');
$('.upload-list').css('display','block');
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


$(document).ready(function() {

	$('form#course').on('submit', function(event) {
 var csrf_token = $('#csrf_token').attr('value');
   // Populate hidden form on submit
  var about = $('input.about').attr('name');
  about.value = $('.ql-editor').html();


		$.ajax({
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrf_token);
            }
        },  enctype: 'multipart/form-data',
			data : new FormData(this),
			type : 'POST',
			url : '/createcourse',
            processData: false,
            contentType: false,

		})
		.done(function(data) {

        console.log('done')

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
			url : '/seriesCourse',
            processData: false,
            contentType: false,

		})
		.done(function(data) {

        console.log('done')

		});

		event.preventDefault();

	});

});