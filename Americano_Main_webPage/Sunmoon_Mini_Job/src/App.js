import {Routes, Route} from 'react-router-dom';

import Map from './pages/Map';
import JobList from './pages/JobList';
import MyPage from './pages/MyPage';
import Main from './pages/Main';
// 지도 각각 게시판들
import Bongwan from './pages/Bongwan';
import Wonhwagwan from './pages/Wonhwagwan';
import Notice_page from './pages/Notice_page';



function App() {
  return (
    <div>
         
        <Routes> 

          <Route path='/' element={<Main />}/>  
          <Route path='/map' element={<Map />}/>
          <Route path='/joblist' element={<JobList />}/>
          <Route path='/userinfo' element={<MyPage />}/>
          {/*
            지도 이미지 각각의 페이지 링크
          */}
          <Route path ='/map/Bongwan' element={<Bongwan/>}/>
          <Route path ='/map/Wonhwagwan' element={<Wonhwagwan/>}/>
          
          {/*
            본관 페이지에서 게시글 작성
          */}
          <Route path ='/map/Bongwan/notice' element={<Notice_page/>}/>
      </Routes> 
      
    </div> 
  );
}
export default App;
