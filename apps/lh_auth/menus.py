from django.core.urlresolvers import reverse
from menu import Menu
from apps.main.menus import ViewMenuItem


# Perfil
auth_children = (
    ViewMenuItem(
        "Mi perfil",
        reverse('perfil'),
        weight=10,
        icon="fa-users"),
    ViewMenuItem(
        "Cerrar sesión",
        reverse('custom_logout'),
        weight=10,
        icon="fa-users"))

Menu.add_item(
    "perfil",
    ViewMenuItem(
        "Perfil",
        "javascript:void(0)",
        weight=10,
        icon="fa-key",
        children=auth_children),)
