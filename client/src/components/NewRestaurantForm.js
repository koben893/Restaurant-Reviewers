import React, { useState } from "react";
import "./Restaurant.css"

function NewRestaurantForm({ addRestaurantToState }) {
    const [name, setName] = useState("");
    const [rating, setRating] = useState("");

    const handleNameChange = (event) => {
    setName(event.target.value);
    };

    const handleRatingChange = (event) => {
    setRating(event.target.value);
    };

    const handleSubmit = async (event) => {
    event.preventDefault();

    if (!name || isNaN(rating) || rating < 1 || rating > 5) {
      alert("Invalid input. Please provide a valid name and rating between 1 and 5.");
      return;
    }

    const newRestaurant = {
      name: name,
      rating: parseInt(rating),
    };

    // Call the function provided by the parent component to add the restaurant
    addRestaurantToState(newRestaurant);

    // Reset form fields
    setName("");
    setRating("");
  };

  return (
    <div className="new-restaurant-form">
      <h2>New Restaurant</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Restaurant Name"
          value={name}
          onChange={handleNameChange}
        />
        <input
          type="number"
          placeholder="Rating 1-5"
          value={rating}
          onChange={handleRatingChange}
        />
        <button type="submit">Add Restaurant</button>
      </form>
    </div>
  );
}

export default NewRestaurantForm;