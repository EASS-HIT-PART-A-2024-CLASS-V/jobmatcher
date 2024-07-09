import { NavLink, useLoaderData } from "react-router-dom";

export default function CompanyProfile() {
    const {company, jobs} = useLoaderData()
    //console.log(jobs)
    return (
        <div>
            <h1>Profile page</h1>
            <h2>{company.name}</h2>
            {jobs.map((j) => <NavLink key={j.id} to={`/swipe/${j.id}?isCandidate=false`}>{j.title}</NavLink>)}
        </div>
    )

}