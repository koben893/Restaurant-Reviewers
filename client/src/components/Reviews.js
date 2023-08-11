import React, { useEffect, useState } from 'react'

function Reviews() {

    const [reviews, setReviews] = useState([])
    
    useEffect(() => {
        fetch('http://127.0.0.1:5557/reviews')
            .then((response) => response.json())
            .then((data) => setReviews(data));
    }, []);

    return (
        <div className="header">
            <h1 className="center">Reviews</h1>
            <div className="grid-container">
                {reviews.map((reviews) => (
                    <div key={reviews.id} className="card">
                        <h3>{reviews.name}</h3>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default Reviews