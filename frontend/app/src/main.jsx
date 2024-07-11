import * as React from "react";
import * as ReactDOM from "react-dom/client";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import "./index.css";
import Root from "./routes/Root";
import Login from "./routes/Login";
import Home from "./routes/Home";
import Swipe from "./routes/Swipe";
import { getMatches, getCompany, getJobs } from "./apiCalles";
import CompanyProfile from "./routes/CompanyProfile";
import Chat from "./routes/Chat";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Root/>,
    children: [
      {
        path: "/",
        element: <Home/>,
      },
      {
        path: "login",
        element: <Login/>,
      },
      {
        path: "companyprofile/:company_id",
        element: <CompanyProfile/>,
        loader: async ({params, request}) => {
          const {company_id} = params
          const company = await getCompany(company_id)
          const jobs = await getJobs(company.job_ids)
          return {company, jobs}
        }
      },
      {
        path: "swipe/:user_id",
        element: <Swipe/>,
        loader: async ({params, request}) => {
          const {user_id} = params
          const url = new URL(request.url)
          const isCandidate = (url.searchParams.get("isCandidate")) === "true"
          const matchEntities = await getMatches(user_id, isCandidate)
          return {matchEntities, isCandidate, user_id}
        } 
      },
      {
        path: "chat",
        element: <Chat/>
      }
  
    ]
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);