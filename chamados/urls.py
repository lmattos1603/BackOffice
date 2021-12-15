from django.urls import path
from .views import list_chamados, create_chamados, update_chamados, delete_chamados, login_user, submit,logout_user,list_setores,create_setor,update_setor,delete_setor,alterar_senha
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Tickets
    path('', list_chamados, name='list_chamados'),
    path('list', list_chamados, name='list_chamados'),
    path('new', create_chamados, name='create_chamados'),
    path('update/<int:id>', update_chamados, name='update_chamados'),
    path('delete/<int:id>', delete_chamados, name='delete_chamados'),

    # Setores
    path('setores/list', list_setores, name='list_setores'),
    path('setores/new', create_setor, name='create_setor'),
    path('setores/update/<int:id>', update_setor, name='update_setor'),
    path('setores/delete/<int:id>', delete_setor, name='delete_setor'),

    # Usuarios
    path('users/login', login_user, name='login_user'),
    path('users/submit', submit, name='submit'),
    path('users/logout', logout_user, name='logout_user'),
    path('users/alterar_senha/<int:id>', alterar_senha, name='alterar_senha'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)