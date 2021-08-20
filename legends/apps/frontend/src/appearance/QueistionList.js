import React, {useState, useEffect} from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';

function QuestionList() {

    const [questions, setQuestions] = useState([])

    useEffect(() => {
        axios.get(`http://127.0.0.1:8000/api/questions/`)
            .then(res => {
                setQuestions(res.data)
            })
    }, []);

    return (
        <div className="QuestionList">
            {questions.map(question =>
                <ul className="list-group list-group-horizontal">
                    <li className="list-group-item">
                        {question.question_name}
                    </li>
                    <li className="list-group-item">
                        {question.question_text}
                    </li>
                    <li className="list-group-item">
                        {question.question_answers}
                    </li>

                </ul>
            )}
        </div>
    );
}

export default QuestionList;