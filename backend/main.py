from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import Candidate, Job, MatchEntity
from utils import *
from match_make_server_calls import *
from typing import List
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from the specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

#### functions that should utilize matching algorithm
# def matching_jobs(candidate: Candidate) -> List[Job]:
#     jobs = find_jobs_list() #async
#     return jobs
# def matching_candidates(job: Job) -> List[Candidate]:
#     candidates = find_candidates_list() #async
#     return candidates

#API
@app.get('/')
async def home():
    return {'message': 'home'}
@app.get('/v1/jobs_match/{cand_id}')
async def jobs_match(cand_id:int):
    candidate = find_candidate_by_id(cand_id) #async
    if candidate:
        jobs = matching_jobs(candidate)
        return {'jobs': jobs}
    else:
        raise HTTPException(status_code=404, detail=f"couldn't find candidate with id: {cand_id}")

@app.get('/v1/candidates_match/{job_id}')
async def candidates_match(job_id: int):
    job = find_job_by_id(job_id) #async
    if job:
        candidates = matching_candidates(job)
        return {'candidates': candidates}
    else:
        raise HTTPException(status_code=404, detail=f"couldn't find job with id: {job_id}")


@app.post('/v1/swiping_jobs/{cand_id}')
async def swiping_jobs(cand_id: int, job_id: int, like: bool):
    candidate = find_candidate_by_id(cand_id) #async
    response = {'match': False}
    if job_id in candidate.likes or job_id in candidate.dislikes:
        raise HTTPException(status_code=400, detail='This candidate has swiped this job already') 

    if like:
        candidate.likes.append(job_id)
        if match(cand_id, job_id):
            response['match'] = True
    else:
        candidate.dislikes.append(job_id)
    
    return response

@app.post('/v1/swiping_candidates/{job_id}')
async def swiping_candidates(job_id: int, cand_id: int, like: bool):
    job = find_job_by_id(job_id) #async
    response = {'match': False}
    if cand_id in job.likes or cand_id in job.dislikes:
        raise HTTPException(status_code=400, detail='This job has swiped this candidate already')
    if like:
        job.likes.append(cand_id)
        if match(cand_id, job_id):
            response['match'] = True
    else:
        job.dislikes.append(cand_id)
    
    return response

#database routing
@app.get('/v1/company/{company_id}')
async def get_company(company_id):
    company = find_company_by_id(company_id) #async
    response = {'company': company}
    return response

@app.get('/v1/jobs/')
async def get_jobs():
    jobs = find_jobs_list() #async
    response = {'jobs': jobs}
    return response

@app.get('/v1/field/{field_id}')
async def get_field(field_id):
    field = find_field_by_id(field_id)
    response = {'field': field}
    return response

@app.get('/v1/skills/')
async def get_field():
    skills = find_skills_list()
    response = {'skills': skills}
    return response