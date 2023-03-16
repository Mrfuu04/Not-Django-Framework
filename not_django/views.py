from abc import (
    ABC,
    abstractmethod,
)


class View(ABC):
    """
    Primary view class.
    """

    @abstractmethod
    def get(self, request):
        pass

    @abstractmethod
    def post(self, request):
        pass
