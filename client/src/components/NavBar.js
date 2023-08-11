import React from "react";
import { NavLink } from "react-router-dom";

const linkStyles = {
  display: "inline-block",
  width: "300px",
  padding: "12px",
  margin: "0 18px 6px",
  background: "black",
  textDecoration: "none",
  color: "orange",
};

function NavBar() {
  return (
    <>
      <NavLink
        className="nav-buttons"
        to="/"
        exact
        style={linkStyles}
      >
        Home
      </NavLink>
      <NavLink
        className="nav-buttons"
        to="/about"
        exact
        style={linkStyles}
      >
        About
      </NavLink>
      <NavLink
        className="nav-buttons"
        to="/restaurants"
        exact
        style={linkStyles}
      >
        Restaurants
      </NavLink>

      <NavLink
        to="/reviews"
        className="nav-buttons"
        exact
        style={linkStyles}
      >
        Reviews
      </NavLink>
    </>
  );
}

export default NavBar;
