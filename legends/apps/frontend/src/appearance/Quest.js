import React, {useState, useEffect} from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';

function Quest() {

    const [categories, setCategories] = useState([])

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/categories/`)
            .then(res => {
                setCategories(res.data)
            })
    }, []);

    return (
        <div className="Quest">
            {categories.map(category =>
                <ul className="list-group list-group-horizontal">
                    <li className="list-group-item">
                        {category.category_name}
                    </li>
                    <li className="list-group-item">
                        {category.questions}
                    </li>
                </ul>
            )}
        </div>
    );
}

export default Quest;