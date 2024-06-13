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
@app.get('/v1/jobs_match/{user_id}')
async def jobs_match(user_id:int):
    candidate = find_candidate_by_id(user_id)
    jobs = matching_jobs(candidate)
    
    return {'jobs': jobs}

@app.get('/v1/candidates_match/{job_id}') #needs job_id and employee_id
async def candidates_match(job_id: int):
    job = find_job_by_id(job_id)
    candidates = matching_candidates(job)
    return {'candidates': candidates}
