import React from "react";
import {BrowserRouter, Route} from "react-router-dom";
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import NavBar from "./components/navigation/NavBar"
import CategoryList from "./components/appearance/category/CategoryList";
import GetCategories from "./data/GetCategories";

function App() {

    const categories = GetCategories()

    return (
        <BrowserRouter>
            <div className="App">
                <NavBar />
                <Route path="/" render={() => <CategoryList categories={categories}/>}/>
            </div>
        </BrowserRouter>
    );
}

export default App;
