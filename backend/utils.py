from schemas import Job, Candidate
import json
def find_jobs_list():
    with open ('./mock_DB/jobs.json', 'r') as f:
        jobs_dicts = json.load(f)
    jobs = [Job.parse_obj(job) for job in jobs_dicts]
    return jobs

def find_candidates_list():
    with open ('./mock_DB/candidates.json', 'r') as f:
        candidates_dicts = json.load(f)
    candidates = [Candidate.parse_obj(cand) for cand in candidates_dicts]
    return candidates