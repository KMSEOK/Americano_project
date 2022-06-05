import React from "react";

import { Form, Button, Row, Col } from "react-bootstrap";
import { Link } from "react-router-dom";

const Signup = () => {
  return (
    <Row style={{ marginTop: "50px" }}>
      <Col style={{ maxWidth: "500px", margin: "0 auto" }}>
        <Form>
          <Form.Group className="mb-3">
            <Form.Control type="text" placeholder="Enter name" />
          </Form.Group>

          <Form.Group className="mb-3" controlId="formBasicPassword">
            <Form.Control type="password" placeholder="Password" />
          </Form.Group>
          <p>
            <Link to="/login">or login.</Link>
          </p>
          <Button variant="primary" type="submit">
            Signup
          </Button>
        </Form>
      </Col>
    </Row>
  );
};

export default Signup;
