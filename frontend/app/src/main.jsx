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
import { getMatches } from "./apiCalles";

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
        path: "swipe/:user_id",
        element: <Swipe/>,
        loader: async ({params, request}) => {
          const {user_id} = params
          const url = new URL(request.url)
          const isCandidate = (url.searchParams.get("isCandidate")) === "true"
          const matchEntities = await getMatches(user_id, isCandidate)
          return {matchEntities, isCandidate, user_id}
        } 
      }
  
    ]
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);