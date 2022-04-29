//메인 
import { useState } from "react";
import MainButton from "../components/MainButton";


function Main(){
    return(
        <div>
            <h1 className="h1"><a href='http://localhost:3000/'><img class="image" src="/img/sunmoonImge.png"/></a></h1>
            <h2 className = 'h2'>선문 미니알바</h2>
            <nav className="navbar"></nav>

            <MainButton/>
            <nav className="navbar"></nav>
        </div>
    );
}

export default Main;