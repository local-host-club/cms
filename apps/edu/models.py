from django.db import models
from django.contrib.auth.models import User


class Alumno(models.Model):
    user = models.OneToOneField(User, related_name='alumno')

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name


class CompetenciaArea(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Área de competencias"
        verbose_name_plural = "Áreas de competencias"

    def __str__(self):
        return self.nombre


class Competencia(models.Model):
    nombre = models.CharField(max_length=100)
    area = models.ForeignKey(CompetenciaArea, on_delete=models.PROTECT, related_name='competencia', verbose_name='área')

    class Meta:
        verbose_name = "Competencia"
        verbose_name_plural = "Competencias"

    def __str__(self):
        return self.nombre


class Nivel(models.Model):
    nombre = models.CharField(max_length=100)
    competencia = models.ForeignKey(Competencia, on_delete=models.PROTECT, related_name='nivel')
    porcentaje = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Nivel de competencia"
        verbose_name_plural = "Niveles de competencia"

    def __str__(self):
        return str(self.competencia) + " > " + self.nombre


class Indicador(models.Model):
    descripcion = models.TextField("descripción")
    nivel = models.ForeignKey(Nivel, related_name='indicador')

    class Meta:
        verbose_name = "Indicador"
        verbose_name_plural = "Indicadores"

    def __str__(self):
        return self.descripcion

    def get_porcentaje(self):
        cuenta = Indicador.objects.filter(nivel=self.nivel).count()
        return 1 / cuenta

    def get_porcentaje_total(self):
        porcentaje = self.get_porcentaje()
        return porcentaje * self.nivel.porcentaje / 100


class Nota(models.Model):
    numero = models.PositiveIntegerField("número", default=1)
    descripcion = models.CharField("descripcion", max_length=100, null=True, blank=True)
    indicador = models.ForeignKey(Indicador, related_name='nota')

    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Notas"
        unique_together = (('numero', 'indicador'), )

    def __str__(self):
        if self.descripcion:
            return self.descripcion + str(self.get_nota())
        else:
            return str(self.numero)

    def get_nota(self):
        cuenta = Nota.objects.filter(indicador=self.indicador).count()
        return 1 / cuenta * self.numero

    def get_nota_indicador(self):
        return self.get_nota() * self.indicador.get_porcentaje()

    def get_nota_total(self):
        return self.get_nota() * self.indicador.get_porcentaje_total()


class Evaluacion(models.Model):
    nombre = models.CharField(max_length=140)
    estrategia = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creador_por = models.ForeignKey(User)

    indicador = models.ManyToManyField(Indicador, blank=True, through='EvaluacionIndicador')

    class Meta:
        verbose_name = "Evaluación"
        verbose_name_plural = "Evaluaciones"

    def __str__(self):
        return self.nombre


class EvaluacionIndicador(models.Model):
    evaluacion = models.ForeignKey(Evaluacion, related_name='indicadores')
    indicador = models.ForeignKey(Indicador, related_name='evaluaciones')

    class Meta:
        verbose_name = "Indicador por evaluación"
        verbose_name_plural = "Indicadores por evaluación"

    def __str__(self):
        pass


class EvaluacionAlumno(models.Model):
    alumno = models.ForeignKey(Alumno)
    evaluacion = models.ForeignKey(Evaluacion, verbose_name='evaluación')
    fecha = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "EvaluacionAlumno"
        verbose_name_plural = "EvaluacionAlumnos"

    def __str__(self):
        pass


class EvaluacionNota(models.Model):
    ev_alumno = models.ForeignKey(EvaluacionAlumno)
    ev_indicador = models.ForeignKey(EvaluacionIndicador)
    ev_nota = models.ForeignKey(Nota)
    fecha = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Nota de evaluación"
        verbose_name_plural = "Notas de evaluación"
        unique_together = (("ev_alumno", "ev_indicador"),)

    def __str__(self):
        pass
