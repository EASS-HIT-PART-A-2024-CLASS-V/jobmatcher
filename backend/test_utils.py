import pytest
from utils import *
from schemas import *


def test_find_jobs_list():
    jobs = find_jobs_list()
    for j in jobs:
        assert isinstance(j, Job)

def test_find_candidates_list():
    candidates = find_candidates_list()
    for c in candidates:
        assert isinstance(c, Candidate)

def test_find_companies_list():
    company = find_companies_list()
    for c in company:
        assert isinstance(c, Company)

def test_find_skills_list():
    skills = find_skills_list()
    for s in skills:
        assert isinstance(s, Skill)

def test_find_fields_list():
    fields = find_fields_list()
    for f in fields:
        assert isinstance(f, Field)



def test_find_job_by_id():
    job = find_job_by_id(1)
    assert isinstance(job, Job)
    assert job.id == 1

def test_find_candidate_by_id():
    candidate = find_candidate_by_id(1)
    assert isinstance(candidate, Candidate)
    assert candidate.id == 1

def test_find_company_by_id():
    company = find_company_by_id(2)
    assert isinstance(company, Company)
    assert company.id == 2

def test_find_field_by_id():
    field = find_field_by_id(2)
    assert isinstance(field, Field)
    assert field.id == 2
   