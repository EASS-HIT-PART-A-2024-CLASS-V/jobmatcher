import { NavLink } from "react-router-dom";
import "../index.css"

export default function Navbar() {
    return (
        <nav className={"navbar"}>
            <NavLink to="/" exact className={"navbar-link"}>Home</NavLink>
            <NavLink to="/login" className={"navbar-link"}>Login</NavLink>
            <NavLink to="/contact" className={"navbar-link"}>Contact</NavLink>
        </nav>
    );
}
