from sphinx.util.compat import Directive


class MyException(Exception):
    pass


class MyChildException(MyException):
    def __init__(self, traceback):
        self.traceback = traceback

    def __str__(self):
        return self.traceback

class BadDirective(Directive):
    required_arguments = 0

    def run(self):
        raise MyChildException('error message')


def setup(app):
    setup.app = app
    setup.config = app.config
    setup.confdir = app.confdir

    app.add_directive('badextension', BadDirective)

    retdict = dict(
        version='0.0',
        parallel_read_safe=True,
        parallel_write_safe=True,
    )

    return retdict
