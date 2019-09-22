var fs = require('fs');
var firebase = require('firebase');
var firebaseConfig = {
  apiKey: "AIzaSyBXlSm8iJa8b6cwqEs-yB0gg8ZktWiartg",
  authDomain: "navegacion-72ca7.firebaseapp.com",
  databaseURL: "https://navegacion-72ca7.firebaseio.com",
  projectId: "navegacion-72ca7",
  storageBucket: "",
  messagingSenderId: "818987144864",
  appId: "1:818987144864:web:b252daeea3f7fb32b81bc5"
};
firebase.initializeApp(firebaseConfig);
base = firebase.database();
var ref = base.ref('mineriaOptimismo');
ref.once('value', (data)=> {
  var encuesta = data.val();
  keys = Object.keys(encuesta);
  keys.map((a)=>
    {
      var enc = encuesta[a];
      // var texto = "Feliz: " + enc.feliz.replace('\n',' ') + " Triste: " + enc.triste.replace('\n',' ') + " Preocupado: " + enc.preocupado.replace('\n',' ');
      // if(enc.pes == true)
      // {
      //   texto+=" soy pesimista";
      // }
      // else {
      //   texto+=" soy optimista";
      // }
      var texto = JSON.stringify(enc);
      texto.replace(/(?:\r\n|\r|\n)/g, ' ');
      texto = texto.split("\n").join("");

      fs.unlink('public/python/txts/' + a + '.txt', function (err) {
        //if (err) throw err;
        console.log('File deleted!');
      });
      fs.appendFile('public/python/txts/' + a + '.txt', texto, function (err) {
        if (err) throw err;
        console.log('Saved!');
      });
    }
  );
  setTimeout(()=>
  {
    process.exit(57);
  },1000);
},
  (err)=> {
    console.log(err);
    console.log("error")
  });
