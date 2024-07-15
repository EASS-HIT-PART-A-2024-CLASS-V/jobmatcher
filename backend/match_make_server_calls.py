from fastapi import HTTPException

from schemas import Candidate, Job
from utils import *
from typing import List


def matching_jobs(candidate: Candidate) -> List[Job]:
    jobs = find_jobs_list() #async
    return jobs
def matching_candidates(job: Job) -> List[Candidate]:
    candidates = find_candidates_list() #async
    return candidates
