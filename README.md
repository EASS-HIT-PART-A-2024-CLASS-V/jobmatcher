# Job Seeker and Company Matching App
This project is a job matching application built using FastAPI. It includes endpoints for matching jobs to candidates and vice versa, as well as swiping functionality for candidates and jobs.

## Entities Description
There are two "match entities", "job" and "candidate" that should have a "match" when one liked the other and vice versa, according to the "likes" list. For your convenience, short description of each:
### Candidate
The `Candidate` entity represents an individual seeking a job. Each candidate has the following attributes:

- **id (int)**: Unique identifier for the candidate.
- **first_name (str)**: First name of the candidate.
- **last_name (str)**: Last name of the candidate.
- **field_id (int)**: Identifier of the field or industry the candidate is interested in.
- **technical_skills (List[int])**: List of skill identifiers that the candidate possesses.
- **experience_years (conint(ge=0, le=50))**: Number of years of experience the candidate has in their field.
- **likes (List[int])**: List of job identifiers that the candidate likes.
- **dislikes (List[int])**: List of job identifiers that the candidate dislikes.

### Job
The `Job` entity represents a job position offered by a company. Each job has the following attributes:

- **id (int)**: Unique identifier for the job.
- **title (str)**: Title of the job position.
- **description (str)**: Description of the job responsibilities and requirements.
- **company_id (int)**: Identifier of the company offering the job.
- **location (str)**: Location where the job is based.
- **salary (int)**: Salary offered for the job.
- **job_type (JobType)**: Type of job (e.g., Full-Time, Part-Time, Temporary, Internship).
- **remote (Remote)**: Indicates whether the job is On-Site, Remote, or Hybrid.
- **field_id (int)**: Identifier of the field or industry the job belongs to.
- **technical_skills (List[int])**: List of skill identifiers required for the job.
- **experience_years (conint(ge=0, le=50))**: Number of years of experience required for the job.
- **likes (List[int])**: List of candidate identifiers that like this job.
- **dislikes (List[int])**: List of candidate identifiers that dislike this job.


## Instructions to Run Backend Service

1. Clone the Repository
    ```bash
    git clone https://github.com/EASS-HIT-PART-A-2024-CLASS-V/jobmatcher
    
    ```

2. Build Backend Service

    ```bash
    cd jobmatcher/backend
    docker build . -t jobmatcher-backend
    ```
3. Run The Container

    ```bash
    docker run -p 8000:8000 jobmatcher-backend
    ```
    if port 8000 is occupied, You can try an available one, e.g:
    ```bash
    docker run -p 8001:8000 jobmatcher-backend
    ```
4. Access the Application

    The application should now be available at [http://localhost:8000](http://localhost:8000)

    

## API Endpoints

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


