import React, { useState, useEffect} from "react";
import './home.css';
import GF from './static/GameForgelogo.png';
import List from "./req";
async function Fetch(setData) {
    try {
        const url = 'http://localhost:4500/fetch';
        const request = await fetch(url);
        const result = await request.json();
        console.log(result);
        setData(result);
        sessionStorage.setItem('game-info', JSON.stringify(result, null, 2));
    } catch (err) {
        console.log("Fetching error: ", err);
    }
}

function Home() {
    const [data, setData] = useState(null);
    useEffect(() => {
        const data = sessionStorage.getItem('game-info');
        if (data) {
            setData(JSON.parse(data));
        } else {
            Fetch(setData);
        }
    }, []);

    return (
        <div className="home-page">
            <div className="nav">
                <a href='/home'><button><img src={GF} className="logo" alt="GameForge logo" /></button></a>
                <div className="right-section">
                    <a href='#'><button className="db">Dashboard</button></a>
                    <a href="/"><button className="signout">Sign out</button></a>
                </div>
            </div>
            <List />
        </div>
    );
}

export default Home;
