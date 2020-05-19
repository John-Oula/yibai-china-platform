
document.addEventListener('DOMContentLoaded', function() {
  var calendarEl = document.getElementById('calendar');

  var calendar = new FullCalendar.Calendar(calendarEl, {
    plugins: [ 'interaction', 'dayGrid', 'timeGrid','bootstrap' ,'interactionPlugin'],

    select: function( selectionInfo ){
      let start_time = selectionInfo.startStr;
      document.getElementById('start-time').value = Date.parse(start_time);
      let end_time = selectionInfo.endStr;
      document.getElementById('end-time').value = Date.parse(end_time);

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








