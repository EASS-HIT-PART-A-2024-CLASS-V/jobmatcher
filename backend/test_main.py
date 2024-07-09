import pytest
from main import *
from fastapi.testclient import TestClient
from schemas import *
from typing import List

client = TestClient(app)

def test_home():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'home'}

def test_jobs_match():
    response = client.get('/v1/jobs_match/1')
    assert response.status_code == 200
    assert 'jobs' in response.json()     

    response = client.get('/v1/jobs_match/-1')
    assert response.status_code == 404


def test_candidates_match():
    response = client.get('/v1/candidates_match/1')
    assert response.status_code == 200
    assert 'candidates' in response.json()     

    response = client.get('/v1/candidates_match/-1')
    assert response.status_code == 404

def test_swiping_jobs():
    
    #should match
    cand_id = 1 
    job_id = 1 #liked candidate 1
    response = client.post(f'/v1/swiping_jobs/{cand_id}?job_id={job_id}&like=true')
    assert response.status_code == 200
    assert response.json()['match'] == True
    
    #should not match
    cand_id = 2 
    job_id = 2 #didnt like candidate 2
    response = client.post(f'/v1/swiping_jobs/{cand_id}?job_id={job_id}&like=true')
    assert response.status_code == 200
    assert response.json()['match'] == False

    #candidate sees the same job for the second time
    cand_id = 3 
    job_id = 3
    response = client.post(f'/v1/swiping_jobs/{cand_id}?job_id={job_id}&like=true')
    assert response.status_code == 400
    assert response.json()['detail'] == 'This candidate has swiped this job already'

    cand_id = 7 
    job_id = 7 #liked candidate 7
    response = client.post(f'/v1/swiping_jobs/{cand_id}?job_id={job_id}&like=false')
    assert response.status_code == 200
    assert response.json()['match'] == False

#########################################

def test_swiping_candidates():

    #should match
    job_id = 4 
    cand_id = 4 #liked job 4 
    response = client.post(f'/v1/swiping_candidates/{job_id}?cand_id={cand_id}&like=true')
    assert response.status_code == 200
    assert response.json()['match'] == True

    #should not match
    job_id = 5 
    cand_id = 5 #didnt like job 5
    response = client.post(f'/v1/swiping_candidates/{job_id}?cand_id={cand_id}&like=true')
    assert response.status_code == 200
    assert response.json()['match'] == False

    #job sees the same candidate for the second time
    job_id = 6
    cand_id = 6 
    response = client.post(f'/v1/swiping_candidates/{job_id}?cand_id={cand_id}&like=true')
    assert response.status_code == 400
    assert response.json()['detail'] == 'This job has swiped this candidate already'
    
    job_id = 8 
    cand_id = 8  #liked job 8
    response = client.post(f'/v1/swiping_candidates/{job_id}?cand_id={cand_id}&like=false')
    assert response.status_code == 200
    assert response.json()['match'] == False

def test_db_routes():
    response = client.get(f'/v1/company/2')
    assert response.status_code == 200
    assert 'company' in response.json()
    company = response.json()['company']
    assert company['id'] == 2


    response = client.get(f'/v1/field/2')
    assert response.status_code == 200
    assert 'field' in response.json()
    field = response.json()['field']
    assert field['id'] == 2

    response = client.get(f'/v1/jobs/')
    assert response.status_code == 200
    assert 'jobs' in response.json()
    jobs = response.json()['jobs']
    assert isinstance(jobs, List)
    
    response = client.get(f'/v1/skills/')
    assert response.status_code == 200
    assert 'skills' in response.json()
    skills = response.json()['skills']
    assert isinstance(skills, List)
    


if __name__ == '__main__':
    try :
        test_db_routes()
    except HTTPException as e:
        print(e)