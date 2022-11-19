from flet.view import View


class PageRouter:
    def __init__(self):
        self.objs = []  # List of View objects to pass to the page

    def view_route(self, route: str = None, function_as_route: bool = False):
        def view_func(func):
            view = func()
            assert isinstance(
                view, View
            ), f"The function '{func.__name__}' must return a View object"
            view.route = (
                route if not function_as_route else "/" + func.__name__
            )  # Initializing route for view

            self.objs.append(
                view
            )  # Appending View objects into `self.objs` to access them from `page` class
            return func

        return view_func
