document.addEventListener('DOMContentLoaded', () => {
     new TypeIt(".animated", {
          speed: 200,
          loop: true,
     })
     .type("interativa!", {delay: 400})
     .delete("interativa!".length)
     .type("eficiente!", {delay: 400})
     .delete("eficiente!".length)
     .type("inovadora!", {delay: 400})
     .delete("inovadora!".length)
     .type("acessível!", {delay: 400})
     .delete("acessível!".length)
     .type("moderna!", {delay: 400})
     
     .go();
});