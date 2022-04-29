import {Link} from 'react-router-dom';

//버튼 컨포넌트

function MainButton(){
    return (
    <header>

        <div>
            
                <button className = 'button'> 
                    <Link to='/map' style ={{ textDecoration: 'inherit'}}>
                        <button>위치선택</button>
                    </Link>
                    
                    <Link to='/userinfo' style ={{ textDecoration: 'inherit'}}>
                        <button>내 정보</button>
                    
                    </Link>

                    <Link to='/joblist' style ={{ textDecoration: 'inherit'}}>
                        <button>진행중인 알바</button>
                    </Link>
 
        
                </button>
        </div>  
    </header>
    );
}
export default MainButton;
    