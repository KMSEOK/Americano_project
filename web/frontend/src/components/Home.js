import React from "react";
import { Link } from "react-router-dom";

const Home = (props) => {
  const places = [
    { id: 1, name: "honkan" },
    { id: 2, name: "wonagan" },
    { id: 3, name: "pogonkan" },
    { id: 4, name: "inmunkan" },
    { id: 5, name: "chayonkan" },
    { id: 6, name: "konhakkan" },
  ];

  return (
    <div>
      {places.map((place) => (
        <div key={place.id}>
          <Link to={`/jobs/${place.name}`}>{place.name}</Link>
        </div>
      ))}
    </div>
  );
};

export default Home;
