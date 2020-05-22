from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view),
    path('logout', views.logout_view),
    path('register', views.register_view),
    path('my_menus', views.my_menus),
    path('add_menu', views.add_menu),
    path('view_menu/<int:menu_id>', views.view_menu),
    path('edit_menu/<int:menu_id>', views.edit_menu),
    path('remove_menu/<int:menu_id>', views.remove_menu),
    path('add_item/<int:menu_id>', views.add_item),
    path('remove_item/<int:menu_id>/<int:item_id>', views.remove_item),
    path('view_item/<int:menu_id>/<int:item_id>', views.view_item),
    path('edit_item/<int:menu_id>/<int:item_id>', views.edit_item),
]
