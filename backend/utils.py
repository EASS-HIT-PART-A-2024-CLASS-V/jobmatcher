from schemas import *
import json
from fastapi import HTTPException

#DB operations

##get collections
def find_jobs_list(): #async
    from mock_DB import jobs
    return jobs

def find_candidates_list(): #async
    from mock_DB import candidates
    return candidates

def find_companies_list(): #async
    from mock_DB import companies
    return companies

def find_skills_list(): 
    from mock_DB import skills
    return skills

def find_fields_list(): 
    from mock_DB import fields
    return fields

##get document
def find_job_by_id(job_id: int): #async
    job_id = int(job_id)
    jobs = find_jobs_list()
    for j in jobs:
        if j.id == job_id:
            return j
    raise HTTPException(status_code=404, detail=f"Job id {job_id} not found")

def find_candidate_by_id(candidate_id: int): #async
    candidate_id = int(candidate_id)
    candidates = find_candidates_list()
    for c in candidates:
        if c.id == candidate_id:
            return c
    raise HTTPException(status_code=404, detail=f"candidate id {candidate_id} not found")

def find_company_by_id(company_id: int): #async
    company_id = int(company_id)
    company = find_companies_list()
    for c in company:
        if c.id == company_id:
            return c
    raise HTTPException(status_code=404, detail=f"company id {company_id} not found")

def find_field_by_id(field_id: int): #async
    field_id = int(field_id)
    fields = find_fields_list()
    for f in fields:
        if f.id == field_id:
            return f
    raise HTTPException(status_code=404, detail=f"company id {field_id} not found")

############

def match(cand_id:int, job_id:int): 
    candidate = find_candidate_by_id(cand_id) #async
    job = find_job_by_id(job_id) #async
    
    is_matched = (cand_id in job.likes) and (job_id in candidate.likes)

    return is_matched
    
    
def pydantic_to_dict(instance):
    instance_dict = instance.model_dump()

    for key in instance_dict:
        if isinstance(instance_dict[key], Enum):
            instance_dict[key] = instance_dict[key].value
    return instance_dict
