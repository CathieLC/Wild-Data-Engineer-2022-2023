console.log("Hello, World");
console.log("Hi, world!");

// loge is not a function (voir dans la console)
//console.loge("test")

// Sensible à la casse
console.log('test') 
// et 
console.Log 
// n'est pas la même chose !

/*Commentaire multiple lignes:
deuxième ligne */

console.log(1 + 1)


let userAge = 30;
let fruits = ['apple', 'banana', 'kiwi'];
let userCar = {
  model: "BMW", 
  year: "2000"
};
let sayMyName = function() {
  console.log("My name is Bob!")
};


let myName = "Cathie";
console.log(myName);
// Will print "Bob"
myName = "Caroline";
console.log(myName);
// Will print "Paul"



let myBudget = 0;
myBudget++;
console.log(myBudget); // affiche 1
myBudget += 2; 
console.log(myBudget); // affiche 3
myBudget = myBudget + 1;
console.log(myBudget); // affiche 4
myBudget--;
console.log(myBudget); // affiche 3
myBudget -= 2; 
console.log(myBudget); // affiche 1
myBudget = myBudget - 1;
console.log(myBudget); // affiche 0


let hello = "Hello";
hello += ", World!";
console.log(hello);
//  "Hello, World!"

// let quand la valeur peut changer et const pour les valeurs qui ne changent pas.

const person = {
  name: "Bob", 
  age: 25, 
  sayHello: function(){
    console.log("Hello");
  }
}

person.sayHello();
// "Hello"

typeof person;