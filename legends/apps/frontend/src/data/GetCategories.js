import {useEffect, useState} from "react";
import axios from "axios";

const GetCategories = () => {

    const [categories, setCategories] = useState([])

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/categories/`)
            .then(res => {
                setCategories(res.data)
            })
    }, []);

    return categories
}

export default GetCategories