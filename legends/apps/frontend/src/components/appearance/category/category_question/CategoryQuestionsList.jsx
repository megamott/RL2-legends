import React, {useEffect, useState} from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';

const CategoryQuestionList = (props) => {

    const [categories, setCategories] = useState([])

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/categories/${props.category}/`)
            .then(res => {
                return res.data
            })
            .then(res =>
                setCategories(res.question_details)
            )
    }, []);

    return (
        <div className="CategoryList">
            {categories.map(category =>
                <ul className="list-group list-group-horizontal">
                    <li className="list-group-item">
                        {category.question_name}
                    </li>
                    <li className="list-group-item">
                        {category.slug}
                    </li>
                    <li className="list-group-item">
                        {category.question_text}
                    </li>
                </ul>
            )}
        </div>
    );
}

export default CategoryQuestionList;