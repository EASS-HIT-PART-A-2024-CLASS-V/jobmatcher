import React from 'react';
import { NavLink } from 'react-router-dom';
import Button from './Button';
import styles from '../styles/Matched.module.css';

export default function Matched({ userId, setIsMatch }) {

    const handleSwipeClick = () => {
        setIsMatch(false)
    };

    return (
        <div className={styles.matchedContainer}>
            <h1 className={styles.matchedTitle}>Matched</h1>
            <nav className={styles.matchedNav}>
                <NavLink to="/chat" className={styles.navLink}>Open Chat</NavLink>
                <div className={styles.buttonContainer}>
                    <Button caption="Back to Swiping" onClick={handleSwipeClick} />
                </div>
            </nav>
        </div>
    );
}
