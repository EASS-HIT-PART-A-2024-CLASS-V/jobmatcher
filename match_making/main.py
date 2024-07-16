from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from schemas import Candidate, Job, MatchEntity
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from the specified origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.post('/v1/matching_jobs')
async def matching_jobs(request: Request):
    data = await request.json()
    print("###### in matching_jobs() match making server")

    #extracting dictionaries
    candidate_dict = data['candidate']
    jobs_dicts = data['jobs']

    #converting to pydantic classes
    candidate = Candidate(**candidate_dict)
    jobs = [Job(**job) for job in jobs_dicts]

    #matching algorithm
    print(type(jobs[0]))
    print((jobs[0]))
    return {"best_jobs": jobs}

@app.post('/v1/matching_candidates')
async def matching_candidates(request: Request):
    data = await request.json()  

    print("###### in matching_candidates() match making server")
    #extracting dictionaries
    job_dict = data['job']
    candidates_dict = data['candidates']

    #converting to pydantic classes
    job = Job(**job_dict)
    candidates = [Candidate(**candidate) for candidate in candidates_dict]

    #matching algorithm
    print(type(candidates[0]))
    print((candidates[0]))
    
    return {"best_candidates": candidates}
