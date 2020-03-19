/*function hello(){
  console.log("Hello World!");
}  

function add(a,b){
  console.log(a+b);
}
function presentation(age, nom, genre){
  if(genre == "H"){
    genre = "un homme"
  }
  if(genre == "F"){
    genre = "une femme"
  }
  console.log("Bonjour, je suis " + genre + ", je m’appelle " + nom + " et j’ai " + age + " ans.");
}*/

function romain (chiffre){
  let result = ""

  do {
    if(chiffre >= 1000){
      chiffre = chiffre-1000;
      result += "M";
    }
    else if(chiffre >= 500){
      chiffre -= 500;
      result += "D";
    }
    else if(chiffre >= 100){
      chiffre -= 100;
      result += "C";
    }
    else if(chiffre >= 50){
      chiffre -= 50;
      result += "L";
    }
    else if(chiffre >= 10){
      chiffre -= 10;
      result += "X";
    }
    else if(chiffre >= 5){
      chiffre -= 5;
      result += "V";
    }
    else {
      chiffre -= 1;
      result += "I";
    }
  }
  while (chiffre > 0);
  console.log(result)
}

