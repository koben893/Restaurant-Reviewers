import React from 'react'
import NavBar from './NavBar'
import DarkMode from './DarkMode';

function Header() {
    return (
        <div>
            <DarkMode />
                
            <div>
                <img className='banner-img' src="https://img.freepik.com/free-vector/restaurant-rate-customer-review-isometric-banner_107791-1071.jpg?w=900&t=st=1691551975~exp=1691552575~hmac=99e3fc931948c31128d9698b49ff2665747c946d291f31e94634e27d3112fb07" alt='' /> <br />
            </div>

            <NavBar />

        </div>
    );
}

export default Header;