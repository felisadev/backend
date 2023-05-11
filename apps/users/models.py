from django.db import models

PARENTESCO_CHOICES = (
    ("Otro", "Otro"),
    ("Padre", "Padre"),
    ("Madre", "Madre"),
    ("Hermano", "Hermano"),
    ("Hermana", "Hermana"),
)


class NumerosAyudaUsuario(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    parentesco = models.CharField(
        choices=PARENTESCO_CHOICES, default="OTRO", max_length=100
    )
    otro_parentesco = models.CharField(blank=True, null=True, max_length=100)
    celular = models.IntegerField()
    usuario_app = models.ForeignKey(
        "UsuariosDeApp", related_name="contacto_auxilio", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Número de auxilio"
        verbose_name_plural = "Números de auxilio para usuario"


class UsuariosDeApp(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    creado = models.DateTimeField(auto_now=True)
    ci = models.CharField(max_length=20)
    celular = models.IntegerField()
    identifier = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Cel: {self.celular}"

    class Meta:
        verbose_name = "Usuario de la aplicación"
        verbose_name_plural = "Usuarios de la aplicación"


class UsuarioAtendido(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, blank=True, default="")
    creado = models.DateTimeField(auto_now=True)
    fecha_atendido = models.DateTimeField(blank=True, auto_now=True)
    ci = models.CharField(max_length=20, blank=True, default="")
    celular = models.IntegerField(null=True)
    motivo_consulta = models.TextField(default="")
    usuario_applicacion = models.ForeignKey(UsuariosDeApp, blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Cel: {self.celular}"

    class Meta:
        verbose_name = "Usuario atendido"
        verbose_name_plural = "Usuarios atendidos"


class Case(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(UsuarioAtendido, on_delete=models.CASCADE)
    reason = models.TextField()

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Registro de Caso"
        verbose_name_plural = "Registro de casos"


class AssistanceCentre(models.Model):
    latitude = models.DecimalField(decimal_places=6, max_digits=10)
    longitude = models.DecimalField(decimal_places=6, max_digits=10)
    address = models.TextField(blank=True)
    name = models.CharField(max_length=100)
    link_google_maps = models.CharField(max_length=255, default="")
    cellphone1 = models.CharField(max_length=20)
    cellphone2 = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} {self.address}"

    class Meta:
        ordering = ["name"]
        verbose_name = "Centro de ayuda"
        verbose_name_plural = "Centros de ayuda"


class PersonaParaAsistencia(models.Model):
    name = models.CharField(max_length=100)
    celular = models.CharField(max_length=20)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.celular}"

    class Meta:
        ordering = ["name"]
        verbose_name = "Número Ayuda OMAK"
        verbose_name_plural = "Números de ayuda OMAK"
