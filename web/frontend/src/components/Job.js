import { Alert } from 'react-bootstrap'
import React from 'react'
import { Card } from 'react-bootstrap';


const Job = (props) => {
    
    return (
      <Card style={{ width: '18rem' }} bg="success">
        <Card.Body>
          <Card.Title>{props.job.title}</Card.Title>
          <Card.Subtitle className="mb-2 text-muted">{props.job.place}</Card.Subtitle>
          <Card.Text>
            user_id: {props.job.user_id} 
          </Card.Text>
          <Card.Text>
            {props.job.description}
          </Card.Text>
          <Card.Text>reward_money: {props.job.reawrd_money}</Card.Text>
          <Card.Text>reward_item: {props.job.reward_item}</Card.Text>
          <Card.Text>status: {props.job.status}</Card.Text>
          <Card.Text>time_required: {props.job.time_required}</Card.Text>
        </Card.Body>
      </Card>          
    )
}

export default Job;
