import React, {useState, useEffect} from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';
import {NavLink} from "react-router-dom";

function CategoryList() {

    const [categories, setCategories] = useState([])

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/categories/`)
            .then(res => {
                setCategories(res.data)
            })
    }, []);

    return (
        <div className="CategoryList">
            {categories.map(category =>
                <ul className="list-group list-group-horizontal">
                    <NavLink to={category.slug}>
                        <li className="list-group-item">
                        {category.category_name}
                        </li>
                    </NavLink>
                </ul>
            )}
        </div>
    );
}

export default CategoryList;