// 나의 정보 페이지
import { Link } from "react-router-dom";
import mypage from './MyPage.module.css';

function MyPage(){
    return(
        <div className = {mypage.div}>
            <Link to='/map/Bongwan'>
                <img className = {mypage.image} src="/img/userIcon.png"/>      
            </Link>
            
        </div>
    );
}

export default MyPage;