$(document).ready(function() {
    $('.text').textillate({
        loop: true,
        sync: true,
        in:{
            effect: 'bounceIn',
        },
        out:{
            effect: 'bounceOut',
        },
    });

    // Siri configuration

    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
    });

    // Siri message animation

    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },

    });

    // mic button  click event

    $("#MicBtn").click(function(){
        eel.playassistantsound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands()()
    });

    // Keyboard shortcut

    function doc_keyup(e) {
        if (e.key === 'v' && e.metaKey) {
            eel.playassistantsound()
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands()()
        }
    }
    document.addEventListener('keyup', doc_keyup, false);


});