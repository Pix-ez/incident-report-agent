import {
    BrowserRouter,
    Routes,
    Route
} from "react-router-dom"

import Dashboard from "./pages/Dashboard"
import IncidentDetails from "./pages/IncidentDetails"

function App() {

    return (

        <BrowserRouter>

            <Routes>

                <Route
                    path="/"
                    element={<Dashboard />}
                />

                <Route
                    path="/incidents/:incidentId"
                    element={<IncidentDetails />}
                />

            </Routes>

        </BrowserRouter>

    )
}

export default App