/* eslint-disable react/prop-types */
/* eslint-disable react/jsx-key */

import { useState } from "react";
import Form from "../../components/Form";
import './Hills.css';
import { Button } from "@mui/material";

const Hills = ({ hills }) => {
  const [isOpen, setIsOpen] = useState(false);

  const togglePopup = () => {
    setIsOpen(!isOpen);
  };

  let hills_list = null;
  if (hills !== null) {
    hills_list = hills.map((hill) => {
      return (
        <div key={hill.id} className="hill-list-container">
          <li>
            <h2>{hill.name}</h2>
          </li>
          <li><h4>{hill.description ? hill.description : ''}</h4></li>
          <li>Distance(km): {hill.distance_km ? hill.description : ''}</li>
          <li>Ascent(m): {hill.ascent_metres ? hill.ascent_metres : ''}</li>
          <li>Difficulty: {hill.difficulty ? hill.difficulty : ''}</li>
          <li>Latitude: {hill.latitude ? hill.latitude : ''}</li>
          <li>Longitude: {hill.longitude ? hill.longitude : ''}</li>
          <li>Time added: {hill.time_added ? hill.time_added : ''}</li>
          {/* TODO ADD IMAGE TO DB */}
        </div>
      );
    });
  }

  return (
    <div className="hills-container">
      <h1 className="page-heading">Hills</h1>
      <Button variant="contained" onClick={togglePopup}>{!isOpen ? "Add Hill" : "Close"}</Button>
      {isOpen && (
        <div>
          <Form />
        </div>
      )}
      <ul className="hills-list">{hills_list}</ul>
    </div>
  );
};
export default Hills;
