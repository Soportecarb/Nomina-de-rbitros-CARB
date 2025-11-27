from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path("", lambda request: redirect("inicio")),  # raíz → inicio
    path("inicio/", views.inicio, name="inicio"),
    path("mesa/", views.mesa_view, name="mesa"),
    
    # Autenticación
    path("login/", views.login_view, name="login"),
    path("login_admin/", views.login_admin, name="login_admin"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),

    # Funciones protegidas
    path("subir_documento/", views.subir_documento, name="subir_documento"),
    path("buscar_documentos/", views.buscar_documentos, name="buscar_documentos"),
    path("responder_solicitudes/", views.responder_solicitudes, name="responder_solicitudes"),

    # NUEVAS FUNCIONES PARA BOTONES
    path("seguir_expediente/", views.seguir_expediente, name="seguir_expediente"),
    path("solicitud_arbitraje/", views.solicitud_arbitraje, name="solicitud_arbitraje"),
    path("otros/", views.otros, name="otros"),
    path("administrar_sistema/", views.administrar_sistema, name="administrar_sistema"),
]
