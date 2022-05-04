// 지도 페이지
import { Link } from "react-router-dom";

function Map(){
    return(
        <div>
            <Link to='/map/Bongwan'>
                <img class="image" src="/img/본관.png"/>      
            </Link>
            <Link to = '/map/Wonhwagwan'>

                <img class="image" src="/img/원화관.png"/>
            </Link>
             
        </div>
    );
}

export default Map;