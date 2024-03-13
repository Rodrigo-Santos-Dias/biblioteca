
from django import template
from datetime import datetime
register = template.Library()

@register.filter
def tempo_duracao(devolucao,emprestimo):
    if all((isinstance(devolucao,datetime),(emprestimo,datetime))):
        texto =  'Dias'
        duracao = (devolucao-emprestimo).days
        if duracao == 1:
            texto  = 'Dia'
        return f'{duracao} {texto}'
    return 'Não Devolvido'    

