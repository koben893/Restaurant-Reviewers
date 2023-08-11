import React from 'react';
import '../App.css';
import Header from "./Header"
import PageContainer from "./PageContainer"
import '../darkMode.css';



function App() {
  
  return (
    <div className="App">
      <header className="App-header">
        <Header />
      </header>
      <PageContainer />
    </div>
  );
}
export default App;
