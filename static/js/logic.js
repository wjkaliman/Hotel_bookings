
console.log("hey");

d3.json("http://localhost:5000/api/bookings")
    .then(function (data) {
        console.log(data);
    })
    .catch(function (error) {
        console.log(error);
    });