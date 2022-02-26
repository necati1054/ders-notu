fetch("https://jsonplaceholder.typicode.com/users")
.then((response)=>response.json())
.then((json)=>json.forEach((item)=>console.log("name"+item.name)))
.catch((err)=>console.log(err));

fetch("https://jsonplaceholder.typicode.com/comments")
.then((Response) => Response.json())
.then((json) => json.forEach((ıtem) => console.log(ıtem.email)))