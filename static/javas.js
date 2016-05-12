$("html").keydown(function(e) {
    e.preventDefault();
    switch (e.keyCode) {
        case 37:
            $.get('/left');
            console.info("Pressed left?");
            break
        case 39:
			$.get("/right");
            console.info("Pressed right");
            break;
        case 38:
            $.get("/go");
            break;
         case 40:
            $.get("/back");
        default:
        		$("#msg").html("Pressed unknown button");
            console.info("User pressed uknown button with keycode:", e.keyCode);
    }
    return false;
});


window.networkUpdates = setInterval(function(){ 
    $.getJSON('/api/wireless', function(data) {
        $("#networks").empty();
        $.each(data, function(i, e) {
            console.info("appending:", e);
            $("#networks").append("<option>" + e.ssid + "</option>");
        });
        console.info(data);
        $("#ssid").text(ap.Ssid);
        $("#freq").text(ap.Frequency);
        $("#strength").text(ap.Strength);
    });
}, 1000); 


//clearInterval(window.networkUpdates);
