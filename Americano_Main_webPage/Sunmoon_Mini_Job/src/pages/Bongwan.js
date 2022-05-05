// 게시판 만들기
import {Link} from 'react-router-dom';

function Bongwan(){
    return(
        <div>
            <p>본관 게시판 페이지</p>
            <nav>

                <Link to = '/map'>
                    <button className='bu'>
                        위치선택
                    </button>
                </Link>
                <Link to = '/userinfo'>
                    <button>
                        내 정보
                    </button>
                </Link>
                <Link to = '/joblist'>
                    <button>
                        진행중인 알바
                    </button>
                </Link>
                <Link to = '/map/Bongwan/notice'>
                    <button>
                        글작성
                    </button>
                </Link>
                
                


            </nav>

        </div>
    );
}

export default Bongwan;