from django.core.urlresolvers import reverse
from menu import Menu
from apps.main.menus import ViewMenuItem

EducacionMenu = Menu()

# Perfil
auth_children = (
    ViewMenuItem(
        "Currículo",
        reverse('curriculo'),
        weight=30,
        icon="fa-users"),)

Menu.add_item(
    "educacion",
    ViewMenuItem(
        "Educación",
        "javascript:void(0)",
        weight=30,
        icon="fa-key",
        children=auth_children),)
