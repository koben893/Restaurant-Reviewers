import React from 'react';
import '../App.css';
import Header from "./Header"
import '../darkMode.css';
import HomePage from './HomePage';


function App() {
  
  return (
    <div className="App">
      <header className="App-header">
        <Header />
        <h1>
          <HomePage/>
        </h1>
      </header>
    </div>
  );
}
export default App;
