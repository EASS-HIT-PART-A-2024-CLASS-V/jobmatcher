import { NavLink } from "react-router-dom";
import styles from "../styles/Home.module.css"; // Import CSS module
import logo from '../assets/jobs_logo.svg';

export default function Home() {
    return (
        <div className={styles["home-container"]}>
            <img src={logo} alt="Jobs Logo" className={styles["home-image"]} />
            <h2 className={styles["home-heading"]}>
                Swipe right to your dream job with JobSwipe! Find remote, startup, or corporate careers effortlessly. Start swiping and land your perfect job today!
            </h2>
            <NavLink to={"login"} className={styles["home-button"]}>Let's go!</NavLink>
            <p className={styles["home-quote"]}>
                "Find out what you like doing best and get someone to pay you for doing it." - Katherine Whitehorn
            </p>
        </div>
    );
}
