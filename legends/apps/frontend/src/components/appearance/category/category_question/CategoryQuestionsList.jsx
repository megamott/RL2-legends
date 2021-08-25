import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';

const CategoryQuestionList = (props) => {

    return (
        <div className="CategoryList">
            {props.questions.map(question =>
                <ul className="list-group list-group-horizontal">
                    <li className="list-group-item">
                        {question}
                    </li>
                </ul>
            )}
        </div>
    );
}

export default CategoryQuestionList;