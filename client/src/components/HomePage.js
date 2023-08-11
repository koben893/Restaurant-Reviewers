import React, { useEffect, useState } from "react";
// import homepage from './homepage.css'
import Ratings from './Ratings'
import NewRestaurantForm from './NewRestaurantForm'

function HomePage({user, onLogin}) {
    
const [restaurants, setRestaurants] = useState([])
const addRestaruantToState = NewRestaurantObj =>{
    setRestaurants( [...restaurants, NewRestaurantObj])
}
    
    useEffect(() => {
        fetch('http://127.0.0.1:5557/restaurants')
            .then((response) => response.json())
            .then((data) => setRestaurants(data));
    }, []);
    
    return (
        <div className="header">
            <h1 className="center">Top Rated Restaurants</h1>
            <NewRestaurantForm addRestaurantToState={addRestaruantToState}/>
            <div className="grid-container">
                {restaurants.map((restaurant) => (
                    <div key={restaurant.id} className="card">
                        <img>{restaurant.image}</img>
                        <h1>
                            {restaurant.ratings}
                        </h1>
                        <h3>{restaurant.name}</h3>

                        <button className="cardbutton" type="submit">Favorites</button>
                    </div>
                ))}
            </div>
        </div>
        )
    }


export default HomePage;