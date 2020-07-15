
document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');

  var calendar = new FullCalendar.Calendar(calendarEl, {
    plugins: [ 'interaction', 'dayGrid', 'timeGrid','bootstrap' ,'interactionPlugin'],

    select: function( selectionInfo ){
      let start_time = selectionInfo.startStr;
      document.getElementById('start-time').value = new Date(start_time).valueOf();
      let end_time = selectionInfo.endStr;
      document.getElementById('end-time').value = new Date(end_time).valueOf();

    },
    dateClick: function(info){},
    defaultTimedEventDuration: '01:45:00',
    forceEventDuration: true,
    themeSystem: 'bootstrap',
    defaultView: 'dayGridMonth',
    defaultDate: Date.now(),
    navLinks: true,
    selectable: true,
    selectMirror: true,
    unselectAuto: false,
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
$('#follow').click(function(e){
  e.preventDefault();

  var followURL = $(this).attr("data-href");


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
    $('#followers-count').text(data.followers);
    $('#follow').css("display","none");
    $('#unfollow').css("display","block");
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
    $('#follow').css("display","block");
    $('#unfollow').css("display","none");
  })


})

  });

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

function update() {
  $.getJSON("/updateFeed", function(data) {
    console.log(data)
//    $("#feed-content").html(data);
    window.setTimeout(update, 10000);
  });
}
update()
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

$(window).scroll(function() {
    $('video').each(function() {
        if ($(this).visible(true)) {
            $(this)[0].play();
        } else {
            $(this)[0].pause();
        }
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



function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
    document.body.style.backgroundColor = "white";
}


$(document).ready(function(){
  $('.video').click(function(e){
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
        $('.upload-list').css('display','none');
        $('.video-details').css('display','block');
        $('.video-feed').attr("src",videoSrc + data.videoRef);
        $('.video-feed').attr("video-id",data.id);
        $('#video-title').html(data.title);
        $('#video-author').html(data.author);
        $('#video-description').html(data.description);
        $('#video-price').html(currency + data.price);
        $('#video-price').css("fontSize","17px");
        $('img#profilepic').attr("src",userImgSrc + data.authorImage);

});
});
});
