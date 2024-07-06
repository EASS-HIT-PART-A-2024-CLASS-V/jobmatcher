import axios from "axios";

export const getMatches = async (user_id, isCandidate) => {
    const candidates = [
        {
            id: 1,
            email: "alicesmith@example.com",
            first_name: "Alice",
            last_name: "Smith",
            field_id: 3,
            experience_years: 3,
            technical_skills: [13, 14, 16],
            likes: [],
            dislikes: []
        },
        {
            id: 2,
            email: "bobjohnson@example.com",
            first_name: "Bob",
            last_name: "Johnson",
            field_id: 1,
            experience_years: 2,
            technical_skills: [1, 4, 5],
            likes: [],
            dislikes: []
        },
        {
            id: 3,
            email: "charliewilliams@example.com",
            first_name: "Charlie",
            last_name: "Williams",
            field_id: 3,
            experience_years: 4,
            technical_skills: [13, 14, 16],
            likes: [3],
            dislikes: []
        }
        // Add other candidates similarly...
    ];
    const jobs = [
        {
            id: 1,
            title: "Software Developer",
            field_id: 3,
            description: "Develop and maintain web applications.",
            company_id: 1,
            location: "New York, NY",
            salary: 85000,
            technical_skills: [13, 14, 16],
            experience_years: 3,
            job_type: "Full Time",
            remote: "Hybrid",
            likes: [1],
            dislikes: []
        },
        {
            id: 2,
            title: "Marketing Specialist",
            field_id: 1,
            description: "Plan and execute marketing campaigns.",
            company_id: 2,
            location: "San Francisco, CA",
            salary: 70000,
            technical_skills: [1, 2, 4],
            experience_years: 2,
            job_type: "Full Time",
            remote: "Remote",
            likes: [],
            dislikes: []
        },
        {
            id: 3,
            title: "Travel Consultant",
            field_id: 2,
            description: "Provide travel planning services to clients.",
            company_id: 3,
            location: "Miami, FL",
            salary: 60000,
            technical_skills: [6, 8, 10],
            experience_years: 4,
            job_type: "Full Time",
            remote: "On Site",
            likes: [],
            dislikes: []
        }
        // Add other jobs similarly...
    ];
    //const matchEntities = isCandidate ? candidates : jobs;
    try {
        const url_base = "http://127.0.0.1:8000"
        const url = `${url_base}/v1/${isCandidate ? "jobs" : "candidates"}_match/${user_id}`
        //console.log("#######SUCCESS########")
        const response = await axios.get(url)
        const matchEntities = response.data.candidates || response.data.jobs
        //console.log(response)
        return matchEntities
    } catch (e) {
        console.log("#######ERROR########")
        console.log(e)
    }
}

export const swipe = async (swiperId, matchEntityId, isCandidate, like) => {
    try {
        const url_base = "http://127.0.0.1:8000"
        const url = `${url_base}/v1/swiping_${isCandidate ? "jobs" : "candidates"}/${swiperId}?${isCandidate ? "job_id" : "cand_id"}=${matchEntityId}&like=${like}`
        const response = await axios.post(url)
        console.log(response.data.match)
        return response.data.match
    } catch (e) {
        console.log("#######ERROR########")
        console.log(e)
    }
    //apiCall to the backend
}

export const getCompany = async (companyId) => {
    try {
        const url_base = "http://127.0.0.1:8000"
        const url = `${url_base}/v1/company/${companyId}`
        const response = await axios.get(url)
        //console.log("#########")
        //console.log(response)
        return response.data.company
    }
    catch (e) {
        console.log("#######ERROR########")
        console.log(e)
    }
}

export const getJobs = async (jobIds) => {
    try {
        const url_base = "http://127.0.0.1:8000"
        const url = `${url_base}/v1/jobs/`
        const response = await axios.get(url)
        const allJobs = response.data.jobs

        const jobs = allJobs.filter(job => jobIds.includes(job.id))

        return jobs
    } catch (e) {
        console.log("#######ERROR########")
        console.log(e)
    }
}
