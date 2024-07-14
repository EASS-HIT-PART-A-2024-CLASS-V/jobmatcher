import { NavLink, useLoaderData } from "react-router-dom";
import { useState } from "react";
import styles from '../styles/CompanyProfile.module.css';

export default function CompanyProfile() {
    const { company, jobs } = useLoaderData();
    const [isOpen, setIsOpen] = useState(false);

    const toggleDropdown = () => {
        setIsOpen(!isOpen);
    };

    return (
        <div className={styles.companyProfile}>
            <h1>Company Profile</h1>
            <h2>{company.name}</h2>
            <p>{company.description}</p>
            <h3 onClick={toggleDropdown} className={styles.dropdownHeader}>
                Open Positions {isOpen ? '▲' : '▼'}
            </h3>
            <div className={`${styles.jobListWrapper} ${isOpen ? styles.open : ''}`}>
                <ul className={styles.jobList}>
                    {jobs.map((j) => (
                        <li key={j.id} className={styles.jobItem}>
                            <NavLink to={`/swipe/${j.id}?isCandidate=false`} className={styles.jobLink}>
                                {j.title}
                            </NavLink>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}