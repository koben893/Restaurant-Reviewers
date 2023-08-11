import React, { useEffect, useState } from "react";

function Ratings({ user, onLogin }) {
    const [ratings, setRatings] = useState([]);

    useEffect(() => {
        fetch("http://127.0.0.1:5557/ratings")
            .then((response) => response.json())
            .then((data) => {
                console.log(data); // Check the response data in the console
                setRatings(data);
            })
            .catch((error) => {
                console.error("Error fetching ratings:", error);
            });
    }, []);
    console.log(ratings);
    return (
        <div className="header">
            <h1>Top Ratings</h1>
            <div className="grid-container">
                {ratings.map((rating) => (
                    <div key={rating.id} className="card">
                        <h3>Rating: {rating.rating}</h3>
                        <p>User: {rating.user_name}</p>
                        <p>Restaurant: {rating.restaurant_name}</p>
                        <button className="cardbutton" type="submit">
                            Favorites
                        </button>
                    </div>
                ))}
            </div>
        </div>
    );
}

export default Ratings;