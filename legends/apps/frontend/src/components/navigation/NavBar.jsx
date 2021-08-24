import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import {NavLink} from "react-router-dom";
import './NavBar.module.css'

const NavBar = () => {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <NavLink className="navbar-brand" to="/">Navbar</NavLink>
            <div className="collapse navbar-collapse" id="navbarNav">
                <ul className="navbar-nav">
                    <li className="nav-item active">
                        <NavLink className="nav-link" to="categories">Categories</NavLink>
                    </li>
                    <li className="nav-item">
                        <NavLink className="nav-link" to="users">Users</NavLink>
                    </li>
                </ul>
            </div>
        </nav>
    );
}

export default NavBar