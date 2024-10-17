import React, {useState, useEffect} from "react";
import './home.css'
async function Fetch(setData){
    try{
        const url = 'http://localhost:4500/fetch';
        const request = await fetch(url);
        const result = await request.json();
        console.log(result);
        setData(result);
        sessionStorage.setItem('game-info',JSON.stringify(result,null,2));
    }
    catch(err){
        console.log("Fetching error: ",err);
    }
}
function Home(){
   const [data,setData] = useState(null);
   useEffect(()=>{
    const data = sessionStorage.getItem('game-info');
    if (data){
        setData(JSON.parse(data));
    }
    else{
        Fetch(setData);
    }
   },[]);
   return(
    <div className="home-page">
        <div className="nav">

        </div>
        <hr></hr>
        <div className="home-options">
            <div className="custom">
                <form className="forms">
                    <label>Project Brief</label>
                    <input type='text-area' className="task"/>
                    <label>Prefered Programming Languages</label>
                    <input type='text' className="lang" />
                </form>
            </div>
            <div className="templates">

            </div>
        </div>
    </div>
   );
}
export default Home;
