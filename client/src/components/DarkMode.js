import { useState, useEffect } from "react";
import "../darkMode.css"


function DarkMode() {

    const [theme, setTheme] = useState('light');

    const toggleTheme = () => {
        theme === 'light' ? setTheme('dark') : setTheme('light')
    }
    useEffect(() => {
        document.body.className = theme;
    }, [theme]);

    return (
        <div class="content">
            <i class="fas fa-sun" id="sun"></i>
            &nbsp;&nbsp;&nbsp;
            <input type="checkbox" id="tooglenight" class="cbx hidden" onClick={toggleTheme} />
            <label for="tooglenight" class="switch"></label>
            &nbsp;&nbsp;&nbsp;
            <i class="fas fa-moon" id="moon"></i>
        </div>
    )
}

export default DarkMode