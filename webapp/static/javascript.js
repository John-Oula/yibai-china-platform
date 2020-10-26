var start_time;
var end_time;
var coverImgSrc = '../static/coverImages/';
var userImgSrc = '../static/profile_pics/';
var videoSrc = '../static/videos/';
var currentUserId = $('.uId').attr("user-Id")
var currentUserUsername = $('#currentUser').attr("username")
var currentUserProPic = $('#currentUser').attr("propic")

function popover(msg, statusType) {
    if (statusType == 'success') {
        statusType = 'green'
    } else if (statusType == 'error')
        statusType = '#e74525'
    $('.flash-msg').text(msg);
    $('.flash-msg').css('color', statusType);

    $(".flash-msg").animate({marginTop: "30px"});
    $('.navbar-brand').css('zIndex', '0');
    $('.flash-msg').slideDown(function () {

        setTimeout(function () {

            $('.flash-msg').slideUp();
            $(".flash-msg").animate({marginTop: "0px"});
            $('.navbar-brand').css('zIndex', '0');
            $('.navbar-brand').css('zIndex', '100');
        }, 2000);


    });

}

document.addEventListener('DOMContentLoaded', function () {
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: ['interaction', 'dayGrid', 'timeGrid', 'bootstrap', 'interactionPlugin'],

        select: function (selectionInfo) {
            start_time = selectionInfo.startStr;
            document.getElementById('start-time').value = new Date(start_time).valueOf();
            end_time = selectionInfo.endStr;
            document.getElementById('end-time').value = new Date(end_time).valueOf();

        },
        dateClick: function (info) {
        },
        longPressDelay: '1000',
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
        eventTimeFormat: {
            hour: 'numeric',
            minute: '2-digit',
            meridiem: false,

        },

        header: {
            left: 'prev,next today',
            center: 'title',

            right: 'dayGridMonth,timeGridWeek,timeGridDay'
        },
        height: 650,

        slotDuration: '00:05',
        allDayDefault: false,

        displayEventEnd: true,
    });


    calendar.render();

});

function update() {
    $.getJSON("/getUserLive?user_id=" + currentUserId, function (data) {
        var obj = data.result;

        $.each(obj, function t(key, value) {
            var meetingTime = value.startTime


            return meetingTime
        });


        window.setTimeout(update, 10000);
    })

}

function homepage() {


    
    
    
    
    $('.upload-list').css('display', 'flex');
    $('#user-profile').css('display', 'none');
    $('#course-upload').css('display', 'none');
    $('.checkout').css('display', 'none')


};

function calculateTime(now, scheduled) {


    s = now.split(':');
    e = scheduled.split(':');

    min = e[1] - s[1];
    hour_carry = 0;
    if (min < 0) {
        min += 60;
        hour_carry += 1;
    }
    hour = e[0] - s[0] - hour_carry;
    diff = hour + ":" + min;
    mins = hour * 60 + min;
    return mins

}

function checkTime(time) {
    var now = new Date()
    var h = now.getHours()
    var m = now.getMinutes()
    var current = h + ':' + m

    if ((calculateTime(current, time)) == 0) {
        $('.edit-live').detach()
        $('.start-btn').css('display', 'flex')
        return 'flex'

    } else if ((calculateTime(current, time)) <= 5) {
//    popover('Your meeting is starting in 5 minutes')
        $('.start-btn').css('display', 'flex')
        return 'flex'
    } else if ((calculateTime(current, time)) >= 5) {
//    popover('Your meeting is starting in 5 minutes')
        $('.start-btn').css('display', 'none')
        return 'none'
    }
    ;
};

$(function () {

    $('.btn-add').click(function () {
        $('.wrapper:first').clone().appendTo('.series-div');
    });

});

