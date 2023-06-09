## Representa um Link (Endereço Web).
from django.forms import ModelForm
class Link:
    """
    Representa um Link (Endereço Web).

    ...

    Atributos
    ---------
 

    """
    def __init__(self,title,url,conteudo):
        self.title = title
        self.url = url
        self.conteudo = conteudo

    def __str__(self):
        return f'\n{self.title} = {self.url}\n{self.conteudo}\n'

