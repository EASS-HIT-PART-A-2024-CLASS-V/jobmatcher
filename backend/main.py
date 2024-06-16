from fastapi import FastAPI
from schemas import Candidate, Job
from utils import *
from typing import List
app = FastAPI()
def matching_jobs(candidate: Candidate) -> List[Job]:
    jobs = find_jobs_list()
    return jobs
def matching_candidates(job: Job) -> List[Candidate]:
    candidates = find_candidates_list()
    return candidates

@app.get('/')
async def home():
    return {'message': 'home'}

#maybe outsource to a service with some matching algorithm that gives high matching rate
@app.get('/v1/jobs_match/{cand_id}')
async def jobs_match(cand_id:int):
    candidate = find_candidate_by_id(cand_id)
    jobs = matching_jobs(candidate)
    return {'jobs': jobs}

@app.get('/v1/candidates_match/{job_id}')
async def candidates_match(job_id: int):
    job = find_job_by_id(job_id)
    candidates = matching_candidates(job)
    return {'candidates': candidates}

@app.get('/v1/swiping_jobs/{cand_id}')
async def swiping_jobs(cand_id: int, job_id: int, like: bool):
    candidate = find_candidate_by_id(cand_id)
    if like:
        candidate.likes.append(job_id)
        if match(cand_id, job_id):
            return {'match': True}
        else:
            return {'match': False}
    else:
        candidate.dislikes.append(job_id)
    
