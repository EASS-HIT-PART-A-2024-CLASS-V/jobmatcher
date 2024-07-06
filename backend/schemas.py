from pydantic import BaseModel, EmailStr, conint
from enum import Enum
from typing import List, Optional, Dict


class Field(BaseModel):
    id: int
    title: str

    '''marketing = 'Marketing'
    tourism = 'Tourism'
    software = 'Software'''

class JobType(Enum):
    full_time = 'Full-Time'
    part_time = 'Part-Time'
    temporary = 'Temporary'
    internship = 'Internship'

class Remote(Enum):
    on_site = 'On-Site'
    remote = 'Remote'
    hybrid = 'Hybrid'

class Skill(BaseModel): 
    id: int
    title: str
    field_id: int


class MatchEntity(BaseModel):
    id: int #maybe later i'll have special ID class or something
    field_id: int
    technical_skills: List[int]
    experience_years: conint(ge=0, le=50)
    #likes = Dict[int, bool] #{some id: True==like False==dislike}
    likes : List[int]
    dislikes : List[int]

class Job(MatchEntity):
    title: str
    description: str
    company_id: int
    location: str
    salary: int
    job_type: JobType
    remote: Remote

class Candidate(MatchEntity):
    first_name: str
    last_name: str

###This is only foundation for further classes development###
class User(BaseModel):
    id: int
    email: EmailStr

class Company(User):
    name: str
    job_ids: List[int]
#######################################################