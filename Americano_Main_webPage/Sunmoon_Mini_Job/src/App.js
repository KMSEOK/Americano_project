import {Routes, Route} from 'react-router-dom';
import Map from './pages/Map';
import JobList from './pages/JobList';
import MyPage from './pages/MyPage';
import Main from './pages/Main';



function App() {
  return (
    <div>
         
        <Routes> 

          <Route path='/' element={<Main />}/>  
          <Route path='/map' element={<Map />}/>
          <Route path='/joblist' element={<JobList />}/>
          <Route path='/userinfo' element={<MyPage />}/>
      </Routes> 
      
    </div> 
  );
}
export default App;
