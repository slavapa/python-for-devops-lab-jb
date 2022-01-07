class App(object):
    def __init__(self, param='some_value'):
        pass

    def public(self):
        return "public method"

    def _indicate_private(self):
        return "private method"


    def __pseudo_private(self):
        return "realy private method"

