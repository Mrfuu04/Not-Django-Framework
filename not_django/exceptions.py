class AppNotFound(Exception):
    def __init__(self, *args):
        if args:
            self.msg = f"\nCan't find module named {args[0].name}\nCheck your urls"
        else:
            self.msg = "Can't find module"

    def __str__(self):
        return self.msg
