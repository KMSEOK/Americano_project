import React, { useState, useEffect } from 'react';
import MenuAppBar from './components/MenuAppBar'
import Home from './components/Home'
import Jobs from './components/Jobs'
import MyPage from './components/MyPage'

import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  const [ jobs, setJobs ] = useState([]);
  const [ loading, setLoading ] = useState(false);

  const fetchJobs = async () => {
    const res = await fetch("http://localhost:8080/api/v1/jobs");
    const tmp = await res.json();
    console.log(tmp);
    setJobs(tmp);
  }
  
  useEffect(() => {
    setLoading(true);
    fetchJobs();
    setLoading(false);
  }, [])
  

  return (
    <BrowserRouter>
      <MenuAppBar/>
      <Routes>
        <Route path="/" element={ <Home />} />
        <Route path="/jobs/:place" element={ < Jobs jobs={jobs}/> } />
        <Route path="/mypage" element={ <MyPage /> } />
      </Routes>
    </BrowserRouter>  
  )
}
export default App;
