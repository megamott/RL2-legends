import React from "react";
import {BrowserRouter, Route} from "react-router-dom";
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import NavBar from "./components/navigation/NavBar"
import CategoryList from "./components/appearance/category/CategoryList";

function App() {
    return (
        <BrowserRouter>
            <div className="App">
                <NavBar />
                <Route path="/" component={CategoryList}/>
            </div>
        </BrowserRouter>
    );
}

export default App;
