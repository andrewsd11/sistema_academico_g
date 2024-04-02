from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(seçf, request):
        pass

class OcupacaoView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacoes' : ocupacoes})
    
class AreaView(View):
    def get(self, request, *args, **kwargs):
        areas = Area.objects.all()
        return render(request, 'area.html', {'areas' : areas})
    
class PeriodoView(View):
    def get(self, request, *args, **kwargs):
        periodos = Periodo.objects.all()
        return render(request, 'periodo.html', {'periodos' : periodos})
    
class TurmaView(View):
    def get(self, request, *args, **kwargs):
        turmas = Turma.objects.all()
        return render(request, 'turma.html', {'turmas' : turmas})
    
class CidadeView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades' : cidades})
    
class Tipos_AvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        tipos_avaliacoes = Tipos_Avaliacao.objects.all()
        return render(request, 'tipos_avaliacao.html', {'tipos_avaliacoes' : tipos_avaliacoes})
    
class PessoaView(View):
    def get(self, request, *args, **kwargs):
        pessoas = Pessoa.objects.all()
        return render(request, 'pessoa.html', {'pessoas' : pessoas})
    
class InstituicaoView(View):
    def get(self, request, *args, **kwargs):
        instituicoes = Instituicao.objects.all()
        return render(request, 'instituicao.html', {'instituicoes' : instituicoes})
    
class CursoView(View):
    def get(self, request, *args, **kwargs):
        cursos = Curso.objects.all()
        return render(request, 'curso.html', {'cursos' : cursos})
    
class DisciplinaView(View):
    def get(self, request, *args, **kwargs):
        disciplinas = Disciplina.objects.all()
        return render(request, 'disciplina.html', {'disciplinas' : disciplinas})
    
class MatriculaView(View):
    def get(self, request, *args, **kwargs):
        matriculas = Matricula.objects.all()
        return render(request, 'matricula.html', {'matriculas' : matriculas})
    
class AvaliacaoView(View):
    def get(self, request, *args, **kwargs):
        avaliacoes = Avaliacao.objects.all()
        return render(request, 'avaliacao.html', {'avaliacoes' : avaliacoes})
    
class FrequenciaView(View):
    def get(self, request, *args, **kwargs):
        frequencias = Frequencia.objects.all()
        return render(request, 'frequencia.html', {'frequencias' : frequencias})
    
class OcorrenciaView(View):
    def get(self, request, *args, **kwargs):
        ocorrencias = Ocorrencia.objects.all()
        return render(request, 'ocorrencia.html', {'ocorrencias' : ocorrencias})
    
class Disciplina_CursoView(View):
    def get(self, request, *args, **kwargs):
        disciplinas_cursos = Disciplina_Curso.objects.all()
        return render(request, 'disciplinacurso.html', {'disciplinas_cursos' : disciplinas_cursos})
