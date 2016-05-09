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
