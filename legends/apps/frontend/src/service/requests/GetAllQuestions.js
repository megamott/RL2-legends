import {useEffect, useState} from "react";
import axios from "axios";

const GetAllQuestions = () => {
    const [questions, setQuestions] = useState([])

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/questions/`)
            .then(res => {
                setQuestions(res.data)
            })
    }, []);

    return questions
}

export default GetAllQuestions