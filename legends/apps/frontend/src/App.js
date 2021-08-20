import React from "react";
import {BrowserRouter, Route} from "react-router-dom";
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import CategoryList from "./appearance/CategoryList";
import QuestionList from "./appearance/QueistionList";

function App() {
    return (
        <BrowserRouter>
            <div className="App">
                <Route path="/" component={CategoryList}/>
                <Route path="/toes" component={QuestionList}/>
            </div>
        </BrowserRouter>
    );
}

export default App;
