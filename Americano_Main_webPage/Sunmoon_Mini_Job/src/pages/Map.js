// 지도 페이지
import { Link } from "react-router-dom";
import map from './Map.module.css';

function Map(){
    return(
        <div>
            <Link to='/map/Bongwan'>
                <img class={map.image} src="/img/본관.png"/>      
            </Link>
            <Link to = '/map/Wonhwagwan'>

                <img class= {map.image} src="/img/원화관.png"/>
            </Link>
            <Link to = '/map/Recently'>
                <img class= {map.image} src="/img/star.png"/>
                <p>최근에 올라온 게시글</p>
            </Link>
             
        </div>
    );
}

export default Map;