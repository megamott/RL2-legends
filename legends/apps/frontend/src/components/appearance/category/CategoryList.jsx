import React, {useState, useEffect} from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';
import {NavLink, Route} from "react-router-dom";
import CategoryQuestionList from "./category_question/CategoryQuestionsList";

function CategoryList() {

    const [categories, setCategories] = useState([])

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/categories/`)
            .then(res => {
                setCategories(res.data)
            })
    }, []);

    return (
        <div className="CategoryList category">
            {categories.map(category =>
                <ul className="list-group-item">
                    <NavLink to={category.slug}>
                        <li className="list-group-item list-group-item-info">
                            {category.category_name}
                        </li>
                    </NavLink>
                </ul>
            )}
            <Route path="/optics" render={() => <CategoryQuestionList category='optics'/>}/>
            <Route path="/toes" render={() => <CategoryQuestionList category='toes'/>}/>
            <Route path="/without-category" render={() => <CategoryQuestionList category='without-category'/>}/>
            <Route path="/professors" render={() => <CategoryQuestionList category='professors'/>}/>
        </div>
    );
}

export default CategoryList;