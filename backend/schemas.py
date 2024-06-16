from pydantic import BaseModel, EmailStr, conint
from enum import Enum
from typing import List, Optional, Dict


class Field(Enum):
    marketing = 'Marketing'
    tourism = 'Tourism'
    software = 'Software'

class JobType(Enum):
    full_time = 'Full-Time'
    part_time = 'Part-Time'
    temporary = 'Temporary'
    internship = 'Internship'

class Remote(Enum):
    on_site = 'On-Site'
    remote = 'Remote'
    hybrid = 'Hybrid'

class Skill(Enum):
    
    # Marketing Skills
    seo = {'name': 'SEO', 'field': Field.marketing}
    content_creation = {'name': 'Content Creation', 'field': Field.marketing}
    social_media_management = {'name': 'Social Media Management', 'field': Field.marketing}
    email_marketing = {'name': 'Email Marketing', 'field': Field.marketing}
    ppc_campaigns = {'name': 'PPC Campaigns', 'field': Field.marketing}

    # Tourism Skills
    travel_planning = {'name': 'Travel Planning', 'field': Field.tourism}
    tour_guiding = {'name': 'Tour Guiding', 'field': Field.tourism}
    customer_service = {'name': 'Customer Service', 'field': Field.tourism}
    itinerary_design = {'name': 'Itinerary Design', 'field': Field.tourism}
    booking_management = {'name': 'Booking Management', 'field': Field.tourism}

    # Software Skills
    debugging = {'name': 'Debugging', 'field': Field.software}
    software_design = {'name': 'Software Design', 'field': Field.software}
    node_js = {'name': 'Node.js', 'field': Field.software}
    react = {'name': 'React', 'field': Field.software}
    c_cpp = {'name': 'C/C++', 'field': Field.software}
    python = {'name': 'Python', 'field': Field.software}
    database_management = {'name': 'Database Management', 'field': Field.software}

class MatchEntity(BaseModel):
    id: int #maybe later i'll have special ID class or something
    field: Field
    technical_skills: List[Skill]
    experience_years: conint(ge=0, le=50)
    #likes = Dict[int, bool] #{some id: True==like False==dislike}
    likes = List[int]
    dislikes = List[int]

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
    jobs: List[Job]
#######################################################