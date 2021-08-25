import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';

function QuestionList(props) {

    return (
        <div className="QuestionList">
            {props.questions.map(question =>
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