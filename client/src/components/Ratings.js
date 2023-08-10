import React, { useEffect, useState } from "react";

function Ratings({user, onLogin}) {
    
        const [ratings, setRatings] = useState([])
    
    useEffect(() => {
        fetch('http://127.0.0.1:5557/reviews')
            .then((response) => response.json())
            .then((data) => setRatings(data));
    }, []);
    
    return (
        <div className="header">
            <h1>Top </h1>
            <div className="grid-container">
                {ratings.map((rating) => (
                    <div key={rating.id} className="card">
                        <h3>{rating.rating}</h3>
                        <button className="cardbutton" type="submit">Favorites</button>
                    </div>
                ))}
            </div>
        </div>
        )
    }


export default Ratings;