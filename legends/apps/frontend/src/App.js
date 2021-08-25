import React from "react";
import {BrowserRouter, Route} from "react-router-dom";
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import NavBar from "./components/navigation/NavBar"
import CategoryList from "./components/appearance/category/CategoryList";
import GetCategories from "./service/requests/GetCategories";

function App() {

    const categories = GetCategories()
    const questionsInCategory = new Map()
    categories.forEach(category => questionsInCategory.set(category.slug, category.questions))

    const state = {
        categoryListPage: {
            categories: categories
        },
        categoryQuestionList: {
            questionsInCategory: questionsInCategory
        }
    }

    return (
        <BrowserRouter>
            <div className="App">
                <NavBar />
                <Route path="/" render={() => <CategoryList state={state}/>}/>
            </div>
        </BrowserRouter>
    );
}

export default App;
