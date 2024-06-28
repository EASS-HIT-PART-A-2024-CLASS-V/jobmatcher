import React from 'react';
import Button from '../components/Button';
import { NavLink } from 'react-router-dom';
import "../index.css"

export default function Login() {
    //should create api call to candidates_match
    
    const cand_id = 1;
    const job_id = 2;
    return (
        <div className={"login-container"}>
            <h2>Who Are You?</h2>
            <NavLink to={`/swipe/${job_id}?isCandidate=false`} className={"navlink-button"}>
                Job
            </NavLink>
            <NavLink to={`/swipe/${cand_id}?isCandidate=true`} className={"navlink-button"}>
                Candidate
            </NavLink>
        </div>
    );
};

