const express = require('express')
const dotenv = require('dotenv')
var cors = require('cors')
app = express()
const port = 4500;
app.use(cors())

app.get('/fetch',(req,res) =>{
    // var resp ;
    let header = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiVXNlcm5hbWUiOiJ2cnMiLCJleHBpcmVzIjoiMTAvMTcvMjQgMDk6NDM6MjcifQ.iF7jLdXhfpDP4ALmB-C1Y9875klWCdvSwHBW6GNYaPQ",
        "Content-Type": "application/json"
    };
    console.log('hello');
    let url = "http://127.0.0.1:8000/Task/get/{id}?request_id=3f8c5da5-338f-4f52-bb50-1fe285806f38";
    fetch(url,{method:'GET',headers: header})
    .then(response=>response.json())
    .then(data => res.json(data))
    .catch(error => console.log(error));
    // console.log(resp);
    // res.send(String(resp));
})

app.listen(port, () =>{
    console.log('Server is running')
})