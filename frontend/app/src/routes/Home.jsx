import { NavLink } from "react-router-dom";
import "../index.css"

export default function Home() {
    return (
        <>
        <NavLink to={"login"} className={"navlink-button"}>Let's go!</NavLink>
        </>
    )
}