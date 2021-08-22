import React from "react";
import {BrowserRouter, Route} from "react-router-dom";
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import CategoryList from "./components/appearance/CategoryList";
import CategoryQuestionList from "./components/appearance/CategoryQuestionsList";

function App() {
    return (
        <BrowserRouter>
            <div className="App">
                <Route path="/" component={CategoryList}/>
                <Route path="/optics"><CategoryQuestionList category='optics'/></Route>
                <Route path="/toes"><CategoryQuestionList category='toes'/></Route>
                <Route path="/without-category"><CategoryQuestionList category='without-category'/></Route>
                <Route path="/professors"><CategoryQuestionList category='professors'/></Route>
            </div>
        </BrowserRouter>
    );
}

export default App;
