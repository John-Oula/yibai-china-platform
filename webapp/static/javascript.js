
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





function Event(new_event){
  alert(new_event.toString())
  return new_event
}

$("#button-join").on("click",function(){
  roomName = document.getElementById('room-name').value;
  if(!roomName){
    alert("enter room name")
    return;
  }
  else{
  $.ajax({
  type:"GET",
  url:"/token",
  dataType:"json",

  beforeSend :function() {


    $("#loader").show();
  },
  complete:function(){
    $("#loader").hide();

    $("#user-input").hide();
    document.getElementById('room-page').style.display='flex';
    },
  success:function(data){
    identity = data.identity;



    document.getElementById('room-controls').style.display='block';



    log("Joining room '" + roomName + "'...");
    var connectOptions = {
      name: roomName,
      logLevel: 'debug',
      dominantSpeaker: true,
      automaticSubscription:true
    };




    // Join the Room with the token from the server and the
    // LocalParticipant's Tracks.
    Video.connect(data.token, connectOptions).then(roomJoined, function(error) {
      log('Could not connect to Twilio: ' + error.message)




    });


  },
  error:function(){
    $("#user-input").show()

  }

});
  };
})




