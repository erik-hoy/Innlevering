# Dette er Readme for Assigment 2

Vi valgte å bruke en regresjons-algoritme for å finne et estimat på antall passasjerer på en gitt dag.
Metoden som ble brukt var lineær regresjon som fant linjen som passet best til datasettet. 
Resultatet var en linje som så tilnærmet rett ut men som hadde en liten helning: 
regObj.predict([[1]]) = array([5.50116485])
regObj.predict([[120]]) = array([5.48613281])
Av dette ser vi at det ikke er en gjennomsnittsverdi men at prediksjonenen varierer rundt 5.5 passasjerer. 
