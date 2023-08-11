import React, { useState } from "react";

function NewRestaurantForm({addRestaurantToState}) {


const [name, setName] =useState ("")
const [rating, setRating] =useState ("")

const newRestaurantSubmit = e => {
  e.preventDefault ()
  const newRestaurant = {
    name: name,
    rating: rating,
  }
  addRestaurantToState(newRestaurant)
}

  return (
    <div className="new-restaurant-form">
      <h2>New Restaurant</h2>
      <form onSubmit = {newRestaurantSubmit}>
        <input onChange = {e => setName(e.target.value)}type="text" name="name" placeholder="Restaurant name" />
        <input onChange = {e => setRating(e.target.value)}type="interger" name="rating" placeholder="Rating 1-5" />
        <button type="submit">Add Restaurant</button>
      </form>
    </div>
  );
}

export default NewRestaurantForm;