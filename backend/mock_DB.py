from schemas import *
candidates = [
    Candidate(
        id=1,
        email="alicesmith@example.com",
        first_name="Alice",
        last_name="Smith",
        field=Field.software,
        experience_years=3,
        technical_skills=[Skill.node_js, Skill.react, Skill.python]
    ),
    Candidate(
        id=2,
        email="bobjohnson@example.com",
        first_name="Bob",
        last_name="Johnson",
        field=Field.marketing,
        experience_years=2,
        technical_skills=[Skill.seo, Skill.email_marketing, Skill.ppc_campaigns]
    ),
    Candidate(
        id=3,
        email="charliewilliams@example.com",
        first_name="Charlie",
        last_name="Williams",
        field=Field.software,
        experience_years=4,
        technical_skills=[Skill.node_js, Skill.react, Skill.python]
    ),
    Candidate(
        id=4,
        email="davidjones@example.com",
        first_name="David",
        last_name="Jones",
        field=Field.tourism,
        experience_years=5,
        technical_skills=[Skill.travel_planning, Skill.tour_guiding, Skill.customer_service]
    ),
    Candidate(
        id=5,
        email="emmabrown@example.com",
        first_name="Emma",
        last_name="Brown",
        field=Field.software,
        experience_years=2,
        technical_skills=[Skill.react, Skill.python, Skill.database_management]
    ),
    Candidate(
        id=6,
        email="frankdavis@example.com",
        first_name="Frank",
        last_name="Davis",
        field=Field.marketing,
        experience_years=3,
        technical_skills=[Skill.social_media_management, Skill.email_marketing, Skill.seo]
    ),
    Candidate(
        id=7,
        email="gracemiller@example.com",
        first_name="Grace",
        last_name="Miller",
        field=Field.tourism,
        experience_years=4,
        technical_skills=[Skill.tour_guiding, Skill.itinerary_design, Skill.booking_management]
    ),
    Candidate(
        id=8,
        email="hannahwilson@example.com",
        first_name="Hannah",
        last_name="Wilson",
        field=Field.software,
        experience_years=2,
        technical_skills=[Skill.node_js, Skill.python, Skill.react]
    ),
    Candidate(
        id=9,
        email="ianthompson@example.com",
        first_name="Ian",
        last_name="Thompson",
        field=Field.software,
        experience_years=3,
        technical_skills=[Skill.react, Skill.python, Skill.database_management]
    ),
    Candidate(
        id=10,
        email="janeroberts@example.com",
        first_name="Jane",
        last_name="Roberts",
        field=Field.marketing,
        experience_years=2,
        technical_skills=[Skill.seo, Skill.social_media_management, Skill.email_marketing]
    )
]

jobs = [
    Job(
        id=1,
        title="Software Developer",
        field=Field.software,
        description="Develop and maintain web applications.",
        company_id=1,
        location="New York, NY",
        salary=85000,
        technical_skills=[Skill.node_js, Skill.react, Skill.python],
        experience_years=3,
        job_type=JobType.full_time,
        remote=Remote.hybrid
    ),
    Job(
        id=2,
        title="Marketing Specialist",
        field=Field.marketing,
        description="Plan and execute marketing campaigns.",
        company_id=2,
        location="San Francisco, CA",
        salary=70000,
        technical_skills=[Skill.seo, Skill.content_creation, Skill.email_marketing],
        experience_years=2,
        job_type=JobType.full_time,
        remote=Remote.remote
    ),
    Job(
        id=3,
        title="Travel Consultant",
        field=Field.tourism,
        description="Provide travel planning services to clients.",
        company_id=3,
        location="Miami, FL",
        salary=60000,
        technical_skills=[Skill.travel_planning, Skill.customer_service, Skill.booking_management],
        experience_years=4,
        job_type=JobType.full_time,
        remote=Remote.on_site
    ),
    Job(
        id=4,
        title="Full-Stack Developer",
        field=Field.software,
        description="Develop full-stack web applications.",
        company_id=4,
        location="Austin, TX",
        salary=95000,
        technical_skills=[Skill.node_js, Skill.react, Skill.database_management],
        experience_years=5,
        job_type=JobType.full_time,
        remote=Remote.hybrid
    ),
    Job(
        id=5,
        title="SEO Specialist",
        field=Field.marketing,
        description="Optimize websites for search engines.",
        company_id=5,
        location="Los Angeles, CA",
        salary=75000,
        technical_skills=[Skill.seo, Skill.content_creation, Skill.ppc_campaigns],
        experience_years=3,
        job_type=JobType.full_time,
        remote=Remote.remote
    ),
    Job(
        id=6,
        title="Tour Guide",
        field=Field.tourism,
        description="Guide tourists through various destinations.",
        company_id=6,
        location="Las Vegas, NV",
        salary=50000,
        technical_skills=[Skill.tour_guiding, Skill.customer_service, Skill.itinerary_design],
        experience_years=6,
        job_type=JobType.part_time,
        remote=Remote.on_site
    ),
    Job(
        id=7,
        title="Backend Developer",
        field=Field.software,
        description="Develop backend services and APIs.",
        company_id=7,
        location="Seattle, WA",
        salary=90000,
        technical_skills=[Skill.node_js, Skill.python, Skill.database_management],
        experience_years=4,
        job_type=JobType.full_time,
        remote=Remote.hybrid
    ),
    Job(
        id=8,
        title="Email Marketing Specialist",
        field=Field.marketing,
        description="Create and manage email marketing campaigns.",
        company_id=8,
        location="Boston, MA",
        salary=65000,
        technical_skills=[Skill.email_marketing, Skill.content_creation, Skill.social_media_management],
        experience_years=3,
        job_type=JobType.full_time,
        remote=Remote.remote
    ),
    Job(
        id=9,
        title="Customer Service Manager",
        field=Field.tourism,
        description="Manage customer service operations.",
        company_id=9,
        location="Orlando, FL",
        salary=70000,
        technical_skills=[Skill.customer_service, Skill.booking_management, Skill.itinerary_design],
        experience_years=5,
        job_type=JobType.full_time,
        remote=Remote.on_site
    ),
    Job(
        id=10,
        title="Frontend Developer",
        field=Field.software,
        description="Develop frontend user interfaces.",
        company_id=10,
        location="Chicago, IL",
        salary=85000,
        technical_skills=[Skill.react, Skill.node_js, Skill.debugging],
        experience_years=3,
        job_type=JobType.full_time,
        remote=Remote.hybrid
    )
]
