from schemas import Job, Candidate, Field, JobType, Remote, Skill
import json
def find_jobs_list():
    from mock_DB import jobs
    return jobs

def find_candidates_list():
    from mock_DB import candidates
    return candidates

def find_job_by_id(job_id: int):
    jobs = find_jobs_list()
    for j in jobs:
        if j.id == job_id:
            return j
    return f'job {job_id} not found'

def find_candidate_by_id(candidate_id: int):
    candidates = find_candidates_list()
    for c in candidates:
        if c.id == candidate_id:
            return c
    return f'candidate {candidate_id} not found'


