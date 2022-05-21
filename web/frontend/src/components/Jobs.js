import React from 'react'
import { useState, useEffect } from 'react';

const Jobs = () => {
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
    <div>
      { loading ? (
        <div>loading...</div>
        ) : (
          <div>
            { 
              jobs.map(job => (
                <div> { job.title } </div>
            ))
            }
          </div> 
        )
      }
    </div>
  )
}

export default Jobs;

