import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import GetCategoryQuestionList from "../../../../service/requests/GetCategoryQuestions";

const CategoryQuestionList = (props) => {

    const questions = GetCategoryQuestionList(props)

    return (
        <div className="CategoryList">
            {questions.map(question =>
                <ul className="list-group list-group-horizontal">
                    <li className="list-group-item">
                        {question.question_name}
                    </li>
                    <li className="list-group-item">
                        {question.slug}
                    </li>
                    <li className="list-group-item">
                        {question.question_text}
                    </li>
                </ul>
            )}
        </div>
    );
}

export default CategoryQuestionList;