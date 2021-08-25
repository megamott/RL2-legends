import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import {NavLink, Route} from "react-router-dom";
import CategoryQuestionList from "./category_question/CategoryQuestionsList";

const CategoryList = (props) => {

    const routeComponents = []
    props.state.categoryQuestionList.questionsInCategory.forEach((value, key) =>
        routeComponents.push(<Route exact path={`/${key}`} render={() => <CategoryQuestionList questions={value}/>}/>)
    )

    return (
        <div className="CategoryList category">
            {props.state.categoryListPage.categories.map(category =>
                <ul className="list-group-item">
                    <NavLink to={category.slug}>
                        <li className="list-group-item list-group-item-info">
                            {category.category_name}
                        </li>
                    </NavLink>
                </ul>
            )}
            {routeComponents}
        </div>
    );
}

export default CategoryList;