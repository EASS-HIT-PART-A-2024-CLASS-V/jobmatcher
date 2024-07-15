import pytest
from main import *
from match_make_server_calls import *
from fastapi.testclient import TestClient
from schemas import *
from typing import List

client = TestClient(app)

def test_matching_jobs():
    cand_test = Candidate(
        id=1,
        email="alicesmith@example.com",
        first_name="Alice",
        last_name="Smith",
        field_id=3,
        experience_years=3,
        technical_skills=[13, 14, 16],
        job_type=JobType.full_time,
        likes=[],
        dislikes=[],
    )
    jobs = matching_jobs(cand_test)
    for j in jobs:
        assert isinstance(j, Job)

def test_matching_candidates():
    job_test = Job(
        id=1,
        title="Software Developer",
        field_id=3,
        description="Develop and maintain web applications.",
        company_id=1,
        location="New York, NY",
        salary=85000,
        technical_skills=[13, 14, 16],
        experience_years=3,
        job_type=JobType.full_time,
        remote=Remote.hybrid,
        likes=[1],
        dislikes=[],
    )
    candidates = matching_candidates(job_test)
    for c in candidates:
        assert isinstance(c, Candidate)


