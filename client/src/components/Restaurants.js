import React, { useState } from "react";
import NewRestaurantForm from "./NewRestaurantForm";

function Restaurants() {
  const [restaurants, setRestaurants] = useState([]);

  const addRestaurantToState = (newRestaurant) => {
    // Update the restaurants state with the new restaurant
    setRestaurants([...restaurants, newRestaurant]);
  };

  return (
    <div className="header">
      <h1 className="center">Top Rated Restaurants</h1>
      <NewRestaurantForm addRestaurantToState={addRestaurantToState} />
      <div className="grid-container">
        {restaurants.map((restaurant, index) => (
          <div key={index} className="card">
            <h3>{restaurant.name}</h3>
            <p>Rating: {restaurant.rating}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Restaurants;
