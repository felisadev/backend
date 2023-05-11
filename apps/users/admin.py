from django.contrib import admin

from .models import (AssistanceCentre, Case, NumerosAyudaUsuario, PersonaParaAsistencia, UsuariosDeApp, UsuarioAtendido)

admin.site.register(UsuarioAtendido)

admin.site.site_header = "Felisa Admin"

admin.site.register(UsuariosDeApp)
