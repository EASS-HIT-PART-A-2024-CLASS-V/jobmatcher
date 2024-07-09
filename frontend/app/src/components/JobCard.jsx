import { useEffect, useState } from "react";
import { getCompany, getSkills, getField } from "../apiCalles";


export default function JobCard({ matchEntity }) {
    const [company, setCompany] = useState(null);
    const [skills, setSkills] = useState([]);
    const [field, setField] = useState("");

    useEffect(() => {
        const fetchData = async () => {
            const companyData = await getCompany(matchEntity.company_id);
            setCompany(companyData);

            const skillsData = await getSkills(matchEntity.technical_skills);
            setSkills(skillsData);

            const fieldData = await getField(matchEntity.field_id);
            setField(fieldData);
        }

        fetchData();
    }, [matchEntity]);


    return (
        <div className="job-card">
            <h2>{matchEntity.title}</h2>
            <p>{matchEntity.description}</p>
            <p>Company: {company ? company.name : "Loading..."}</p>
            <p>Location: {matchEntity.location}</p>
            <p>Salary: ${matchEntity.salary}</p>
            <p>Job Type: {matchEntity.job_type}</p>
            <p>Location: {matchEntity.remote}</p>
            <p>Field: {field.title}</p>
            <p>Experience: {matchEntity.experience_years} years</p>
            <p>Technical Skills: {skills.map(s => s.title).join(", ")}</p>
        </div>
    );
}
