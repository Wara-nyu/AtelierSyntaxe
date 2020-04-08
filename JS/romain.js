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


/*
	chiffreRomain1 => 'I'
  si element  = I
  et que element + 1 = 'V' , 'X'
  */


/*Créer une fonction qui accepte en paramètre deux chaines de caractères représentant des nombres romains et qui renvoie en résultat une chaine de
caractères correspondant à la somme de ces deux nombres*/

/*
	i = 1
	ii = 2
	iii = 3
	iv = 4
	v = 5
	vi = 6
  vii = 7
  viii = 8
  ix = 9
  x = 10

  CDXCIX = 499
*/

function sommeChiffreR(chiffreRomain1,chiffreRomain2){

  chiffreRomain
	var NombreR = [[0, null],[900, "CM"],[1000, "M"], [400, "CD"], [500, "D"], [90, "XC"], [100, "C"], [40, "XL"], [50, "L"], [9, "IX"], [10, "X"], [4, "IV"], [1,"I"]];

	chiffreRomain1.
	console.log(chiffreRomain1 + chiffreRomain2);
  console.log("je suis dans la fonction")
}

console.log("je suis en dehors de la fonction")
 sommeChiffreR("V","III")
