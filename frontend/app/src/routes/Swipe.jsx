import React, { useEffect, useState } from 'react';
import JobCard from '../components/JobCard';
import Button from '../components/Button';
import { useLoaderData } from 'react-router-dom';
import CandidateCard from '../components/CandidateCard';
import { swipe } from '../apiCalles';
import Matched from '../components/Matched';

export default function Swipe () {
    const {matchEntities, isCandidate, user_id} = useLoaderData()
    const [isMatch, setIsMatch] = useState(false)
    
    const [currentIndex, setCurrentIndex] = useState(0);
    const nextEntity = () => {
        setCurrentIndex((prevIndex) => ((prevIndex < matchEntities.length) ? prevIndex + 1 : prevIndex));
    };
    const handleLike = async () => {
        console.log('Liked:', matchEntities[currentIndex].id);
        setIsMatch(await swipe(user_id, matchEntities[currentIndex].id, isCandidate, true))
        //swipe(user_id, matchEntities[currentIndex].id, isCandidate, true)
        nextEntity();
    }
    const handleDislike = async () => {
        console.log('Disliked:', matchEntities[currentIndex].id);
        setIsMatch(await swipe(user_id, matchEntities[currentIndex].id, isCandidate, false))
        //swipe(user_id, matchEntities[currentIndex].id, isCandidate, false)
        nextEntity();
    };
    
    return(
        <div className={"swipe-container"}> 
            {isMatch ? <Matched userId={user_id} setIsMatch={setIsMatch}/> : ( 
            <> 
                {matchEntities.length > currentIndex ? (
                <>
                    <Button caption={"like"} onClick={handleLike} className={"swipe-button like-button stick-right"}></Button>
                    {isCandidate ? <JobCard matchEntity={matchEntities[currentIndex]}/> : <CandidateCard matchEntity={matchEntities[currentIndex]}/>}
                    <Button caption={"dislike"} onClick={handleDislike} className={"swipe-button dislike-button"}></Button>
                </>
                ) : (
                    <h1>No more matches</h1>
                )}
            </>
        ) }
        </div>
    ) 
};

