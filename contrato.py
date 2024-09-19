#Poderia coloca-lo no arquivo app.py, porém ficaria extenso 
#Ele é uma regra de validação de dados 
# O contrato garante que qualquer dado seu, que seja: (excel, banco de dados, API, dashboard) seja feito uma verificação dele, ou seja qualque coisa swue vc precisa que seja validados os dados usando a lib pydantic.
# O python tem suas tipagens padrão, string, int, float, boolean e o python não valida isso como as linguagnes tipeScript, java que tem uma tipagem em seus códigos.
# Com isso no python por não ter tipagem ele dificilmente quebra, porém op pydantic tem validações mais complexas e meio que trasnforma o python em um java.

# BASICAMENTE se cria uma classe, chama ele de contrato e seguir: !!!!!!! LEMBRANDO QUE TODA CLASSE CRIADA PRECISA TER A LETRA INICIAL MAIUSCULA 



from datetime import datetime
from typing import Tuple

# similar a classe dataclases é uma classe ou um objeto que não tem métodos e isso garante o meu banco de dados que garante que as tipagens do meu python sejam iguais ao meu BD

from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt # validate_call, 
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1= "ZapFlow com Gemini"
    produto2= "ZapFlow com ChatGPT"
    produto3= "ZapFlow com Llama3.0"



# Em python quando vc usa : vc esta tipando algo e quando = é por que ela é algo
class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum

    #Esta classe do pydantic validate_call, deixa eu construir a minhas lógicas
    """@validate_call("produto")
    def categoria_deve_estar_no_enum(cls, v):
        return v"""