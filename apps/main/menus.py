# from django.core.urlresolvers import reverse_lazy
from menu import Menu, MenuItem


class ViewMenuItem(MenuItem):
    def __init__(self, *args, **kwargs):
        super(ViewMenuItem, self).__init__(*args, **kwargs)
        if 'perm' in kwargs:
            self.perm = kwargs.pop('perm')

    def check(self, request):
        """ Revisa los permisos """
        if hasattr(self, 'perm'):
            if request.user.has_perm(self.perm):
                self.visible = True
                return True
            else:
                self.visible = False
        """ Revisa por grupo """
        if hasattr(self, 'group'):
            if request.user.has_perm(self.perm):
                self.visible = True
                return True
            else:
                self.visible = False


Menu.add_item(
    "user",
    ViewMenuItem(
        "Home",
        "#",
        weight=90,
        icon="fa-key"),)
