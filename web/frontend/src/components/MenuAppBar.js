import React from 'react';
import { Navbar, Container, Nav, NavDropdown } from 'react-bootstrap';
import { Link } from "react-router-dom";

const MenuAppBar = () => {
  return (
    <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand href="#home">
          <Link to="/" style={{color: "white", textDecoration: "none"}}>
            Sun Moon Mini Alba
          </Link>
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link>
              <Link to="/" style={{textDecoration: 'none', color: 'gray'}}>Home</Link>
            </Nav.Link>
            <Nav.Link>
              <Link to="/mypage" style={{textDecoration: 'none', color: 'gray'}}>MyPage</Link>
            </Nav.Link>
         </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
 )
}

export default MenuAppBar;
