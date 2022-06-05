import React, { useState, useEffect } from 'react';
import MenuAppBar from './components/MenuAppBar'
import Home from './components/Home'
import Jobs from './components/Jobs'
import MyPage from './components/MyPage'
import Signup from './components/Signup'
import Login from './components/Login'
import { ContextProvider } from './components/Context'

import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  // const [ jobs, setJobs ] = useState([]);
  // const [ loading, setLoading ] = useState(false);
  // const fetchJobs = async () => {
  //   const res = await fetch("http://localhost:8080/api/v1/jobs");
  //   const tmp = await res.json();
  //   console.log(tmp);
  //   setJobs(tmp);
  // }
  
  // useEffect(() => {
  //   setLoading(true);
  //   fetchJobs();
  //   setLoading(false);
  // }, [])
  

  return (
    <ContextProvider>
      <BrowserRouter>
        <MenuAppBar/>
        <Routes>
          <Route path="/" element={ <Home />} />
          <Route path="/jobs/:place" element={ < Jobs />}  />
          <Route path="/mypage" element={ <MyPage /> } />
          <Route path="/login" element={ <Login /> } />
          <Route path="/signup" element={ <Signup /> }/>
        </Routes>
      </BrowserRouter>  
    </ContextProvider>
  )
}
export default App;
