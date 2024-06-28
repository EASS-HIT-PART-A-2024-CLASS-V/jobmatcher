import { NavLink, Outlet } from "react-router-dom";
import Navbar from "../components/Navbar";
import "../index.css"

export default function Root()
{
    return (
        <div className="root-layout">
            <Navbar/>
            <Outlet/>
        </div>
    )
}