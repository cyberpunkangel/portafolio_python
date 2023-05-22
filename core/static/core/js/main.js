//Animacion de tecla
var app = document.getElementById('app');

var typewriter = new Typewriter(app, {
    loop: true,
    delay: 50
});

typewriter.typeString('La inteligencia artificial no es una amenaza para la humanidad, sino una oportunidad para mejorarla.')
    .pauseFor(1)
    .deleteAll()
    .start();

//modal
$("#exampleModal").on('hidden.bs.modal', function (e) {
    $("#exampleModal iframe").attr("src", $("#exampleModal iframe").attr("src"));
});