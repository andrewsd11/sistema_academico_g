"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),

    path('ocupacao.html', OcupacaoView.as_view(), name='ocupacao'),
    path('area.html', AreaView.as_view(), name='area'),
    path('periodo.html', PeriodoView.as_view(), name='periodo'),
    path('turma.html', TurmaView.as_view(), name='turma'),
    path('cidade.html', CidadeView.as_view(), name='cidade'),
    path('tipos_avaliacao.html', Tipos_AvaliacaoView.as_view(), name='tipos_avalicao'),
    path('pessoa.html', PessoaView.as_view(), name='pessoa'),
    path('instituicao.html', InstituicaoView.as_view(), name='instituicao'),
    path('curso.html', CursoView.as_view(), name='curso'),
    path('disciplina.html', DisciplinaView.as_view(), name='disciplinas'),
    path('matricula.html', MatriculaView.as_view(), name='matricula'),
    path('avaliacao.html', AvaliacaoView.as_view(), name='avaliacao'),
    path('frequencia.html', FrequenciaView.as_view(), name='frequencia'),
    path('ocorrencia.html', OcorrenciaView.as_view(), name='ocorrencia'),
    path('disciplinacurso.html', Disciplina_CursoView.as_view(), name='disciplina_curso'),
]
