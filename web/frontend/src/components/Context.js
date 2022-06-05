import React, { useState, createContext, useEffect } from 'react';

export const Context = createContext();

export const ContextProvider = (props) => {
    const [jobs, setJobs] = useState([]);
    const [ currentUser, setCurrentUser ] = useState(null);
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
        <Context.Provider job_data={{jobs, setJobs, currentUser, setCurrentUser, loading, setLoading}}>
            {props.children}
        </Context.Provider>
    )
}

