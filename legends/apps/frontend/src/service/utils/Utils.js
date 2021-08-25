const FilterQuestionsByCategory = (question_list, category) => {
    return question_list.filter(question => question.category)
}