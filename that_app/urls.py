from that_app.views import FormView, CreateCategoryView, CreateCourse, CoursesListView

urls = {
    '/my_form': FormView,
    '/create_course': CreateCourse,
    '/create_category': CreateCategoryView,
    '/courses': CoursesListView,
}
