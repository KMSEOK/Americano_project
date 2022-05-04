// 게시판 만들기
import {Link} from 'react-router-dom';
function Bongwan(){
    return(
        <div>
            <p>본관 게시판 페이지</p>
            <Link to = '/'>
                <button>
                    메인
                </button>
            </Link>
             
        </div>
    );
}

export default Bongwan;