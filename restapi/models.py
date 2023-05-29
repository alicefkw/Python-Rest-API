from django.db import models

class Aluno(models.Model):
    # 1 aluno pode ter várias matrículas
    cpf = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    email = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Matricula(models.Model):
    # 1 aluno pode ter várias matrículas
    id = models.IntegerField(primary_key = True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Data de realização')

    def __str__(self):
        return self.id

class Curso(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 100)
    workload = models.IntegerField()

    def __str__(self):
        return self.name


class Aluno_Curso(models.Model):
    aluno_id = models.ForeignKey('Aluno', on_delete=models.DO_NOTHING)
    curso_id = models.ForeignKey('Curso', on_delete=models.DO_NOTHING)

class Aluno_Matricula(models.Model):
    aluno_id = models.ForeignKey('Aluno', on_delete=models.DO_NOTHING)
    matricula_id = models.ForeignKey('Matricula', on_delete=models.DO_NOTHING)
