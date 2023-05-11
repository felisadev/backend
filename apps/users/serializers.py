from rest_framework import serializers

from .models import AssistanceCentre, PersonaParaAsistencia, UsuariosDeApp


class AssistanceCentreSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssistanceCentre
        fields = [
            "latitude",
            "longitude",
            "address",
            "name",
            "cellphone1",
            "cellphone2",
        ]


class PromotoraSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    cellphone = serializers.CharField()

    class Meta:
        model = PersonaParaAsistencia
        fields = ["name", "cellphone"]

    def validate_cellphone(self, value: str):
        is_digit = value.isnumeric()
        return is_digit and len(value) == 8 and value[0] in "67"


class UsuariosDeAppSerializer(serializers.ModelSerializer):
    identifier = serializers.CharField(read_only=True)

    class Meta:
        model = UsuariosDeApp
        fields = ["nombre", "apellido", "ci", "celular", "identifier"]

    def save(self, **kwargs):
        instance = super().create(self.validated_data)
        ci = self.validated_data["ci"]
        instance.identifier = f"{ci}-{instance.id}"
        instance.save()
        self.validated_data["identifier"] = instance.identifier
        return instance
