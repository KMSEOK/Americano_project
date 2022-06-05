import React, {useContext} from 'react'
import { useParams } from 'react-router-dom';
import Job from './Job';
import { Context } from './Context'


const Jobs = () => {

  const {jobs, setJobs, currentUser, setCurrentUser, loading, setLoading} = useContext(Context)
  console.log(jobs)  
  const params = useParams()
  // const currentJobs = jobs.filter(job => job.place === params.place); 
  // console.log(jobs);

  return (
    <div>
      { jobs === 'undefined' ? (
        <div>no results.</div>
        ) : (
          <div>
            { 
              jobs.filter(job => job.place === params.place).map(job => (
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

