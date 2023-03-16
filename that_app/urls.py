from that_app.views import (
    CoursesListView,
    CreateCategoryView,
    CreateCourse,
    FormView,
)

urls = {
    '/my_form': FormView,
    '/create_course': CreateCourse,
    '/create_category': CreateCategoryView,
    '/courses': CoursesListView,
}
