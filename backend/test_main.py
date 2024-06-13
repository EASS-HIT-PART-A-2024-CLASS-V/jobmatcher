import pytest
from main import *
from fastapi.testclient import TestClient
from schemas import *

client = TestClient(app)

def test_home():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'home'}

def test_jobs_match():
    response = client.get('/v1/jobs_match/1')
    assert response.status_code == 200
    assert 'jobs' in response.json()     

def test_cndidates_match():
    response = client.get('/v1/candidates_match/1')
    assert response.status_code == 200
    assert 'candidates' in response.json()     




        