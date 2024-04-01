// Assuming you have a JavaScript object
var myObj = { name: "John", age: 31, city: "New York" };

// Convert the object into a JSON string and store it
var myJSON = JSON.stringify(myObj);
localStorage.setItem("testJSON", myJSON);

// Retrieve the JSON string from local storage
var text = localStorage.getItem("testJSON");

// Convert the JSON string back into an object
var obj = JSON.parse(text);

console.log(obj); // { name: "John", age: 31, city: "New York" }
