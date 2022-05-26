import React from 'react'
import { useParams } from 'react-router-dom';
import Job from './Job';

const Jobs = (props) => {
  
  const params = useParams()
  const jobs = props.jobs.filter(job => job.place === params.place); 
  console.log(jobs);

  return (
    <div>
      { jobs.length === 0 ? (
        <div>no results.</div>
        ) : (
          <div>
            { 
              jobs.map(job => (
                <Job job={job}/>
              ))
            }
          </div> 
        )
      }
    </div>
  )
}

export default Jobs;

