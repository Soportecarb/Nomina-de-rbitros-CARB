from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# --------------------------
#  INICIO
# --------------------------
def inicio(request):
    return render(request, "mesa/inicio.html")


# --------------------------
#  MESA PRINCIPAL
# --------------------------
@login_required
def mesa_view(request):
    if request.user.is_superuser:
        # Vista exclusiva para administrador
        return render(request, "mesa/mesa_admin.html")
    else:
        # Vista exclusiva para usuario normal
        return render(request, "mesa/mesa_usuario.html")

# --------------------------
#  LOGIN NORMAL
# --------------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("usuario")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("mesa")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")

    return render(request, "mesa/login.html")


# --------------------------
#  LOGIN ADMIN
# --------------------------
def login_admin(request):
    if request.method == "POST":
        username = request.POST.get("admin_user")
        password = request.POST.get("admin_pass")

        user = authenticate(request, username=username, password=password)

        if user and user.is_superuser:
            login(request, user)
            return redirect("mesa")

        messages.error(request, "Credenciales inválidas para administrador.")

    return render(request, "mesa/login_admin.html")


# --------------------------
#  LOGOUT
# --------------------------
def logout_view(request):
    logout(request)
    return redirect("inicio")


# --------------------------
#  REGISTRO
# --------------------------
def register_view(request):
    if request.method == "POST":
        user = request.POST.get("usuario")
        password = request.POST.get("password")

        # Registro simple sin formulario complejo
        from django.contrib.auth.models import User

        if User.objects.filter(username=user).exists():
            messages.error(request, "El usuario ya existe.")
        else:
            User.objects.create_user(username=user, password=password)
            messages.success(request, "Cuenta creada correctamente.")
            return redirect("login")

    return render(request, "mesa/register.html")


# --------------------------
#  SUBIR DOCUMENTO
# --------------------------
@login_required
def subir_documento(request):
    messages.success(request, "Función de subir documento próximamente.")
    return redirect("mesa")


# --------------------------
#  BUSCAR DOCUMENTOS
# --------------------------
@staff_member_required
def buscar_documentos(request):
    messages.info(request, "Función de búsqueda de documentos próximamente.")
    return render(request, "mesa/buscar_documentos.html")


# --------------------------
#  RESPONDER SOLICITUDES
# --------------------------
@staff_member_required
def responder_solicitudes(request):
    messages.info(request, "Módulo de respuestas próximamente.")
    return render(request, "mesa/responder_solicitudes.html")

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def seguir_expediente(request):
    return render(request, "mesa/seguir_expediente.html")

@login_required
def solicitud_arbitraje(request):
    return render(request, "mesa/solicitud_arbitraje.html")

@login_required
def otros(request):
    return render(request, "mesa/otros.html")

@staff_member_required
def administrar_sistema(request):
    return render(request, "mesa/administrar_sistema.html")
