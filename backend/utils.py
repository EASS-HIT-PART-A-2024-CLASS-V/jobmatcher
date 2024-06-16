from schemas import *
import json

#DB operations
def find_jobs_list(): #async
    from mock_DB import jobs
    return jobs

def find_candidates_list(): #async
    from mock_DB import candidates
    return candidates

def find_job_by_id(job_id: int): #async
    jobs = find_jobs_list()
    for j in jobs:
        if j.id == job_id:
            return j
    return f'job {job_id} not found'

def find_candidate_by_id(candidate_id: int): #async
    candidates = find_candidates_list()
    for c in candidates:
        if c.id == candidate_id:
            return c
    return f'candidate {candidate_id} not found'

############

def match(cand_id:int, job_id:int): 
    candidate = find_candidate_by_id(cand_id) #async
    job = find_job_by_id(job_id) #async
    
    is_matched = (cand_id in job.likes) and (job_id in candidate.likes)

    return is_matched
    
    

