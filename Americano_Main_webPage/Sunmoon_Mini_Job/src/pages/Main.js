//메인 
import { useState } from "react";
import MainButton from "../components/MainButton";
import MainCss from './Main.module.css'

function Main(){
    return(
        <div>
            <h1 className= {MainCss.h1}><a href='http://localhost:3000/'>
                <img class={MainCss.image} src="/img/sunmoonImge.png"/></a>
            </h1>
            <h2 className = {MainCss.h2}>선문 미니알바</h2>
            <nav className={MainCss.navbar}></nav>
            
            <MainButton/>
            <nav className={MainCss.navbar}></nav>
        </div>
    );
}

export default Main;