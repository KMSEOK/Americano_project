import { Alert } from 'react-bootstrap'
import React, { Component } from 'react'

const Job = () => {
    
    return (
        <Alert>
          This is alert. 
          <Alert.Link href="#">an example link</Alert.Link>. Give it a click if you
          like.
        </Alert>
    )
}

export default Job;