$(document).ready(function () {
    $("#addclass").click(function () {
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




$(document).ready(function () {
    $('.like-btn').click(function (e) {
        e.preventDefault();

        var likeURL = $(this).attr("data-href");


        req = $.ajax({
            url: likeURL,
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")
                popover('Log in to Like the video', 'error')

            }

        });
        req.done(function (data) {
            $('.likes').text(data.likes);
            $('#video-likes').text(data.likes);
            $('.like-btn').css("display", "none");
            $('#unlike-btn').css("display", "flex");
        })


    })

});


$(document).ready(function () {
    $('#unlike-btn').click(function (e) {
        e.preventDefault();
        var unlikeURL = $(this).attr("data-href");


        req = $.ajax({
            url: unlikeURL,
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        req.done(function (data) {
            $('.likes').text(data.likes);
            $('#video-likes').text(data.likes);
            $('.like-btn').css("display", "flex");
            $('#unlike-btn').css("display", "none");

        })


    })
});


function updateText(word, verb) {
    word.text(verb)
}


$(document).ready(function () {
    $('#main').on('click', '#book', function (e) {
        e.preventDefault();

        var bookURL = $(this).attr("data-href");


        req = $.ajax({
            url: bookURL,
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")
                popover('Login to Book a seat', 'error')

            }

        });
        req.done(function (data) {
            popover('Booked successfully', 'green')

            $('#book').css("display", "none");

            $('#unbook').css("display", "flex");
        })


    })
    $('#main').on('click', '.click-book', function (e) {
        e.preventDefault();

        var bookURL = $(this).attr("data-href");
        var cnt = $(this).attr("cnt");


        req = $.ajax({
            url: bookURL,
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")
                popover('Login to Book a seat', 'error')

            }

        });
        req.done(function (data) {
            popover('Booked successfully', 'green')

            $('#book-schedule-' + cnt +'').css("display", "none");

            $('#unbook-schedule-' + cnt +'').css("display", "flex");
        })


    })
    $('#main').on('click', '#unbook', function (e) {
        e.preventDefault();

        var unbookURL = $(this).attr("data-href");


        req = $.ajax({
            url: unbookURL,
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        req.done(function (data) {
            $('#book').css("display", "flex");

            $('#unbook').css("display", "none");
        })


    })
    $('#main').on('click', '.click-unbook', function (e) {
        e.preventDefault();

        var unbookURL = $(this).attr("data-href");
        var cnt = $(this).attr("cnt");


        req = $.ajax({
            url: unbookURL,
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        req.done(function (data) {
             $('#book-schedule-' + cnt +'.click-book').css("display", "flex");

            $('#unbook-schedule-' + cnt +'.click-unbook').css("display", "none");
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
    coll[i].addEventListener("click", function () {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
            content.style.display = "none";
        } else {
            content.style.display = "block";
        }
    });
}


function Event(new_event) {
    alert(new_event.toString())
    return new_event
}

$(document).ready(function () {
    $('#follow').click(function (e) {
        e.preventDefault();

        var followURL = $(this).attr("data-href");
        var username = $('#user-username').text()


        req = $.ajax({
            url: followURL,
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                popover('Log in to follow ' + username + '', 'red');

                console.log(error)
                console.log("error")

            }

        });
        req.done(function (data) {
            popover('You are now following ' + username + '', 'green');
            $('#followers-count').text(data.followers);
            $('#user-followers').text(data.followers);
            popover('You are now following ' + username + '');
            $('#follow').css("display", "none");
            $('#unfollow').css("display", "inline-block");
        })


    })
    $('#unfollow').click(function (e) {
        e.preventDefault();

        var unfollowURL = $(this).attr("data-href");


        req = $.ajax({
            url: unfollowURL,
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        req.done(function (data) {
            $('#followers-count').text(data.followers);
            $('#user-followers').text(data.followers);
            $('#follow').css("display", "inline-block");
            $('#unfollow').css("display", "none");
        })


    })

});

$(document).ready(function () {
    $('#sessions-btn').click(function (e) {
        e.preventDefault();
        var sessionURL = $(this).attr("data-href");

        req = $.ajax({
            url: sessionURL,
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        req.done(function (data) {
            $('#feed-content').css('display', 'none');
            $('#session-content').css('display', 'block');
        });


    });
    $('#posts-btn').click(function (e) {
        e.preventDefault();
        var postsURL = $(this).attr("data-href");

        req = $.ajax({
            url: postsURL,
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        req.done(function (data) {
            $('#feed-content').css('display', 'block');
            $('#session-content').css('display', 'none');
        });
    });
});

$('.live-details').ready(function () {
    $('.live-details').css('display', 'block');
//    $('.live-list').on('click', '.live-card', function (e) {
//        e.preventDefault();
//        var liveUrl = $(this).attr("data-href");
        var liveParam = $.urlParam('liveId')
        var liveUrl = '/liveDetails?liveId=' + liveParam;
        var userImgUrl = '../static/profile_pics/';
        var userUrl = '/userDetails?user_id=';
        var coverImgUrl = '../static/coverImages/';
        var bookUrl = '/book/';
        var unbookUrl = '/unbook/';
        var param = '?type=schedule';
        var paramLive = '?type=live';

        req = $.ajax({
            url: liveUrl,
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        req.done(function (data) {
            var obj = data.schedule;

            $.each(obj, function (key, value) {
                var cntId = value.id;


                $('#unbook-schedule-' + cntId +'').css("display", "none");
                $('.schedule-tab').append('<div class=" text-center p-2 bg-dark text-light schedule-box"><h4>' + value.date + '</h4><span>' + value.startTime + ' - ' + value.endTime + '</span><span class="mt-1"><a cnt="'+ value.id +'" id="book-schedule-' + cntId + '" class="click-book" data-href="' + bookUrl + value.id + param  + '"><button   class="fixed-btn" >Book</button></a><a cnt="'+ value.id +'" id="unbook-schedule-' + cntId + '" class="click-unbook" data-href="' + unbookUrl + value.id + param  + '" ><button   class="fixed-btn" >Unbook</button></a></span></div>');
                if (value.hasBookedSchedule === true){
                    $('#book-schedule-' + cntId +'').css('display', 'none');
                    $('#unbook-schedule-' + cntId +'').css('display', 'flex');
                } else if(value.hasBookedSchedule === false){
                    $('#unbook-schedule-' + cntId +'').css('display', 'none');
                    $('#book-schedule-' + cntId +'').css('display', 'flex');
            }
            });






            $('.live-details').css('display', 'block');
            $('#profile-btn').attr('data-href', userUrl + data.host.userId);
            $('#profile-btn').attr('href', userUrl + data.host.userId);
            $('.live-profile-pic-wrapper').attr('data-href', userUrl + data.host.id);
            $('.live-title').html(data.title);
            $('#live-startTime').html(data.startTime);
            $('#live-endTime').html(data.endTime);
            $('#live-date').html(data.date);
            $('#live-description').html(data.description);
            $('#host-username').html(data.host.host);
            $('#host-introduction').html(data.host.introduction);
            $('img.live-img').attr('src', coverImgUrl + data.coverImage);
            $('img.profilepic').attr('src', userImgUrl + data.host.userImg);
            $('#book').attr('data-href', bookUrl + data.id+paramLive);
            $('#unbook').attr('data-href', unbookUrl + data.id+paramLive);
            $('#live-username').html(data.host.host);
            if (data.hasBooked === true){
                    $('#book').css('display', 'none');
                    $('#unbook').css('display', 'flex');

            }

                else if(data.hasBooked === false){
                    $('#unbook').css('display', 'none');
                    $('#book').css('display', 'flex');
            }
            
            $('#user-profile').css('display', 'none');
            $('.checkout').css('display', 'none')
        });


    });

//});
$('#posts-btn').click(function (e) {
    e.preventDefault();
    var postsURL = $(this).attr("data-href");

    req = $.ajax({
        url: postsURL,
        type: 'GET',
        data: {},
        success: function (data) {
            console.log(data)
        }, error: function (error) {
            console.log(error)
            console.log("error")

        }

    });
    req.done(function (data) {
        $('#feed-content').css('display', 'block');
        $('#session-content').css('display', 'none');
    });
});
$('.live-list').ready(function () {
    $('.live-list').css('display', 'flex');
//    $('.live').click(function (e) {
//        e.preventDefault();
        var liveUrl = '/liveDetails?liveId=';
        var liveInfoUrl = '/liveInfo?liveId=';
        var userUrl = '/userDetails?user_id='

        req = $.ajax({
            url: '/liveSession',
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        req.done(function (data) {
            var obj = data.result;
//            $('.live-list').empty();
            $.each(obj, function (key, value) {


                $('.live-list').append('<card class="card shadow-lg live-card"  data-href="' + liveUrl + value.id + '" > <card ><a href="' + liveInfoUrl + value.id + '"> <div class="live-img-wrapper"><img class="live-img" src="../static/coverImages/' + value.coverImg + '" alt=""></div> <div class="live-profile-pic-wrapper click-pro-pic"  data-href="' + userUrl + value.host.id + '"><span><a  class="user-profile-pic border-light" href="#"><img class="profilepic"  src="' + value.userImg + '" alt=""></a></span> </div><div class="p-2 row no-gutters"><span class="live-info col-8 flex-content flex-column no-gutters"><span class="live-title">' + value.title + '</span><span class="">Hosted by:' + value.host + ' </span><span class="">Category:' + value.category + '</span><span class=""> </span></span>  <span class="live-info col-4 flex-content flex-column no-gutters">           <span class="text-right">' + value.startTime + '-' + value.endTime + '</span><span class="text-right">' + value.date + '</span>  <div class="circle-icon text-right text-center mt-2  p-2 shadow-sm"> </div> </span> </div> </a></card> </card>');

            });
            $('#live').css('display', 'block');
            $('.live-list').css('display', 'flex');
            
            
            
            
            $('#user-profile').css('display', 'none');
            $('.checkout').css('display', 'none')
        });


//    });
    $('.share-btn').click(function (e) {
        var fbDesc = $('.share-logos').attr('desc');
        var fbCoverImg = 'https://www.100chinaguide.com/static/coverImages/' + $('.share-logos').attr('coverImg');;
        var fbTitle = $('.share-logos').attr('title');
        var url      = window.location.href;
        e.preventDefault();
        $('.fb-share-button').attr('data-href',url)
        $('#fb-share-img').attr('content',fbCoverImg)
        $('#fb-share-title').attr('content',fbTitle)
        $('#fb-share-description').attr('content',fbDesc)
        $('.fb-share-button').appendTo('.share-logos')
        $('.share-logos').toggle()



    });


});

$('.profile').ready(function () {
//    $('.profile-nav').click(function (e) {
        $('#user-profile').css('display', 'block');
        $('.loader').css('display', 'none');
        
        
        
        var param = $.urlParam('user_id');
        var url = '/userDetails?user_id='+ param;
        
        
        $('#create-course').css('display', 'none');
        $('#course-update').css('display', 'none');
        $('#live-update').css('display', 'none');
        $('.checkout').css('display', 'none')

        req = $.ajax({
            url: url,
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        req.done(function (data) {


            $('.my-profile').css('display', 'block');


            $('#my-username').html(data.username);
            $('#my-videos').html(data.videos);
            $('#my-followers').html(data.followers);
            $('#my-live-sessions').html(data.liveSessions);
            $('#my-introduction').html(data.introduction);
            $('.user-form').css('display', 'none');
            $('img.profilepic').attr("src",  data.userImage);
            $('#user-profile').css('display', 'block');
            $('#live').css('display', 'none');
            
            $('.checkout').css('display', 'none');
            $('.schedule').css('display', 'none');

//        });


    });
    $('#edit-profile').click(function (e) {
        e.preventDefault();


        req = $.ajax({
            url: $(this).attr('data-href'),
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        req.done(function (data) {
            var tog = $('.user-form').css('display');
            $('.user-form').css('display', 'none')
            if (tog === 'block') {

                $('.user-form').css('display', 'none')
                $('#my-introduction').css('display', 'block')

            } else if (tog === 'none') {
                $('.user-form').css('display', 'block')
                $('#my-introduction').css('display', 'none')
            }


            $('#introduction').html(data.introduction);
            $('#introVideo').val(data.introVideo);
            $('#fullname').val(data.fullname);
            $('#username').val(data.username);
            $('#email').val(data.email);
            $('#password').val(data.password);
            $('#status').val(data.status);


        });


    });

    $('#posts-btn').click(function (e) {
        e.preventDefault();
        var postsURL = $(this).attr("data-href");

        req = $.ajax({
            url: postsURL,
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        req.done(function (data) {
            $('#feed-content').css('display', 'block');
            $('#session-content').css('display', 'none');
        });
    });
});




function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.getElementById("main").style.marginRight = "250px";
    $('#main').css('display', 'none');
    $('.navbar-brand').css('display', 'none');
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main").style.marginRight = "0";
    document.body.style.backgroundColor = "white";
    $('#main').css('display', 'block');
    $('.navbar-brand').css('display', 'block');


}


function openLeftNav() {
    document.getElementById("leftSidenav").style.width = "80%";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
    $('#main').css('display', 'none');
    $('.navbar-brand').css('display', 'none');
}

function closeLeftNav() {
    document.getElementById("leftSidenav").style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.body.style.backgroundColor = "white";
    $('#main').css('display', 'block');
    $('.navbar-brand').css('display', 'block');

}


// $('.video-details').ready(function () {
// //    $('.upload-list').on("click", '.thumb-wrapper', function (e) {
//
//         $('.loader').css('display', 'block');
// //        e.preventDefault();
//         var vidParam = $.urlParam('videoId')
//         var url = '/videoDetails?videoId='+vidParam;
//         var videoSrc = "../static/videos/";
//         var userImgSrc = "../static/profile_pics/";
//         var userUrl = "/userDetails?user_id=";
//         var courseUrl = "/editSeries?series_id=";
//         var commentUrl = "/comment?series_id=";
//         var currency = "￥";
//         var coverImgUrl = '../static/coverImages/';
//
//         req = $.ajax({
//             url: url,
//             type: 'GET',
//             data: {},
//             success: function (data) {
//                 console.log(data)
//             }, error: function (error) {
//                 console.log(error)
//                 console.log("error")
//
//             }
//
//         });
//         req.done(function (data) {
//
//             var obj = data.result;
//             $('.addCart').attr('data-href', '/addCart?upload_id=' + obj.id);
//             $('.removeCart').attr('data-href', '/addCart?upload_id=' + obj.id);
//                         $('#user-reviews').empty();
//             $.each(obj.comments, function (key, value) {
//
//
//                 $('#user-reviews').append('<div><div data-href="" class="profile-pic-wrapper d-inline-flex mr-2 click-pro-pic"><span><img class="profilepic" src="' + userImgSrc + value.proPic + '" alt=""></span></div><small ><strong>' + value.username + '</strong></small><div><small id="user-review">' + value.content + '</small></div></div></div></div>');
//
//             });
//             if (obj.inCart === true) {
//                 $('.navLink.removeCart').css('display', 'flex');
//
//                 $('.navLink.addCart').css('display', 'none');
//             } else if (obj.inCart === false) {
//                 $('.navLink.addCart').css('display', 'flex');
//
//                 $('.navLink.removeCart').css('display', 'none');
//             }
//
//             if (obj.hasLiked === true) {
//                 $('#unlike-btn').css('display', 'flex');
//
//                 $('.like-btn').css('display', 'none');
//             } else if (obj.hasLiked === false) {
//                 $('.like-btn').css('display', 'flex');
//
//                 $('#unlike-btn').css('display', 'none');
//
//             }
//
//             $('.profile-pic-wrapper').attr("data-href", userUrl + obj.username);
//             $('#comment-form').attr("data-href", commentUrl + obj.id);
//             $('.buy').attr("data-href", courseUrl + obj.id);
//             $('#video-title').html(obj.title);
//             $('#video-author').html(obj.username);
//             $('#video-likes').html(obj.likes);
//             $('#video-comments').html(obj.totalComments);
//             $('#video-description').html(obj.description);
//             $('.share-logos').attr('desc',obj.description);
//             $('.share-logos').attr('title',obj.title);
//             $('.share-logos').attr('coverImg',obj.coverImg);
//             $('#video-description img').css('width', '100%');
//             $('#video-price').html(currency + obj.price);
//             $('#video-price').css("fontSize", "17px");
//             $('img.profilepic').attr("src", userImgSrc + obj.userImg);
//             $('#user-profile').css('display', 'none');
//             $('.checkout').css('display', 'none')
//             $('#comment-nav').css('display', 'none')
//             $('#course-update').css('display', 'none')
//
//             $('.schedule').css('display', 'none')
//             $('#video-bot-nav').css('display', 'flex')
//             $('#create-series').css('display', 'none');
//             $('.video-details').css('display', 'flex');
//             $('.loader').css('display', 'none');
//             $('#episode').empty();
//             if (obj.price == 0) {
//                 $('#video-price').css('display', 'none');
//                 $('.addCart').css('display', 'none');
//                 $('.buy').css('display', 'none');
//             } else {
//                 $('#video-price').css('display', 'flex');
//
//                 $('.buy').css('display', 'flex');
//             }
//             if (obj.isSeries === true  ) {
//                 $('.like-btn').attr('data-href', '/like/episode' + obj.id);
//                 $('#unlike-btn').attr('data-href', '/unlike/episode' + obj.id);
//                 $('#episode-tab').css('display', 'block');
//                 $('#episode-subtitle').css('display', 'block');
//
//                 $.each(obj.episode, function (key, value) {
//
//                     $('#episode').append('<div class="card shadow-sm click-episode" data-href="/getEpisode?episode_id=' + value.episodeId + '" ><div class="p-2"><span><img src="../static/play.svg" alt="" width="12"><span id="episode-title" class="mr-2 ml-5">' + value.subtitle + '</span><span id="episode-duration"></span></span></div></div>')
//
//                 });
//             } else if (obj.isSeries === false) {
//                 $('.like-btn').attr('data-href', '/like/video' + obj.id);
//                 $('#unlike-btn').attr('data-href', '/unlike/video' + obj.id);
//
//                 $('#episode-tab').css('display', 'none');
//                 $('#episode-subtitle').css('display', 'none');
//
//
//             }
//             if (obj.type === 'video') {
//                 $('video').attr("src", videoSrc + obj.videoRef);
//                 $('video').css('display', 'block');
//                 $('#episode-subtitle').text(obj.episode.subtitle);
//
//                 $('.video-js').attr("src", videoSrc + obj.videoRef);
//                 $('#controls').css('display', 'none');
//                 $('video').css('display', 'block');
//                 $('.course-img').css('display', 'none');
//             } else if (obj.type === 'audio') {
//
//                 $('#audio-file').attr("audioFile", obj.videoRef);
//                 $('.course-img').css('display', 'block');
//                 $('.course-img').attr("src", coverImgUrl + obj.coverImg);
//                 var audioSrc = '/static/videos/' + $('#audio-file').attr('audioFile')
//                 $('#controls').css('display', 'flex');
//                 popover('Loading Audio..Please wait','success')
//                 wavesurfer.load(audioSrc);
//                 wavesurfer.on('ready', function () {
//                     popover('Audio ready to play','success')
//                             $('.loader').css('display', 'none')
//
//
//         $('#pause-btn').on('click', function () {
//             wavesurfer.pause();
//             $('#play-btn').css('display', 'flex')
//             $('#pause-btn').css('display', 'none')
//         });
//            $('#play-btn').on('click', function () {
//             wavesurfer.play();
//             $('#play-btn').css('display', 'none')
//             $('#pause-btn').css('display', 'flex')
//         });});
//
//
//
//
//                 $('#episode-subtitle').text(obj.episode.subtitle);
//
//
//
//
//
//
//                 $('video').css('display', 'none');
//
//
//
//             } else if (obj.videoRef == null) {
//                 var ep = obj.episode[0];
//
//
//                 $('video').attr("src", videoSrc + obj.episode[0].videoRef);
//
//                 $('#video-likes').text(ep.likes);
//                 $('video').css('display', 'block');
//                 $('#episode-subtitle').text(ep.subtitle);
//                 $('.video-js').attr("src", videoSrc +obj.episode[0].videoRef);
//
//                 $('video').css('display', 'block');
//                 $('.course-img').css('display', 'none');
//                 $('.like-btn').attr('data-href', '/like/episode' + obj.episode[0].episodeId);
//                 $('#unlike-btn').attr('data-href', '/unlike/episode' + obj.episode[0].episodeId);
//             }
//
//
//
//             if (data.result.episode[0].hasLikedEpisode === true) {
//                     $('#unlike-btn').css('display', 'flex');
//
//                     $('.like-btn').css('display', 'none');
//             }   else if (data.result.episode[0].hasLikedEpisode === false) {
//                     $('.like-btn').css('display', 'flex');
//
//                     $('#unlike-btn').css('display', 'none');
//             }
//
//
//
//
//
//
//
//
//     });
//         });



    $('#main').on("click", ".click-pro-pic", function (e) {
         
        e.preventDefault();
        var url = $(this).attr("data-href");
        var videoSrc = "../static/videos/";
        var userImgSrc = "../static/profile_pics/";
        var currency = "￥";
        var followUrl = "/follow";
        var unfollowUrl = "/unfollow";
        var userUrl = "/userDetails?user_id=";

        req = $.ajax({
            url: url,
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        req.done(function (data) {

            $('.profile').css('display', 'block');
            $('.share-logos').css('display', 'none');
            $('#book-schedule-btn').attr('data-href', userUrl + data.username);
            $('#unfollow').attr('data-href', unfollowUrl + "/" + data.username);
            $('#follow').attr('data-href', followUrl + "/" + data.username);
            if (data.Isfollowing === true) {

                $('#unfollow').css('display', 'inline-block');
                $('#follow').css('display', 'none');


            } else {


                $('#follow').css('display', 'inline-block');
                $('#unfollow').css('display', 'none');


            }


            $('#user-username').html(data.username);
            $('#user-videos').html(data.videos);
            $('#user-followers').html(data.followers);
            $('#user-live-sessions').html(data.liveSessions);
            $('#user-introduction').html(data.introduction);
            $('img.profilepic').attr("src",  data.userImage);
            $('#user-profile').css('display', 'none');
            $('#live').css('display', 'none');
            
            $('.checkout').css('display', 'none');
            $('.live-list').css('display', 'none');
            $('.upload-list').css('display', 'none');
            $('.video-details').css('display', 'none');
            $('.live-details').css('display', 'none');

        });


    });
    $('.video-details').on("click", ".click-episode", function (e) {
        e.preventDefault();
        var url = $(this).attr("data-href");
        var videoSrc = "../static/videos/";
        var userImgSrc = "../static/profile_pics/";
        var currency = "￥";
        var followUrl = "/follow";
        var commentUrl = "/episodeComment?episode_id=";
        var unfollowUrl = "/unfollow";

        req = $.ajax({
            url: url,
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        req.done(function (data) {

            var obj = data.result;
            $('#video-likes').text(obj.likes)
            $('#video-comments').text(obj.comments)
            $('#episode-subtitle').text(obj.subtitle)
            if (obj.hasLikedEpisode == true) {
                $('#unlike-btn').css('display', 'flex');

                $('.like-btn').css('display', 'none');
            } else if (obj.hasLikedEpisode == false) {
                $('.like-btn').css('display', 'flex');

                $('#unlike-btn').css('display', 'none');
            }
                $('.like-btn').attr('data-href', '/like/episode' + obj.id);
                $('#unlike-btn').attr('data-href', '/unlike/episode' + obj.id);

            if (obj.type == 'video') {
                $('video').attr("src", videoSrc + obj.video);
                $('video').css('display', 'block');
                $('.video-js').attr("src", videoSrc + obj.video);
                $('.audio').css('display', 'none');
                $('video').css('display', 'block');
                $('.course-img').css('display', 'none');

            } else if (obj.type == 'audio') {
                $('source').attr("src", videoSrc + obj.video);
                $('.audio').css('display', 'block');
                $('video').css('display', 'none');
                $('.course-img').css('display', 'block');

            }
            else if (obj.videoRef == null) {
                $('.course-img').attr("src", coverImgSrc + obj.coverImg);
                $('.audio').css('display', 'none');
                $('.course-img').css('display', 'block');
                $('video').css('display', 'none');
            }

            
              $('#user-reviews').empty();
            $.each(obj.comments, function (key, value) {


                $('#user-reviews').append('<div><div data-href="" class="profile-pic-wrapper d-inline-flex mr-2 click-pro-pic"><span><img class="profilepic" src="'  + value.proPic + '" alt=""></span></div><small ><strong>' + value.username + '</strong></small><div><small id="user-review">' + value.content + '</small></div></div></div></div>');

            });

            $('#user-profile').css('display', 'none');
            $('#episode-description').append('<div><span>Episode Summary</span></div>')
            $('#episode-description').html(obj.description);
            $('#comment-form').attr("data-href", commentUrl + obj.id);
            $('.checkout').css('display', 'none')


        });


    });


    $('#schedule-create').on("click", function (e) {
        e.preventDefault();
        closeNav()
        $('.schedule').css('display', 'block');
        $(".calendar-source").detach().prependTo("#schedule-form");


        $('#calendar').css('display', 'block');
        $('.schedule-btn').css('display', 'block');
        $('#live').css('display', 'none');
        $('.live-list').css('display', 'none');
        $('.live-details').css('display', 'none');

        
        $('.my-profile').css('display', 'none');
        $('#create-course').css('display', 'none');
        $('.video-details').css('display', 'none');
        $('.upload-list').css('display', 'none');
        $('#user-profile').css('display', 'none');
        $('#live-update').css('display', 'none');
        $('.schedule-container').css('display', 'none');
        $('.checkout').css('display', 'none')
        $('.fc-toolbar h2').css('display', 'none')
        $('#course-update').css('display', 'none');
        $('.upload-option').css('display', 'none');


    });


    $('#live-update').on("click", ".edit-live", function (e) {
        e.preventDefault();
        liveUrl = 'editLive?live_id='
        closeNav()
        req = $.ajax({
            url: $(this).attr('data-href'),
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });

        req.done(function (data) {
            $('#update-session-form').attr('data-href', liveUrl + data.result.id);
            $('#update_session_title').val(data.result.title);
            $('#update_session_description').val(data.result.description);
            $('#update_session_category').val(data.result.category);

            $('.schedule').css('display', 'none');
            $(".calendar-source").detach().appendTo(".append-edit-calendar");
            $('.fc-toolbar h2').css('display', 'none')


            $('#calendar').css('display', 'block');
            $('#edit-live').css('display', 'block');
            $('#live').css('display', 'none');
            $('#live-update').css('display', 'none');
            
            
            $('#create-course').css('display', 'none');
            
            
            $('#user-profile').css('display', 'none');
            $('.checkout').css('display', 'none')
        });


    });
    $('.schedule-container').on("click", ".edit-schedule", function (e) {
        e.preventDefault();
        closeNav()
        req = $.ajax({
            url: $(this).attr('data-href'),
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });

        req.done(function (data) {


            $('.schedule').css('display', 'none');
            $(".calendar-source").detach().prependTo("#update-schedule-form");
            $('.fc-toolbar h2').css('display', 'none')

            $('#calendar').css('display', 'block');
            $('#update-schedule').css('display', 'block');
            $('#edit-live').css('display', 'none');
            $('#live').css('display', 'none');
            $('#live-update').css('display', 'none');
            $('.my-profile').css('display', 'none');
            $('#create-course').css('display', 'none');
            
            
            $('#user-profile').css('display', 'none');
            $('.schedule-container').css('display', 'none');
        });


    });


    $('#course-create').on("click", function (e) {
        e.preventDefault();
        closeNav()
        $(".editor-source").detach().appendTo(".form-editor");
        $('.editor-source').css('display', 'none')
        $('#live').css('display', 'none');
        $('.live-details').css('display', 'none');
        $('#create-live').css('display', 'none');
        $('.schedule').css('display', 'none');
        $('.live-list').css('display', 'none');
        $('#course-upload').css('display', 'none');
        $('#course-update').css('display', 'none');
        $('#create-series').css('display', 'none');
        $('.my-profile').css('display', 'none');
        $('#create-course').css('display', 'none');
        $('.video-details').css('display', 'none');
        $('.upload-list').css('display', 'none');
        $('#user-profile').css('display', 'none');

        $('.schedule-container').css('display', 'none');
        $('#live-update').css('display', 'none');
        $('.upload-option').css('display', 'block');

    });
    $('#course-update').on("click","a.add-ep-btn", function (e) {
        e.preventDefault();
        closeNav()
        $(".editor-source").detach().appendTo(".episode-editor");
            $('.editor-source').css('display', 'block')

    });


    $('#series-stats').on("click", function (e) {
        e.preventDefault();
        closeNav()
        req = $.ajax({
            url: $('#update-course').attr('data-href'),
            type: 'GET',
            data: {},

            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        $('.series-stats').empty();

        req.done(function (data) {
            console.log(data.length)
            if (data.length == 0)
                $('#course-update').append('<p>No contents</p>')

            else
                $.each(data.result, function (key, value) {


                    $('.series-stats').append('<card class="mt-2 mb-2 flex-fill flex-row shadow-lg row no-gutters user-course card"><div class="col-3 no-gutters cover-wrapper"><img id="course-img" src="../static/coverImages/' + value.coverImg + '" alt=""></div><div class="col-8 p-2 flex-fill flex-column no-gutters "><h6 id="course-title">' + value.title + '</h6><div id="total-episodes">Episodes : ' + value.totalEpisodes + '</div><span id="course-price">Price : ' + value.price + '</span><nav class="btn-row" ><a   class=" navLink" data-href="addEpisode?series_id=' + value.id + '"  data-toggle="modal" data-target="#episode-modal" href=""><img class="mobile-icon" src="../static/like.svg" alt=""><span class="nav_text">' + value.likes + '</span></a><a class="navLink"   data-toggle="modal" data-target="#myModal" href="" ><img class="mobile-icon" src="../static/commentGrey.svg" alt="" ><span class="nav_text">' + value.totalComments + '</span></a><a class="navLink"><img class="mobile-icon" src="../static/eye.svg" alt="" width="24" ><span class="nav_text view-text"></span></a></nav></div></card></div>');

                });


            $('#course-update').css('display', 'none');
            $('#live').css('display', 'none');
            $('.live-list').css('display', 'none');
            $('.live-details').css('display', 'none');

            $('#create-live').css('display', 'none');
            $('#live-update').css('display', 'none');
            $('.schedule').css('display', 'none');
            $('#course-upload').css('display', 'none');
            $('#create-series').css('display', 'none');
            $('.my-profile').css('display', 'none');
            $('#create-course').css('display', 'none');
            $('.video-details').css('display', 'none');
            $('.upload-list').css('display', 'none');
            $('.upload-option').css('display', 'none');
            $('#user-profile').css('display', 'none');
            $('.series-stats').css('display', 'block');


        });
    });
    $('#bought-courses').on("click", function (e) {
        e.preventDefault();
        closeNav()
        req = $.ajax({
            url: $(this).attr('data-href'),
            type: 'GET',
            data: {},

            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        $('.bought-courses').empty();

        req.done(function (data) {
            console.log(data.length)
            if (data.length == 0)
                $('.bought-courses').append('<p>No contents</p>')

            else
                $.each(data.result, function (key, value) {


                    $('.bought-courses').append('<a href="/videoInfo?videoId='+ value.id +'" class="mt-2 mb-2 flex-fill flex-row text-dark text-decoration-none shadow-lg row no-gutters user-course card"><div class="col-3 no-gutters cover-wrapper"><img id="course-img" src="../static/coverImages/' + value.coverImg + '" alt=""></div><div class="col-8 p-2 flex-fill flex-column no-gutters "><h6 id="course-title">' + value.title + '</h6><span id="course-price">Price : ' + value.price + '</span></div></a>');

                });


            $('#course-update').css('display', 'none');
            $('#live').css('display', 'none');
            $('.live-list').css('display', 'none');
            $('.live-details').css('display', 'none');

            $('#create-live').css('display', 'none');
            $('#live-update').css('display', 'none');
            $('.schedule').css('display', 'none');
            $('#course-upload').css('display', 'none');
            $('#create-series').css('display', 'none');
            $('.my-profile').css('display', 'none');
            $('#create-course').css('display', 'none');
            $('.video-details').css('display', 'none');
            $('.upload-list').css('display', 'none');
            $('.upload-option').css('display', 'none');
            $('#user-profile').css('display', 'none');
            $('.series-stats').css('display', 'none');
            $('.bought-courses').css('display', 'block');


        });
    });
    $('#live-stats').on("click", function (e) {
        e.preventDefault();
        closeNav()
        req = $.ajax({
            url: $(this).attr('data-href'),
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        $('.live-stats').empty();

        req.done(function (data) {
            console.log(data.length)
            if (data.length == 0)
                $('#course-update').append('<p>No contents</p>')

            else
                $.each(data.result, function (key, value) {


                    $('.live-stats').append('<card class="mt-2 mb-2 flex-fill flex-row shadow-lg row no-gutters user-course card"><div class="col-3 no-gutters cover-wrapper"><img id="course-img" src="../static/coverImages/' + value.coverImg + '" alt=""></div><div class="col-8 p-2 flex-fill flex-column no-gutters "><h6 id="course-title">' + value.title + '</h6><div id="total-episodes"> </div><nav class="btn-row" ><a   class=" navLink" data-href="addEpisode?series_id=' + value.id + '"  data-toggle="modal" data-target="#episode-modal" href=""><img class="mobile-icon" src="../static/like.svg" alt=""><span class="nav_text">' + value.likes + '</span></a><a class="navLink"   data-toggle="modal" data-target="#myModal" href="" ><img class="mobile-icon" src="../static/commentGrey.svg" alt="" ><span class="nav_text">' + value.totalComments + '</span></a><a class="navLink"><img class="mobile-icon" src="../static/eye.svg" width="24" alt="" ><span class="nav_text view-text"></span></a></nav></div></card></div>');

                });


            $('#course-update').css('display', 'none');
            $('#live').css('display', 'none');
            $('.live-list').css('display', 'none');
            $('.live-details').css('display', 'none');
            $('.video-details').css('display', 'none');

            $('#create-live').css('display', 'none');
            $('#live-update').css('display', 'none');
            $('.schedule').css('display', 'none');
            $('#course-upload').css('display', 'none');
            $('#create-series').css('display', 'none');
            $('.my-profile').css('display', 'none');
            $('#create-course').css('display', 'none');
            $('.video-details').css('display', 'none');
            $('.upload-list').css('display', 'none');
            $('.upload-option').css('display', 'none');
            $('#user-profile').css('display', 'none');
            $('.series-stats').css('display', 'none');
            $('.live-stats').css('display', 'block');
            $('.booked-schedule').css('display', 'none');
            $('.booked-live').css('display', 'none');


        });
    });
    $('#booked-schedule').on("click", function (e) {
        e.preventDefault();
        closeNav()
        req = $.ajax({
            url: $(this).attr('data-href'),
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        $('.booked-schedule').empty();

        req.done(function (data) {

            console.log(data.length)
            $('.click-unbook').css('display','flex')
            if (data.length == 0)
                $('#course-update').append('<p>No contents</p>')

            else
                $.each(data.result, function (key, value) {


                    $('.booked-schedule').append('<div class=" text-center p-2 bg-dark text-light schedule-box"><h4>' + value.date + '</h4><span>' + value.start_time + ' - ' + value.end_time + '</span><div class="row w-100"><div class="w-100 col h-50 text-light text-center d-flex my-green"><a class="p-2 text-light" href="' + value.meetingUrl + '">JOIN</a></div><div class="w-100 col h-50 text-light text-center my-green"><a id="unbook-schedule" class="p-2 text-light d-flex click-unbook" data-href="/unbook/'+value.id+'?type=schedule" href="" >UNBOOK</a></div></div></div></div>');

                });
        });


        $('#course-update').css('display', 'none');
        $('#live').css('display', 'none');
        $('.live-list').css('display', 'none');
        $('.live-details').css('display', 'none');
        $('.video-details').css('display', 'none');

        $('#create-live').css('display', 'none');
        $('#live-update').css('display', 'none');
        $('.schedule').css('display', 'none');
        $('#course-upload').css('display', 'none');
        $('#create-series').css('display', 'none');
        $('.my-profile').css('display', 'none');
        $('#create-course').css('display', 'none');
        $('.video-details').css('display', 'none');
        $('.upload-list').css('display', 'none');
        $('.upload-option').css('display', 'none');
        $('#user-profile').css('display', 'none');
        $('.series-stats').css('display', 'block');


    });
    $('#booked-live').on("click", function (e) {
        e.preventDefault();
        closeNav()
        req = $.ajax({
            url: $(this).attr('data-href'),
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        $('.booked-live').empty();

        req.done(function (data) {
            console.log(data.length)
            if (data.length == 0)
                $('#course-update').append('<p>No contents</p>')

            else
                $.each(data.result, function (key, value) {


                    $('.booked-live').append('<div class=" text-center p-2 bg-dark text-light schedule-box"><h4 class="flex-wrap">'+ value.title +'</h4><h4>' + value.date + '</h4><span>' + value.startTime + ' - ' + value.endTime + '</span><div class="row w-100"><div class=" col h-50 text-light text-center d-flex my-green"><a class="p-2 text-light" href="' + value.meetingUrl + '">JOIN</a></div><div class="w-100 col h-50 text-light text-center my-green"><a id="unbook" class="p-2 text-light  click-unbook" data-href="/unbook/'+value.id+'?type=schedule" href="" >UNBOOK</a></div></div></div></div>');
                });
        });


        $('#course-update').css('display', 'none');
        $('#live').css('display', 'none');
        $('.live-list').css('display', 'none');
        $('.live-details').css('display', 'none');
        $('.video-details').css('display', 'none');

        $('#create-live').css('display', 'none');
        $('#live-update').css('display', 'none');
        $('.live-details').css('display', 'none');
        $('.schedule').css('display', 'none');
        $('#course-upload').css('display', 'none');
        $('#create-series').css('display', 'none');
        $('.my-profile').css('display', 'none');
        $('#create-course').css('display', 'none');
        $('.video-details').css('display', 'none');
        $('.upload-list').css('display', 'none');
        $('.upload-option').css('display', 'none');
        $('#user-profile').css('display', 'none');
        $('.series-stats').css('display', 'block');


    });
    $('#schedule-stats').on("click", function (e) {
        e.preventDefault();
        closeNav()
        req = $.ajax({
            url: $(this).attr('data-href'),
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        $('.schedule-stats').empty();

        req.done(function (data) {
            console.log(data.length)
            if (data.length == 0)
                $('.schedule-stats').append('<p>No contents</p>')

            else
                $.each(data.result, function (key, value) {


                    $('.schedule-stats').append('<div class=" text-center p-2 bg-dark text-light schedule-box"><h4>' + value.date + '</h4><span>' + value.start_time + ' - ' + value.end_time + '</span><nav class="btn-row" ></nav></div>');
                });
        });


        $('#course-update').css('display', 'none');
        $('#live').css('display', 'none');
        $('.live-details').css('display', 'none');
        $('.video-details').css('display', 'none');

        $('#create-live').css('display', 'none');
        $('#live-update').css('display', 'none');
        $('.schedule').css('display', 'none');
        $('#course-upload').css('display', 'none');
        $('#create-series').css('display', 'none');
        $('.my-profile').css('display', 'none');
        $('#create-course').css('display', 'none');
        $('.video-details').css('display', 'none');
        $('.upload-list').css('display', 'none');
        $('.upload-option').css('display', 'none');
        $('#user-profile').css('display', 'none');
        $('.series-stats').css('display', 'none');
        $('.booked-schedule').css('display', 'none');
        $('.schedule-stats').css('display', 'block');


    });


    $('#live-create').on("click", function (e) {
        e.preventDefault();
        closeNav()
        $(".calendar-source").detach().appendTo(".append-calendar");
        $('#live').css('display', 'none');
        $('.live-list').css('display', 'none');
        $('.video-details').css('display', 'none');
        $('.live-details').css('display', 'none');

        $('#create-live').css('display', 'block');
        $('#calendar').css('display', 'block');
        $('.schedule').css('display', 'none');
        $('#course-upload').css('display', 'none');
        $('#create-series').css('display', 'none');
        $('.my-profile').css('display', 'none');
        $('#create-course').css('display', 'block');
        $('.video-details').css('display', 'none');
        
        $('.upload-list').css('display', 'none');
        $('#user-profile').css('display', 'none');
        $('.schedule-container').css('display', 'none');
        $('#live-update').css('display', 'none');
        $('.fc-toolbar h2').css('display', 'none')

    });
    $('#single-click').on("click", function (e) {
        e.preventDefault();

        $(".editor-source").detach().appendTo(".form-editor");
        $('.editor-source').css('display', 'block')
        $('#live').css('display', 'none');
        
        $('#create-live').css('display', 'none');
        $('.schedule').css('display', 'none');
        $('#course-upload').css('display', 'block');
        $('#create-series').css('display', 'none');
        
        $('#create-course').css('display', 'block');
        
        
        $('#user-profile').css('display', 'none');

        $('.schedule-container').css('display', 'none');
        $('#live-update').css('display', 'none');
        $('.upload-option').css('display', 'none');

    });
    $('#series-click').on("click", function (e) {
        e.preventDefault();

        $(".editor-source").detach().appendTo(".series-form-editor");
        $('.editor-source').css('display', 'block')
        $('#live').css('display', 'none');
        
        $('#create-live').css('display', 'none');
        $('.schedule').css('display', 'none');
        $('#course-upload').css('display', 'none');
        $('#create-series').css('display', 'block');
        
        $('#create-course').css('display', 'block');
        
        
        $('#user-profile').css('display', 'none');

        $('.schedule-container').css('display', 'none');
        $('#live-update').css('display', 'none');
        $('.upload-option').css('display', 'none');

    });

    $('#update-course').on("click", function (e) {
        e.preventDefault();
        closeNav()
        seriesUrl = '/editSeries?series_id='
        req = $.ajax({
            url: $(this).attr('data-href'),
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        $('#course-update').empty();

        req.done(function (data) {


            if (data.length == 0)
                $('#course-update').append('<p>No contents</p>')

            else

                $.each(data.result, function (key, value) {
                    if (value.approved === false)
                        var status = 'Under review'
                    else if (value.approved === true)
                        var status = 'Reviewed'

                    if (value.isSeries == true)


                        $('#course-update').append('<card class="mt-2 mb-2 flex-fill flex-row shadow-lg row no-gutters user-course card"><div class="col-3 no-gutters cover-wrapper"><img id="course-img" src="../static/coverImages/' + value.coverImg + '" alt=""></div><div class="col-8 p-2 flex-fill flex-column no-gutters "><h6 id="course-title">' + value.title + '</h6><div id="total-episodes">Episodes : ' + value.totalEpisodes + '</div><span id="course-price">Price : ' + value.price + '</span><div id="course-status" class="text-info">Status : ' + status + '</div><nav class="btn-row" ><a   class="add-ep-btn navLink" data-href="addEpisode?series_id=' + value.id + '"  data-toggle="modal" data-target="#episode-modal" href=""><img class="mobile-icon" src="../static/add.svg" alt=""><span class="nav_text">Add  Episode</span></a><a class="navLink"   data-toggle="modal" data-target="#myModal" href="" ><img class="mobile-icon" src="../static/delete.svg" alt="" ><span class="nav_text">Delete</span></a><a   data-href="' + seriesUrl + value.id + '" class="edit-series navLink" data-toggle="modal" data-target="#series-modal" href=""><img class="mobile-icon" src="../static/edit.svg" alt="" ><span class="nav_text">Edit</span></a></nav></div></card></div>');
                    else if (value.isSeries == false) {


                        $('#course-update').append('<card class="mt-2 mb-2 flex-fill flex-row shadow-lg row no-gutters user-course card"><div class="col-3 no-gutters cover-wrapper"><img id="course-img" src="../static/coverImages/' + value.coverImg + '" alt=""></div><div class="col-8 p-2 flex-fill flex-column no-gutters "><h6 id="course-title">' + value.title + '</h6><div id="total-episodes"></div><span id="course-price">Price : ' + value.price + '</span><div id="course-status" class="text-info">Status : ' + status + '</div><nav class="btn-row" ><a class="navLink"   data-toggle="modal" data-target="#myModal" href="" ><img class="mobile-icon" src="../static/delete.svg" alt="" ><span class="nav_text">Delete</span></a><a   data-href="' + seriesUrl + value.id + '" class="edit-series navLink" data-toggle="modal" data-target="#series-modal" href=""><img class="mobile-icon" src="../static/edit.svg" alt="" ><span class="nav_text">Edit</span></a></nav></div></card></div>');


                    }
                });


            $('#course-update').css('display', 'block');
            $('#live').css('display', 'none');
            $('.live-list').css('display', 'none');
            $('#create-live').css('display', 'none');
            $('#live-update').css('display', 'none');
            $('.schedule').css('display', 'none');
            $('.my-profile').css('display', 'none');
            $('#course-upload').css('display', 'none');
            $('#create-series').css('display', 'none');
            
            $('#create-course').css('display', 'none');
            $('.video-details').css('display', 'none');
            $('.upload-list').css('display', 'none');
            $('.upload-option').css('display', 'none');
            $('#user-profile').css('display', 'none');
            $('.live-details').css('display', 'none');
            


        });


    });
    $('#liked-course').on("click", function (e) {
        e.preventDefault();
        closeNav()
        userUrl = '/userDetails?user_id='
        req = $.ajax({
            url: $(this).attr('data-href'),
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        $('.liked-course-list').empty();

        req.done(function (data) {
            if (data.length == 0)
                $('#course-update').append('<p>No contents</p>')

            else

                $.each(data.likedSeries, function (key, value) {
                    $('.liked-course-list').append('<a href="/videoInfo?videoId='+ value.id +'" class="mt-2 mb-2 flex-fill flex-row text-dark text-decoration-none shadow-lg row no-gutters user-course card"><div class="col-3 no-gutters cover-wrapper"><img id="course-img" src="../static/coverImages/' + value.coverImg + '" alt=""></div><div class="col-8 p-2 flex-fill flex-column no-gutters "><h6 id="course-title">' + value.title + '</h6><div id="total-episodes">Episodes : ' + value.totalEpisodes + '</div><span id="course-price">Price : ' + value.price + '</span></div></a>');

                });


            $('#course-update').css('display', 'none');
            $('#live').css('display', 'none');
            $('.live-list').css('display', 'none');
            $('#create-live').css('display', 'none');
            $('#live-update').css('display', 'none');
            $('.schedule').css('display', 'none');
            $('.my-profile').css('display', 'none');
            $('#course-upload').css('display', 'none');
            $('#create-series').css('display', 'none');
            
            $('#create-course').css('display', 'none');
            $('.video-details').css('display', 'none');
            $('.upload-list').css('display', 'none');
            $('.upload-option').css('display', 'none');
            $('#user-profile').css('display', 'none');
            $('.live-details').css('display', 'none');



        });


    });
    $('#book-schedule-btn').on("click", function (e) {
        e.preventDefault();
        $('#book-schedule').modal('toggle')
        scheduleUrl = '/userDetails?user_id=';
        bookUrl = '/book/';
        unbookUrl = '/unbook/';
        param = '?type=';
        type = 'schedule';
        req = $.ajax({
            url: $(this).attr('data-href'),
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        $('.modal-body.append-user-schedule').empty();

        req.done(function (data) {

            var details = data.schedule

            $.each(details, function (key, value) {
                var cntId = value.id;
                $('.modal-body.append-user-schedule').append('<div class=" text-center p-2 bg-dark text-light schedule-box"><h4>' + value.date + '</h4><span>' + value.startTime + ' - ' + value.endTime + '</span><span class="mt-1"><a id="book-schedule-' + cntId + '" class="click-book" cnt="'+ value.id +'" data-href="' + bookUrl + value.id + param  + type + '"><button   class="fixed-btn" >Book</button></a><a  id="unbook-schedule-' + cntId + '" cnt="'+ value.id +'" class="click-unbook" data-href="' + unbookUrl + value.id + param  + type + '" ><button   class="fixed-btn" >Unbook</button></a></span></div>');

                if (value.hasBooked === true){

                    $('#book-schedule-' + cntId +'.click-book').css("display", "none");
                    $('#unbook-schedule-' + cntId +'.click-unbook').css("display", "flex");


                } else if (value.hasBooked === false){

                    $('#book-schedule-' + cntId +'.click-book').css("display", "flex");
                    $('#unbook-schedule-' + cntId +'.click-unbook').css("display", "none");

                }



            });


            $('#course-update').css('display', 'block');
            $('#live').css('display', 'none');

            $('#create-live').css('display', 'none');
            $('#live-update').css('display', 'none');
            $('.schedule').css('display', 'none');
            $('#course-upload').css('display', 'none');
            $('#create-series').css('display', 'none');
            $('.profile').css('display', 'block');
            $('#create-course').css('display', 'block');
            
            
            $('#user-profile').css('display', 'none');


        });


    });
    $('#main').on("click",'#bookers-list', function (e) {
        e.preventDefault();
        $('#bookers-modal').modal('toggle')
        scheduleUrl = '/userDetails?user_id=';
        bookUrl = '/book/';
        unbookUrl = '/unbook/';
        param = '?type=';
        type = 'schedule';
        req = $.ajax({
            url: $(this).attr('data-href'),
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        $('.modal-body.append-bookers').empty();

        req.done(function (data) {

            var details = data.result

            $.each(details.bookers, function (key, value) {

                $('.modal-body.append-bookers').append('<div class=" p-2 d-flex align-items-center "><div data-href="" class=" user-profile-pic-wrapper mr-2"><span><img class="profilepic" src="'+ value.profPic +'" alt=""></span></div><h6>' + value.username + '</h6></div>');




            });





        });


    });
    $('#main').on("click",'#live-bookers-list', function (e) {
        e.preventDefault();
        $('#bookers-live-modal').modal('toggle')
        scheduleUrl = '/userDetails?user_id=';
        bookUrl = '/book/';
        unbookUrl = '/unbook/';
        param = '?type=';
        type = 'schedule';
        req = $.ajax({
            url: $(this).attr('data-href'),
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        $('.modal-body.append-live-bookers').empty();

        req.done(function (data) {

            var details = data.result

            $.each(details.bookers, function (key, value) {

                $('.modal-body.append-live-bookers').append('<div class="  p-2 d-flex align-items-center "><div data-href="" class=" user-profile-pic-wrapper mr-2"><span><img class="profilepic" src="'+ value.profPic +'" alt=""></span></div><h6>' + value.username + '</h6></div>');




            });





        });


    });

    $('#edit-schedule').on("click", function (e) {
        e.preventDefault();
        closeNav()
        scheduleUrl = '/editSchedule?schedule_id='
        req = $.ajax({
            url: $(this).attr('data-href'),
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            },
            error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        $('.append-schedule').empty();
        req.done(function (data) {


            $.each(data.result, function (key, value) {
                $('.append-schedule').append('<div class=" text-center p-2 bg-dark text-light schedule-box"><h4>' + value.date + '</h4><span>' + value.start_time + ' - ' + value.end_time + '</span><nav class="btn-row" ><a  data-target="#bookers-modal" data-toggle="modal" data-href="' + scheduleUrl + value.id + '" class=" text-light navLink" id="bookers-list" href=""><img src="../static/profileWhite.svg" alt=""><span class="nav_text">Participants</span></a><a  data-href="' + scheduleUrl + value.id + '" class="edit-schedule text-light navLink" data-toggle="" data-target="" href=""><img src="../static/edit_w.svg" alt=""><span class="nav_text">Edit</span></a><a  data-href="' + scheduleUrl + value.id + '" class="delete-schedule navLink text-light" data-toggle="modal" data-target="#delete-schedule-modal" href="" ><img src="../static/delete_w.svg"  alt=""><span class="nav_text">Delete</span></a></nav><div class="w-100 h-50 text-light text-center my-green"><a class="p-2 text-light" href="' + value.meetingUrl + '">START</a></div></div>');
            });
            $('.update-schedule').css('display', 'block');


            $('#calendar').css('display', 'none');
            $('.update-schedule-btn').css('display', 'none');
            $('#live').css('display', 'none');
            $('.live-list').css('display', 'none');
            $('.live-details').css('display', 'none');
            $('.video-details').css('display', 'none');

            
            $('#create-course').css('display', 'none');
            $('#course-update').css('display', 'none');
            $('.video-details').css('display', 'none');
            $('.upload-list').css('display', 'none');
            $('#user-profile').css('display', 'none');
            $('.schedule-container').css('display', 'block');
            $('#live-update').css('display', 'none');
            $('.upload-option').css('display', 'none');
            $('#update-schedule').css('display', 'none');
            $('.schedule').css('display', 'none');
            $('.my-profile').css('display', 'none');

        });


    });

    $('#course-update').on("click", ".edit-series", function (e) {
        e.preventDefault();
        req = $.ajax({
            url: $(this).attr('data-href'),
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        req.done(function (data) {
            $(".editor-source").detach().appendTo(".update-series-editor");
            $('.editor-source').css('display', 'block')
            $('#update_series_title').val(data.title);
            $('.ql-editor').html(data.description);
            $('#update_series_price').val(data.price);
            $('#update_series_category').val(data.category);
            $('#series-update').attr('course-id', data.id);
            $('#create-series').css('display', 'none');


        });

    });

    $('#update-live').on("click", function (e) {
        e.preventDefault();
        closeNav()
        liveUrl = '/editLive?live_id='
        req = $.ajax({
            url: $(this).attr('data-href'),
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        req.done(function (data) {

            $('#live-update').empty();
            $.each(data.result, function (key, value) {

//        $('.start-btn').css('display',checkTime(value.startTime));

                $('#live-update').append('<card class="mt-2 mb-2 flex-fill flex-row shadow-lg row no-gutters user-course card live-url" id="' + value.id + '"><div class="col-3 no-gutters cover-wrapper"><img id="course-img" src="' + coverImgSrc + value.coverImg + '" alt=""></div><div class="col-6 p-2 flex-fill flex-column no-gutters "><h6 id="course-title">' + value.title + '</h6><div id="live-date">Date : ' + value.date + '</div><div id="live-time">Time : ' + value.startTime + '-' + value.endTime + '</div><nav class="btn-row"><a  data-target="#bookers-live-modal" data-toggle="modal" data-href="' + liveUrl + value.id + '" class="  navLink" id="live-bookers-list" href=""><img src="../static/profile.svg" alt=""><span class="nav_text">Participants</span></a></nav></div><div class="col-3"> <div class="start-btn  h-25 text-center "><a class="text-light" href="' + value.room + '"><div class="text-center">START</div></div></a><div class="edit-live h-25 bg-info " ><a  data-href="' + liveUrl + value.id + '" class="text-light edit-live" data-toggle="" data-target="" href=""><div class="text-center">EDIT</div></a></div><div class=" h-25 bg-danger " ><a  data-href="' + liveUrl + value.id + '" class="text-light delete-live"  data-toggle="modal" data-target="#delete-modal" href=""><div class="text-center">DELETE</div></a></div></div></card>');

            });
            $('#live-update').css('display', 'block');
            $('#course-update').css('display', 'none');
            $('.live-details').css('display', 'none');
            $('.video-details').css('display', 'none');
            $('#live').css('display', 'none');
            $('.live-list').css('display', 'none');

            $('#create-live').css('display', 'none');
            $('.schedule').css('display', 'none');
            $('#course-upload').css('display', 'none');
            $('#create-series').css('display', 'none');
            $('#course-update').css('display', 'none');
            $('.my-profile').css('display', 'none');
            $('#create-course').css('display', 'block');
            $('.video-details').css('display', 'none');
            $('.upload-list').css('display', 'none');
            $('.upload-option').css('display', 'none');
            $('#user-profile').css('display', 'none');
            $('#edit-live').css('display', 'none');
            $('.schedule-container').css('display', 'none');
            $('#create-series').css('display', 'none');
            $('.live-details').css('display', 'none');
            


        });


    });
    $('.yes-btn').on("click", function (e) {
        e.preventDefault();
        closeNav()
        liveUrl = '/editLive?live_id='
        req = $.ajax({
            url: $('.edit-series').attr('data-href'),
            type: 'DELETE',
            data: {},
            beforeSend: function(){
                popover('Deleting...','success')
            },
            success: function (data) {
                popover(data, 'success')
            }, error: function (error) {
                console.log(error)
                popover(error, 'error')

            }

        });
        req.done(function (data) {
        });

        $('#live-update').css('display', 'block');
        $('#course-update').css('display', 'block');

        
        
        $('#create-live').css('display', 'none');
        $('.schedule').css('display', 'none');
        $('#course-upload').css('display', 'none');
        $('#create-series').css('display', 'none');
        
        $('#create-course').css('display', 'block');
        
        
        $('#user-profile').css('display', 'none');
        $('.schedule-container').css('display', 'none');


    });
    $('.yes-live-btn').on("click", function (e) {
        e.preventDefault();
        closeNav()
        liveUrl = '/editLive?live_id='
        req = $.ajax({
            url: $('.delete-live').attr('data-href'),
            type: 'DELETE',
            data: {},
            beforeSend: function(){
                popover('Deleting...','success')
            },
            success: function (data) {
                popover(data, 'success')
            }, error: function (error) {
                console.log(error)
                popover(error, 'error')

            }

        });
        req.done(function (data) {
        });

        $('#live-update').css('display', 'block');
        $('#course-update').css('display', 'block');



        $('#create-live').css('display', 'none');
        $('.schedule').css('display', 'none');
        $('#course-upload').css('display', 'none');
        $('#create-series').css('display', 'none');

        $('#create-course').css('display', 'block');


        $('#user-profile').css('display', 'none');
        $('.schedule-container').css('display', 'none');


    });
    $('.yes-schedule-btn').on("click", function (e) {
        e.preventDefault();
        closeNav()
        liveUrl = '/editSchedule?schedule_id='
        req = $.ajax({
            url: $('.delete-schedule').attr('data-href'),
            type: 'DELETE',
            data: {},
            beforeSend: function(){
                popover('Deleting...','success')
            },
            success: function (data) {
                popover(data, 'success')
            }, error: function (error) {
                console.log(error)
                popover(error, 'error')

            }

        });
        req.done(function (data) {
        });

        $('#live-update').css('display', 'block');
        $('#course-update').css('display', 'block');



        $('#create-live').css('display', 'none');
        $('.schedule').css('display', 'none');
        $('#course-upload').css('display', 'none');
        $('#create-series').css('display', 'none');

        $('#create-course').css('display', 'block');


        $('#user-profile').css('display', 'none');
        $('.schedule-container').css('display', 'none');


    });
    $('.comment').on("click", function (e) {
        e.preventDefault();


        $('#comment-nav').css('display', 'flex');
        $('#video-bot-nav').toggle();


    });

    $('.click-search').on("click", function (e) {
        e.preventDefault();



        $('.logo').toggle();
        $('#search-form').toggle();



    });


function pageRedirect(url) {
    window.location.href = url;
}

$(document).ready(function () {
    $('.addCart').on("click", function (e) {
        e.preventDefault();
        var url = $(this).attr("data-href");
        var videoSrc = "../static/videos/";
        var userImgSrc = "../static/profile_pics/";
        var currency = "￥"

        req = $.ajax({
            url: url,
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")
                popover('Log in to add to cart', 'error')

            }

        });
        req.done(function (data) {
            popover('Added to cart', 'green')
            $('.removeCart').css('display','flex')
            $('.addCart').css('display','none')

        });
    });
    $('.removeCart').on("click", function (e) {
        e.preventDefault();
        var url = $(this).attr("data-href");
        var videoSrc = "../static/videos/";
        var userImgSrc = "../static/profile_pics/";
        var currency = "￥"

        req = $.ajax({
            url: url,
            type: 'DELETE',
            data: {},

            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")
                popover('Log in to add to cart', 'error')

            }

        });
        req.done(function (data) {
            popover(data, 'green')
            $('.removeCart').css('display','none')
            $('.addCart').css('display','flex')

        });
    });

});
$(document).ready(function () {
    $('.cart').on("click", function (e) {
        e.preventDefault();
        var url = $(this).attr("data-href");
        var videoSrc = "../static/videos/";
        var userImgSrc = "../static/profile_pics/";
        var currency = "￥"

        req = $.ajax({
            url: url,
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")


            }

        });
        req.done(function (data) {
            $('.cart-list').empty();
            $.each(data.result, function (key, value) {


                $('.cart-list').append('<div class="row"><div class="col-3 buy no-gutters cover-wrapper" ><img class="" id="cart-coverImg" src="' + coverImgSrc + value.coverImage + '" alt="" ></div><div class="col-8"><p id="cart-title">' + value.title + '</p><span id="cart-price">￥' + value.price + '</span></div></div>');

            });

        });
    });
    $('.buy').on("click", function (e) {
        e.preventDefault();
        closeLeftNav()
        closeNav()
        var url = $(this).attr("data-href");
        var userId = $(this).attr("user-id");

        var videoSrc = "../static/videos/";
        var userImgSrc = "../static/profile_pics/";
        var currency = "￥"

        req = $.ajax({
            url: url,
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        req.done(function (data) {
            var checkoutUrl = "/checkout?price=" + data.price + "&subject=" + data.title + "&course_id=" + data.id + "&user=" + userId;
            $('.checkout').css('display', 'block')
            $('.course-details').css('display', 'none')

            $('.navLink.total-price').css('font-size', '1.5rem')
//            $('.click-pay').attr('data-href', checkoutUrl)
            $('.live-img').attr('src', coverImgSrc + data.coverImg)
//            $('#checkout-title').text(data.title)
            $('#live-update').css('display', 'none');
            $('#course-update').css('display', 'none');

            $('#live').css('display', 'none');

            $('#create-live').css('display', 'none');
            $('.schedule').css('display', 'none');
            $('#course-upload').css('display', 'none');
            $('#create-series').css('display', 'none');
            
            $('#create-course').css('display', 'none');
            $('.my-profile').css('display', 'none');
            $('.live-list').css('display', 'none');
            $('.live-details').css('display', 'none');
            $('.video-list').css('display', 'none');
            $('.video-details').css('display', 'none');


            $('#user-profile').css('display', 'none');
            $('.schedule-container').css('display', 'none');


        });
    });

    $('.click-pay-login').on("click", function (e) {
        e.preventDefault();
        popover('Login to complete Payment', 'error')
    });
    $('.click-pay').on("click", function (e) {
        e.preventDefault();
        var url = $(this).attr("data-href");
        var videoSrc = "../static/videos/";
        var userImgSrc = "../static/profile_pics/";
        var currency = "￥"

        req = $.ajax({
            url: url,
            type: 'GET',
            data: {},
            success: function (data) {
                console.log(data)
            }, error: function (error) {
                console.log(error)
                console.log("error")

            }

        });
        req.done(function (data) {


            pageRedirect(data)


        });
    });

});


$('.upload-list').ready(function () {
    var arg = 'videoId=';
    var videoUrl = '/videoInfo?' + arg;
    var userUrl = '/userDetails?user_id='
    var currency = "￥"
    req = $.ajax({
        url: '/videos',
        type: 'GET',
        data: {},
        success: function (data) {
            console.log(data)
        }, error: function (error) {
            console.log(error)
            console.log("error")

        }

    });
    req.done(function (data) {
        var obj = data.result;

            $.each(obj, function (key, value) {

                if (value.approved === true)
                    $('.upload-list').append('<div class="video-container"><div class="thumb-wrapper" data-href="' + videoUrl + value.id + '"><li><a class="video" video-id="' + value.id + '" href="' + videoUrl + value.id + '"><img class="video-feed" loading="lazy" src="../static/coverImages/' + value.coverImage + '"></a></li></div><div class="video-info">     <div class="row no-gutters">     <div class="col-2 col-sm-2 col-md-2 no-gutters">     <div class="profile-pic-wrapper click-pro-pic" data-href=" ' + userUrl + value.username + '">     <span><a class="user-profile-pic" user-id="" href="#"><img class="profilepic" src="' + value.userImg + '" alt=""></a></span></div> </div>     <div class="col no-gutters">     <div class="inner-info">     <div class="flex-fill flex-column"><span>' + value.title + '</span><h5 class="float-right mr-2 text-success">'+currency+ value.price + '</h5>     <div class="upload-username">' + value.username + '</div>     <div class="upload-username">' + value.category + '</div> <span><p class="likes-comments" class="text-justify text-left " data-likes=""><span>' + value.likes + '</span><img    class="ml-1 mr-1"     src="../static/heart.png" alt="" width="16"><span>' + value.comments + '</span>     <img         src="../static/comment.svg" alt="" width="16"> </p> </span></div> </div> </div> </div></div></div>');

            });



        $('#live').css('display', 'none');

        

        $('.upload-list').css('display', 'flex');
        $('#user-profile').css('display', 'none');
        $('#course-upload').css('display', 'none');
        $('.checkout').css('display', 'none')

    });
});
    $('#verify-courses').on("click", function (e) {

        e.preventDefault();
        closeNav()

    var arg = 'videoId=';
    var videoUrl = '/videoInfo?' + arg;
    var userUrl = '/userDetails?user_id='
    var verifyUrl = '/verifyCourse?videoId='

    req = $.ajax({
        url: '/verifyCourseList',
        type: 'GET',
        data: {},
        success: function (data) {
            console.log(data)
        }, error: function (error) {
            console.log(error)
            console.log("error")

        }

    });
    req.done(function (data) {
        var obj = data.result;

        $('#verify-list').empty()


                   $.each(obj, function (key, value) {

                $('#verify-list').append('<card class="card shadow-lg live-card"  data-href="' + value.id + '" > <card ><a href="'  + value.id + '"> <div class="live-img-wrapper"><img class="live-img" src="../static/coverImages/' + value.coverImage + '" alt=""></div> <div class="live-profile-pic-wrapper click-pro-pic"  data-href="'  + value.username + '"><span><a  class="user-profile-pic border-light" href="#"><img class="profilepic"  src="' + value.userImg + '" alt=""></a></span> </div><div class="p-2 row no-gutters"><span class="live-info col-8 flex-content flex-column no-gutters"><span class="live-title">' + value.title + '</span><span class="">Created by:' + value.username + ' </span><span class="">Type:' + value.status + ' </span><span class="">Category:' + value.category + '</span><span class=""> </span></span>  <span class="live-info col-4 flex-content flex-column no-gutters"></div> </a></card><img src="../static/arrowDown.svg" type="button" class=" d-block mx-auto  extra-info m-2"><div class="content"><div class="text-center"><button class="fixed-btn m-2 review-videos-btn" data-target="#review-video-modal" data-toggle="modal">Review Videos</button><button class="fixed-btn m-2 user-intro" data-target="#user-info-modal" data-toggle="modal">User Intro</button></div><div></div><h6>Description</h6><div>'+ value.description+'</div><button type="button" class=" d-block mx-auto fixed-btn extra-info approve-btn" data-href="'+verifyUrl + value.id +'" >Approve</button></div> </card>');

                $('.user-intro').attr('data-href','/userDetails?user_id='+value.username)
                $('.review-videos-btn').attr('data-href','/videoDetails?videoId='+value.id)
        });




                $('.approve-card').css('display','none')






    });
    });
    $('#verify-list').on("click",'.approve-btn', function (e) {

        e.preventDefault();
        closeNav()

    var arg = 'videoId=';
    var videoUrl = '/videoInfo?' + arg;
    var userUrl = '/userDetails?user_id='
    var verifyUrl = '/verifyCourse?videoId='

    req = $.ajax({
        url: $(this).attr('data-href'),
        type: 'GET',
        data: {},
        success: function (data) {
            console.log(data)
        }, error: function (error) {
            console.log(error)
            console.log("error")

        }

    });
    req.done(function (data) {

        popover(data,'success')



    });
    });
    $('#verify-list').on("click",'.review-videos-btn', function (e) {

        e.preventDefault();


    req = $.ajax({
        url: $(this).attr('data-href'),
        type: 'GET',
        data: {},
        success: function (data) {
            console.log(data)
        }, error: function (error) {
            console.log(error)
            console.log("error")

        }

    });
    req.done(function (data) {
        var obj = data.result;

            if (obj.type === 'video') {
                $('video').attr("src", videoSrc + obj.videoRef);
                $('video').css('display', 'block');
                $('#episode-subtitle').text(obj.episode.subtitle);

                $('.video-js').attr("src", videoSrc + obj.videoRef);
                $('#controls').css('display', 'none');
                $('video').css('display', 'block');
                $('.course-img').css('display', 'none');
            } else if (obj.type === 'audio') {

                $('#audio-file').attr("audioFile", obj.videoRef);
                $('.course-img').css('display', 'block');
                $('.course-img').attr("src", coverImgUrl + obj.coverImg);
                var audioSrc = '/static/videos/' + $('#audio-file').attr('audioFile')
                $('#controls').css('display', 'flex');
                popover('Loading Audio..Please wait','success')
                wavesurfer.load(audioSrc);
                wavesurfer.on('ready', function () {
                    popover('Audio ready to play','success')
                            $('.loader').css('display', 'none')


        $('#pause-btn').on('click', function () {
            wavesurfer.pause();
            $('#play-btn').css('display', 'flex')
            $('#pause-btn').css('display', 'none')
        });
           $('#play-btn').on('click', function () {
            wavesurfer.play();
            $('#play-btn').css('display', 'none')
            $('#pause-btn').css('display', 'flex')
        });});




                $('#episode-subtitle').text(obj.episode.subtitle);






                $('video').css('display', 'none');



            } else if (obj.videoRef == null) {
                var ep = obj.episode[0];


                $('video').attr("src", videoSrc + obj.episode[0].videoRef);

                $('#video-likes').text(ep.likes);
                $('video').css('display', 'block');
                $('#episode-subtitle').text(ep.subtitle);
                $('.video-js').attr("src", videoSrc +obj.episode[0].videoRef);

                $('video').css('display', 'block');
                $('.course-img').css('display', 'none');
                $('.like-btn').attr('data-href', '/like/episode' + obj.episode[0].episodeId);
                $('#unlike-btn').attr('data-href', '/unlike/episode' + obj.episode[0].episodeId);
            }



    });
    });
    $('#verify-list').on("click",'.user-intro', function (e) {

        e.preventDefault();

    req = $.ajax({
        url: $(this).attr('data-href'),
        type: 'GET',
        data: {},
        success: function (data) {
            console.log(data)
        }, error: function (error) {
            console.log(error)
            console.log("error")

        }

    });
    req.done(function (data) {

        $('.user-introduction').text(data.introduction)



    });
    });


$("form#series-course").on('click', '.subtitle', function () {

    $header = $(this);
    //getting the next element
    $content = $header.next();
    //open up the content needed - toggle the slide- if visible, slide up, if not slidedown.
    $content.slideToggle(500, function () {
        //execute this after slideToggle is done
    });

});
$("#verify-list").on('click', '.extra-info', function () {

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
    dropdown[i].addEventListener("click", function () {
        this.classList.toggle("active");
        var dropdownContent = this.nextElementSibling;
        if (dropdownContent.style.display === "block") {
            dropdownContent.style.display = "none";
        } else {
            dropdownContent.style.display = "block";
        }
    });
}


$(document).ready(function () {




    $('form#schedule-form').on('submit', function (event) {
        var csrf_token = $('#csrf-token').attr('value');
        $.ajax({
            beforeSend: function (xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrf_token);
                }
                $('.loader').css('display', 'block')
               $('.border-btn').css('display','block')
                 popover('Creating schedule','success')
              $('.schedule-btn').css('display','none')

            },

            data: new FormData(this),
            type: 'POST',
            url: $('#schedule-form').attr('data-href'),
            processData: false,
            contentType: false,
            complete: function () {
                $('.loader').css('display', 'none')

            }

        })
            .done(function (data) {

                popover(data, 'success')
                $('.border-btn').css('display','none')
              $('.schedule-btn').css('display','block')

            });

        event.preventDefault();

    });
    $('form#update-session-form').on('submit', function (event) {
        var csrf_token = $('#csrf-token').attr('value');
        $.ajax({
            beforeSend: function (xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrf_token);
                }
                $('.loader').css('display', 'block')
            },
            data: new FormData(this),
            type: 'PUT',
            url: $(this).attr('data-href'),
            processData: false,
            contentType: false,
            complete: function () {
                $('.loader').css('display', 'none')

            }

        })
            .done(function (data) {

                popover(data, 'success')

            });

        event.preventDefault();

    });
    $('form#update-schedule-form').on('submit', function (event) {
        var csrf_token = $('#csrf-token').attr('value');
        $.ajax({
            beforeSend: function (xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrf_token);
                }
                $('.loader').css('display', 'block')
            },
            data: new FormData(this),
            type: 'PUT',
            url: $('.edit-schedule').attr('data-href'),
            processData: false,
            contentType: false,
            complete: function () {
                $('.loader').css('display', 'none')

            }

        })
            .done(function (data) {

                popover(data, 'success')

            });

        event.preventDefault();

    });
    $('form#create-role').on('submit', function (event) {
        var csrf_token = $('#csrf-token').attr('value');
        $.ajax({
            beforeSend: function (xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrf_token);
                }
                $('.loader').css('display', 'block')
            },
            data: new FormData(this),
            type: 'POST',
            url:'/createrole',
            processData: false,
            contentType: false,
            complete: function () {
                $('.loader').css('display', 'none')

            }

        })
            .done(function (data) {

                popover(data, 'success')

            });

        event.preventDefault();

    });
    $('form.session-form').on('submit', function (event) {
        var csrf_token = $('#csrf_token').attr('value');
        $.ajax({
            beforeSend: function (xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrf_token);
                }
                $('.loader').css('display', 'block')

                popover('Creating live session','success')

            },
            data: new FormData(this),
            type: 'POST',
            url: $('.session-form').attr('data-href'),
            processData: false,
            contentType: false,

        })
            .done(function (data) {
                $('.loader').css('display', 'none')
                popover(data, 'success')


            });

        event.preventDefault();

    });
    $('form.user-form').on('submit', function (event) {
        var csrf_token = $('#csrf_token').attr('value');
        $.ajax({
            beforeSend: function (xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrf_token);

                }
                $('.loader').css('display', 'block')
                popover('Updating Info','success')

            },
            error: function (error) {

                popover(error, 'error')
                $('.loader').css('display', 'none')

            },
            enctype: 'multipart/form-data',
            data: new FormData(this),
            type: 'POST',
            url: $(this).attr('data-href'),
            processData: false,
            contentType: false,

        })
            .done(function (data) {
                $('.loader').css('display', 'none')

                var intro = $('#introduction').val()

                $('#my-introduction').html(intro)
                $('.user-form').css('display', 'none')
                $('#my-introduction').css('display', 'block')
                $('#my-proPic').attr('src',$('#pic').value.split('\\')[2])

                popover(data, 'success')

            });

        event.preventDefault();

    });
    $('form#comment-form').on('submit', function (event) {
        var csrf_token = $('#csrf_token').attr('value');
        $.ajax({
            beforeSend: function (xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrf_token);

                }
            },
            error: function (error) {

                popover('Login to post a comment', 'error')


            },
            data: new FormData(this),
            type: 'POST',
            url: $(this).attr('data-href'),
            processData: false,
            contentType: false,

        })
            .done(function (data) {


                var comment = $('#content').val()
                $('#video-comments').text(data.totalComments)
                $('#user-reviews').append('<div><div data-href="" class="profile-pic-wrapper d-inline-flex mr-2 click-pro-pic"><span><img class="profilepic" src="'  + currentUserProPic + '" alt=""></span></div><small ><strong>' + currentUserUsername + '</strong></small><div><small id="user-review">' + comment + '</small></div></div></div></div>');


                popover(data.msg, 'success')

            });

        event.preventDefault();

    });

});

$.urlParam = function(name){
    var results = new RegExp('[\?&]' + name + '=([^&#]*)').exec(window.location.href);
    if (results==null) {
       return null;
    }
    return decodeURI(results[1]) || 0;
}