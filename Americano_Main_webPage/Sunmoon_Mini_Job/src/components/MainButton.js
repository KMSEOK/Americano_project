import {Link} from 'react-router-dom';
import mainButton from './MainButton.module.css';

//버튼 컨포넌트

function MainButton(){
    return (
    <header>

        <div>
            
                <div className= {mainButton.mbutton}>
                    <Link to='/map' style ={{ textDecoration: 'inherit'}}>
                        <button className = {mainButton.button}>위치선택</button>
                    </Link>
                    
                    <Link to='/userinfo' style ={{ textDecoration: 'inherit'}}>
                        <button className = {mainButton.button}>  내 정보</button>
                    
                    </Link>

                    <Link to='/joblist' style ={{ textDecoration: 'inherit'}}>
                        <button className = {mainButton.button}>진행중인 알바</button>
                    </Link>
                </div>
            
        </div>  
    </header>
    );
}
export default MainButton;
    