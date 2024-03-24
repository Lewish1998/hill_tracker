import { useEffect, useState } from "react";
import Hills from "./Pages/Hills/Hills";
import Navbar from "./Navbar/Navbar";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./Pages/Home/Home";
import Signup from "./Pages/Signup/Signup";
import Login from "./Pages/Login/Login";

function App() {
  const [hills, setHills] = useState(null);

  // Fetching hills data
  useEffect(() => {
    fetch("http://127.0.0.1:5000/hills")
      .then((res) => res.json())
      .then((data) => setHills(data));
  }, []);

  console.log(hills);

  return (
    <div>
      <Router>
        <Navbar />
        <Routes>
          <Route exact path="/" element={<Home />} />
          <Route path="/hills" element={<Hills hills={hills} />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/login" element={<Login />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;

{
  /* <Navbar /> */
}
{
  /* <Hills hills={hills} /> */
}
