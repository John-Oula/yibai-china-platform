
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

$(document).ready(function(){

  $('#ajax').on('submit',function(){
  var that = $(this),
    url = that.attr('url'),
      data={};
  that.find('[name]').each(function (index,value) {
    var that = $(this),
        name= that.attr('name'),
        value = that.val();
    data[name] = value;

  });
  console.log(data);




    var csrf_token = $('input#csrf_token').attr('value');
    $.ajax({
      url:url,
      type:"post",
      data:JSON.stringify(data) ,
      contentType: "application/json; charset=utf-8", // this
      dataType: "json",
      beforeSend: function(xhr, settings) {
          if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrf_token);
          }
      },
      success:function(response){
        console.log(response);
      }
    });
    return false;
});
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






