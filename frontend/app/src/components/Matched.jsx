
import React from 'react';
import { NavLink } from 'react-router-dom';
import Button from './Button';

export default function Matched({userId, setIsMatch}) {
    

    const handleSwipeClick = () => {
        setIsMatch(false)
    };

    return (
        <div>
            <h1>Matched</h1>
            <nav>
                <NavLink to="/chat">Open Chat</NavLink>
                <Button caption="Back to Swiping" onClick={handleSwipeClick} />
            </nav>
        </div>
    );
}

