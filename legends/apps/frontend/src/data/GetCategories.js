import React, {useEffect, useState} from "react";
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

    return categories
}

export default CategoryQuestionList;