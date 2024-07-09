import axios, { all } from "axios";

export const getMatches = async (user_id, isCandidate) => {
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
        console.log("#######ERROR########\ngetMatches")
        console.log(e)
    }
}

export const swipe = async (swiperId, matchEntityId, isCandidate, like) => {
    try {
        const url_base = "http://127.0.0.1:8000"
        const url = `${url_base}/v1/swiping_${isCandidate ? "jobs" : "candidates"}/${swiperId}?${isCandidate ? "job_id" : "cand_id"}=${matchEntityId}&like=${like}`
        const response = await axios.post(url)
        //console.log(response.data.match)
        return response.data.match
    } catch (e) {
        console.log("#######ERROR########\nswipe")
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
        console.log("#######ERROR########\ngetCompany")
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
        console.log("#######ERROR########\ngetJobs")
        console.log(e)
    }
}

export const getField = async (fieldId) => {
    const url_base = "http://127.0.0.1:8000"
    const url = `${url_base}/v1/field/${fieldId}`
    try {
        const response = await axios(url)
        const field = response.data.field
        //console.log("the field is: ")
        //console.log(field)
        return field 
    } catch (e)
    {
        console.log("#######ERROR########\ngetField")
        console.log(e)
    }
}

export const getSkills = async (skillIds) => {
    const url_base = "http://127.0.0.1:8000"
    const url = `${url_base}/v1/skills/`
    try {
        const response = await axios.get(url)
        const allSkills = response.data.skills
        const skills = allSkills.filter(skill => skillIds.includes(skill.id))
        //console.log(skills)
        return skills
    } catch (e) {
        console.log("#######ERROR########\ngetSkills")
        console.log(e)
    }
}