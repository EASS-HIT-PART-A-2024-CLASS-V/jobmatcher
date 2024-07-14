import { useEffect, useState } from "react";
import { getSkills, getField } from "../apiCalles";
import styles from "../styles/CandidateCard.module.css";

export default function CandidateCard({ matchEntity }) {
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
        <div className={styles.candidateCard}>
            <h2>{matchEntity.first_name} {matchEntity.last_name}</h2>
            <p>{matchEntity.description}</p>
            <div className={styles.candidateDetails}>
                <p><strong>Job Type:</strong> {matchEntity.job_type}</p>
                <p><strong>Field:</strong> {field.title}</p>
                <p><strong>Experience:</strong> {matchEntity.experience_years} years</p>
                <p><strong>Technical Skills:</strong> {skills.map(s => s.title).join(", ")}</p>
            </div>
        </div>
    );
}


