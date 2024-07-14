import axios, { all } from "axios";

export const getMatches = async (user_id, isCandidate) => {
    //const matchEntities = isCandidate ? candidates : jobs;
    try {
        const url_base = import.meta.env.VITE_URL_BASE || "http://127.0.0.1:8000"
        const url = `${url_base}/v1/${isCandidate ? "jobs" : "candidates"}_match/${user_id}`
        const response = await axios.get(url)
        const matchEntities = response.data.candidates || response.data.jobs
        
        return matchEntities
    } catch (e) {
        console.log("#######ERROR########\ngetMatches")
        console.log(e)
    }
}

export const swipe = async (swiperId, matchEntityId, isCandidate, like) => {
    try {
        const url_base = import.meta.env.VITE_URL_BASE || "http://127.0.0.1:8000"
        const url = `${url_base}/v1/swiping_${isCandidate ? "jobs" : "candidates"}/${swiperId}?${isCandidate ? "job_id" : "cand_id"}=${matchEntityId}&like=${like}`
        const response = await axios.post(url)
        return response.data.match
    } catch (e) {
        console.log("#######ERROR########\nswipe")
        console.log(e)
    }
    //apiCall to the backend
}

export const getCompany = async (companyId) => {
    try {
        const url_base = import.meta.env.VITE_URL_BASE || "http://127.0.0.1:8000"
        const url = `${url_base}/v1/company/${companyId}`
        const response = await axios.get(url)
        return response.data.company
    }
    catch (e) {
        console.log("#######ERROR########\ngetCompany")
        console.log(e)
    }
}

export const getJobs = async (jobIds) => {
    try {
        const url_base = import.meta.env.VITE_URL_BASE || "http://127.0.0.1:8000"
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
    const url_base = import.meta.env.VITE_URL_BASE || "http://127.0.0.1:8000"
    const url = `${url_base}/v1/field/${fieldId}`
    try {
        const response = await axios(url)
        const field = response.data.field
        return field 
    } catch (e)
    {
        console.log("#######ERROR########\ngetField")
        console.log(e)
    }
}

export const getSkills = async (skillIds) => {
    const url_base = import.meta.env.VITE_URL_BASE || "http://127.0.0.1:8000"
    const url = `${url_base}/v1/skills/`
    try {
        const response = await axios.get(url)
        const allSkills = response.data.skills
        const skills = allSkills.filter(skill => skillIds.includes(skill.id))
        return skills
    } catch (e) {
        console.log("#######ERROR########\ngetSkills")
        console.log(e)
    }
}