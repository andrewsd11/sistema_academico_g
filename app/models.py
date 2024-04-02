from django.db import models


class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Ocupação")

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

class Area(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Área")

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Área"
        verbose_name_plural = "Áreas"

class Periodo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Período Cursado")

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Período"
        verbose_name_plural = "Períodos"

class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Sala")
    turno = models.CharField(max_length=100, verbose_name="Turno Cursado")

    def __str__(self):
        return f'{self.nome} {self.turno}'
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f'{self.nome} {self.uf}'
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Tipos_Avaliacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipos de Avaliação")

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "Tipo de Avaliação"
        verbose_name_plural = "Tipos de Avaliações"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Pessoa")
    nome_pai = models.CharField(max_length=100, verbose_name="Nome do Pai")
    nome_mae = models.CharField(max_length=100, verbose_name="Nome da Mãe")
    cpf = models.CharField(max_length=100, verbose_name="CPF")
    data_nasc = models.DateField(verbose_name="Data de Nascimento")
    email = models.EmailField(max_length=100, verbose_name="Email da Pessoa")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação")

    def __str__(self):
        return f'{self.nome} {self.nome_pai} {self.nome_mae} {self.cpf} {self.data_nasc} {self.email} {self.cidade} {self.ocupacao}'
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class Instituicao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Instituição")
    site = models.CharField(max_length=100, verbose_name="Site da Instituição")
    telefone = models.CharField(max_length=14, verbose_name="Telefone da Instituição")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade")


    def __str__(self):
        return f'{self.nome} {self.site} {self.telefone} {self.cidade}'
    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"

class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Curso")
    carga_horaria = models.IntegerField(verbose_name="Carga Horária do Curso (total)")
    duracao_meses = models.CharField(max_length=14, verbose_name="Duração em Meses do Curso")
    area_saber = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Área de Saber")
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituição")

    def __str__(self):
        return f'{self.nome} {self.carga_horaria} {self.duracao_meses} {self.area_saber} {self.instituicao}'
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Curso"

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Disciplina")
    area_saber = models.ForeignKey(Area, on_delete=models.CASCADE, verbose_name="Área de Saber")    

    def __str__(self):
        return f'{self.nome} {self.area_saber}'
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE, verbose_name="Instituição")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso para Matrìcula")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Aluno para Matricular")    
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_pre_termino = models.DateField(verbose_name="Data Prevista para Término")


    def __str__(self):
        return f'{self.instituicao} {self.curso} {self.pessoa} {self.data_inicio} {self.data_pre_termino}'
    class Meta:
        verbose_name = "Matrícula"
        verbose_name_plural = "MatrÌculas"

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição da Avaliação")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso para Avaliação")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina para Avaliação")

    def __str__(self):
        return f'{self.descricao} {self.curso} {self.disciplina}'
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso para Checar Frequência")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina para Checar Frequência")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Aluno para Checar Frequência")   
    numero_faltas = models.IntegerField(verbose_name="Número de Faltas do Aluno") 

    def __str__(self):
        return f'{self.curso} {self.disciplina} {self.pessoa} {self.numero_faltas}'
    class Meta:
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"

class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Descrição da Ocorrência")
    data_ocorrencia = models.DateField(verbose_name="Data da Ocorrência")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso do Aluno")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina do Aluno")
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="Aluno que levou a Ocorrência")   

    def __str__(self):
        return f'{self.descricao} {self.data_ocorrencia} {self.curso} {self.disciplina} {self.pessoa}'
    class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"

class Disciplina_Curso(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina para Manter")
    carga_horaria = models.IntegerField(verbose_name="Carga horária em meses do curso")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso para Manter")
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, verbose_name="Período para Manter")

    def __str__(self):
        return f'{self.disciplina} {self.carga_horaria} {self.curso} {self.periodo}'
    class Meta:
        verbose_name = "Disciplina por Curso"
        verbose_name_plural = "Disciplinas por Cursos"