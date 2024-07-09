import { useEffect, useState } from "react";
import { getSkills, getField } from "../apiCalles";

export default function CandidateCard({matchEntity}) {
    const [skills, setSkills] = useState([]);
    const [field, setField] = useState("");

    useEffect(() => {
        const fetchData = async () => {
            const skillsData = await getSkills(matchEntity.technical_skills);
            setSkills(skillsData);

            const fieldData = await getField(matchEntity.field_id);
            setField(fieldData);
        }

        fetchData();
    }, [matchEntity]);


    return (
        <div className="job-card">
            <h2>{matchEntity.first_name} {matchEntity.last_name}</h2>
            <p>{matchEntity.description}</p>
            <p>Job Type: {matchEntity.job_type}</p>
            <p>Field: {field.title}</p>
            <p>Experience: {matchEntity.experience_years} years</p>
            <p>Technical Skills: {skills.map(s => s.title).join(", ")}</p>
        </div>
    );
}