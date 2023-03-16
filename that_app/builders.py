from dataclasses import (
    dataclass,
)
from decimal import (
    Decimal,
)
from typing import (
    Optional,
)

# Временное решение. Пока категории и курсы складываю сюда
categories = []
courses = []


@dataclass
class Category:
    id: Optional[int] = 0
    title: Optional[str] = ''
    info: Optional[str] = ''


@dataclass
class Course:
    id: Optional[int] = 0
    category: Optional[Category] = None
    title: Optional[str] = ''
    info: Optional[str] = ''
    price: Optional[Decimal] = Decimal(0)


class CategoryBuilder:
    """Строитель категорий"""

    def __init__(self):
        self.category = Category()

    def set_title(self, title):
        self.category.title = title
        return self

    def set_info(self, info):
        self.category.info = info
        return self

    def build(self):
        self.category.id = len(categories) + 1
        return self.category


class CourseBuilder:
    """Строитель курсов"""

    def __init__(self):
        self.course = Course()

    def set_category(self, category: Category):
        self.course.category = category
        return self

    def set_title(self, title):
        self.course.title = title
        return self

    def set_info(self, info):
        self.course.info = info
        return self

    def set_price(self, price):
        self.course.price = price
        return self

    def build(self):
        self.course.id = len(courses) + 1
        return self.course
