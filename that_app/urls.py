from that_app.views import index_view, about_view, FormView, CreateCategoryView, CreateCourse, CoursesListView

urls = {
    '': index_view,
    '/about': about_view,
    '/my_form': FormView,
    '/create_course': CreateCourse,
    '/create_category': CreateCategoryView,
    '/courses': CoursesListView,
}
