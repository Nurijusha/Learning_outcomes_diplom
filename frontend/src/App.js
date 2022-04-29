import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import Auth from "./Auth/Auth";
import Registration from "./Registration/Registration";
import Congratulation from "./Congratulation/Congratulation";
import SendEmail from "./SendEmail/SendEmail";

import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route exact path="/" element={<Auth />} />
        </Routes>
        <Routes>
          <Route exact path="/reg" element={<Registration />} />
        </Routes>
        <Routes>
          <Route exact path="/congratulation" element={<Congratulation />} />
        </Routes>
        <Routes>
          <Route exact path="/send_email" element={<SendEmail />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
