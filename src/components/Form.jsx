import { useState } from "react";
import "./Form.css";
import { Button } from "@mui/material";
// TODO 
const Form = () => {
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [distance, setDistance] = useState(0)
  const [ascent, setAscent] = useState(0);
  const [difficulty, setDifficulty] = useState(0);
  const [latitude, setLatitude] = useState(0);
  const [longitude, setLongitude] = useState(0);

  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = {
      name: name,
      description: description,
      distance_km: distance,
      ascent_metres: ascent,
      difficulty: difficulty,
      latitude: latitude,
      longitude: longitude
    };

    try {
      const response = await fetch('http://127.0.0.1:5000/hills', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });

    if (response.ok) {
      console.log('Hill created successfully.')
      setName("");
      setDescription("");
      setDistance("");
      setAscent("");
      setDifficulty("");
      setLatitude("");
      setLongitude("");
      } else {
        console.error('Failed to create hill.')
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

  return (
    <div className="form-container">
        <h2>Add Hill</h2>
        <p>All fields currently mandatory.</p>
      <form className="form-component" onSubmit={handleSubmit}>
        <label>Hill Name: *</label>
        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <label>Description: *</label>
        <input 
            type="text" 
            placeholder="Description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            // required
        />
        <label>Distance(km): *</label>
        <input 
            type="number" 
            placeholder="Distance(km)"
            value={distance}
            onChange={(e) => setDistance(e.target.value)} 
            // required
        />
        <label>Ascent(m): *</label>
        <input 
            type="number" 
            placeholder="Ascent(m)"
            value={ascent}
            onChange={(e) => setAscent(e.target.value)} 
            // required
        />
        <label>Difficulty: *</label>
        <input 
            type="number" 
            min="0"
            max="10"
            placeholder="Difficulty"
            value={difficulty}
            onChange={(e) => setDifficulty(e.target.value)} 
            // required
        />
        <label>Latitude: *</label>
        <input 
            type="number" 
            placeholder="Latitude"
            value={latitude}
            onChange={(e) => setLatitude(e.target.value)} 
            // required
        />
        <label>Longitude: *</label>
        <input 
            type="number" 
            placeholder="Longitude"
            value={longitude}
            onChange={(e) => setLongitude(e.target.value)} 
            // required
        />
        <Button variant="contained" type="submit">Submit</Button>
      </form>
    </div>
  );
};
export default Form;
