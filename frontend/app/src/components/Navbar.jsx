import { NavLink } from "react-router-dom";
import styles from "../styles/Navbar.module.css"; // Import your module.css file
import logo from '../assets/jobs_logo.svg';


export default function Navbar() {
    return (
        <nav className={styles.navbar}>
            <NavLink to="/" className={styles.navbarLink}>Home</NavLink>
            <NavLink to="/login" className={styles.navbarLink}>Login</NavLink>
            <img src={logo} alt="Jobs Logo" className={styles.navbarLogo} />

        </nav>
    );
}

