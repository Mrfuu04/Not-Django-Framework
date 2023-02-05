class View:
    """
    Primary view class.
    """
    def __init__(self, request):
        self.get(request)
        self.post(request)

    def get(self, request):
        raise NotImplementedError(f'Определите get в {self.__class__.__name__}')

    def post(self, request):
        raise NotImplementedError(f'Определите post в {self.__class__.__name__}')
