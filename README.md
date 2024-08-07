# Job Seeker and Company Matching App

This project is a job matching application built using FastAPI and ReactJS. It includes endpoints for matching jobs to candidates and vice versa, as well as swiping functionality for candidates and jobs.

## Building Instructions

1. Clone the Repository. 
   Choose one of the following, according to you preference:

    HTTPS:
    ```bash
    git clone https://github.com/EASS-HIT-PART-A-2024-CLASS-V/jobmatcher
    
    ```
    SSH:
    ```bash
    git clone git@github.com:EASS-HIT-PART-A-2024-CLASS-V/jobmatcher.git
    
    ```
    GitHub CLI:
    ```bash
    gh repo clone EASS-HIT-PART-A-2024-CLASS-V/jobmatcher
    
    ```

2. Build and Run Via docker-compose

    ```bash
    cd jobmatcher
    ```
    ```bash
    docker-compose up
    ```
    
3. Access the Application

    The application should now be available at [http://localhost:5173/](http://localhost:5173/)

## Getting Started

After following the [building instructions](#building-instructions) to run the containers, you can start using the app. 

### Video Instructions
[Link to youtube](https://youtu.be/Nv8GoMkXw34) Sound on!
[![Watch the video](https://img.youtube.com/vi/Nv8GoMkXw34/maxresdefault.jpg)](https://youtu.be/Nv8GoMkXw34)


## Entities Description
There are two "match entities", "job" and "candidate" that should have a "match" when one liked the other and vice versa, according to the "likes" list.

![Diagram](images/diagram.jpg)

## Backend Endpoints

You can also try "swagger" at [http://localhost:8000/docs](http://localhost:8000/docs) and test manually the following endpoints:

### Home

- **GET /**: Returns a simple home message.

### Job Matching

- **GET /v1/jobs_match/{cand_id}**: Matches jobs for a candidate by their ID.

### Candidate Matching

- **GET /v1/candidates_match/{job_id}**: Matches candidates for a job by its ID.

### Swiping Jobs

- **POST /v1/swiping_jobs/{cand_id}**: A candidate swipes (like/dislike) a job and the Database is updated.
  - **Parameters**:
    - `cand_id` (int): The ID of the candidate.
    - `job_id` (int): The ID of the job.
    - `like` (bool): Whether the candidate likes the job.

### Swiping Candidates

- **POST /v1/swiping_candidates/{job_id}**: A job swipes (like/dislike) a candidate and the Database is updated.
  - **Parameters**:
    - `job_id` (int): The ID of the job.
    - `cand_id` (int): The ID of the candidate.
    - `like` (bool): Whether the job likes the candidate.


### Company Information

- **GET /v1/company/{company_id}**: Retrieves information about a company by its ID.

### Jobs List

- **GET /v1/jobs/**: Retrieves a list of all jobs.

### Field Information

- **GET /v1/field/{field_id}**: Retrieves information about a field by its ID.

### Skills List

- **GET /v1/skills/**: Retrieves a list of all skills.

## Match_making Endpoints

You can also try "swagger" at [http://localhost:8001/docs](http://localhost:8001/docs) and test manually the following endpoints:

### Job Matching

- **POST /v1/matching_jobs**: Matches jobs for a candidate.
  - **Request Body**:
    - `candidate` (Candidate): The candidate's information.
    - `jobs` (List[Job]): A list of jobs to match against.

### Candidate Matching

- **POST /v1/matching_candidates**: Matches candidates for a job.
  - **Request Body**:
    - `job` (Job): The job's information.
    - `candidates` (List[Candidate]): A list of candidates to match against.


## Technologies
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
