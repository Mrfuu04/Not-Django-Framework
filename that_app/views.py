from datetime import datetime

from not_django.response import response
from not_django.views import View
from that_app.builders import CategoryBuilder, CourseBuilder, categories, courses


def index_view(request):
    context = {
        'current_date': datetime.today().strftime('%Y-%m-%d'),
        'categories': categories,
    }

    return response(request, 'index.html', context=context)


def about_view(request):
    context = {
        'name': 'Sergei',
        'phone_number': '911',
        'categories': categories,
    }

    return response(request, 'about.html', context=context)


class FormView(View):

    def get(self, request):
        form_url = request["path"]
        context = {
            'form_url': form_url,
            'categories': categories,
        }

        return response(
            request,
            'form.html',
            context=context,
        )

    def post(self, request):
        print(f"post_data = {request['post_data']}")

        return response(request, 'form.html')


class CreateCategoryView(View):

    @staticmethod
    def get_context(request):
        form_url = request["path"]
        context = {
            'form_url': form_url,
            'categories': categories,
        }

        return context

    def get(self, request):
        context = self.get_context(request)

        return response(
            request,
            'create_category.html',
            context=context,
        )

    def post(self, request):
        context = self.get_context(request)
        post_data = request['post_data']

        category_builder = CategoryBuilder()
        # todo Переписать этот геттер с индексами из post
        title = post_data.get('title')[0] if post_data.get('title') else ''
        info = post_data.get('info')[0] if post_data.get('info') else ''

        categories.append(
            category_builder.set_title(
                title
            ).set_info(
                info
            ).build()
        )

        return response(request, 'create_category.html', context=context)


class CreateCourse(View):

    @staticmethod
    def get_context(request):
        form_url = request["path"]
        context = {
            'form_url': form_url,
            'categories': categories,
        }

        return context

    def get(self, request):
        context = self.get_context(request)

        return response(
            request,
            'create_course.html',
            context=context,
        )

    def post(self, request):
        context = self.get_context(request)
        post_data = request['post_data']

        # todo Переписать этот геттер с индексами из post
        course_builder = CourseBuilder()
        title = post_data.get('title')[0] if post_data.get('title') else ''
        info = post_data.get('info')[0] if post_data.get('info') else ''
        price = post_data.get('price')[0] if post_data.get('price') else ''
        category = post_data.get('category')[0] if post_data.get('category') else ''

        courses.append(
            course_builder.set_title(
                title
            ).set_info(
                info
            ).set_price(
                price
            ).set_category(
                category
            ).build()
        )

        return response(
            request,
            'create_course.html',
            context=context,
        )


class CoursesListView(View):

    @staticmethod
    def get_context(request):
        context = {
            'categories': categories,
        }

        return context

    def get(self, request):
        context = self.get_context(request)
        courses_list = []

        query_string = request['ENVIRON'].get('QUERY_STRING')
        if query_string:
            _, cat_id = query_string.split('=')
            for course in courses:
                if course.id == int(cat_id):
                    courses_list.append(course)
        else:
            courses_list = courses

        context.update({'courses': courses_list})

        return response(
            request,
            'courses_list.html',
            context=context,
        )

    def post(self, request):
        pass
