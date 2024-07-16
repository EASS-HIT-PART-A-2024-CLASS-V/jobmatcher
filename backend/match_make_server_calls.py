from fastapi import HTTPException
import httpx
import os
from schemas import Candidate, Job
from utils import *
from typing import List

base_url = os.getenv("URL_BASE", "http://localhost:8001")

def matching_jobs(candidate: Candidate) -> List[Job]:
    #importing list from DB
    jobs = find_jobs_list() #async

    #converting pydantic classes into dictionaries
    candidate_data = pydantic_to_dict(candidate)
    jobs_data = [pydantic_to_dict(job) for job in jobs]

    #API call for the match-maker
    r = httpx.post(f'{base_url}/v1/matching_jobs', json={'candidate': candidate_data, 'jobs': jobs_data})
  
    #converting the list of doctionaries to a list of pydantic classes
    best_jobs_dict = r.json()['best_jobs']
    best_jobs = [Job(**job) for job in best_jobs_dict]
    
    return best_jobs

def matching_candidates(job: Job) -> List[Candidate]:
    #importing list from DB
    candidates = find_candidates_list() #async

    #converting pydantic classes into dictionaries
    job_data = pydantic_to_dict(job)
    candidates_data = [pydantic_to_dict(candidate) for candidate in candidates]

    #API call for the match-maker
    r = httpx.post(f'{base_url}/v1/matching_candidates', json={'job': job_data, 'candidates': candidates_data})

    #converting the list of doctionaries to a list of pydantic classes
    best_candidates_dict = r.json()['best_candidates']
    best_candidates = [Candidate(**candidate) for candidate in best_candidates_dict]
    
    return best_candidates

if __name__ == "__main__":
    jobs = find_jobs_list()
    jobs_data = [pydantic_to_dict(job) for job in jobs]
    print(jobs_data[0])