# Neste bloco está a estrutura do app, como um formulário e algumas lógicas


import streamlit as st
# estou chamando o arquivo contrato e também a classe vendas
from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError
from database import salvar_no_postgres


def main():

    st.title("Sistema de CRM e Vendas da ZApFlow - Front End Simples")
    email = st.text_input("Campo de texto para inserção do email do vendedor")
    data = st.date_input("Data da compra", datetime.now())
    hora = st.time_input("Hora da compra", value=time(9, 0)
                         )  # valor padão 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%2f")
    quantidade = st.number_input("Quantidade de Vendas", min_value=1, step=1)
    produto = st.selectbox("Produto", options=[
                           "ZapFlow com Gemini", "ZapFlow com ChatGPT", "ZapFlow com Llama3.0"])

    if st.button("Salvar"):

        # contrato(email, data, hora, valor)
        try:

            data_hora = datetime.combine(data, hora)
            data_hora_formatada = data_hora.strftime("%d/%m/%Y %H:%M:%S")

            venda = Vendas(
                email=email,
                data=data_hora,
                valor=valor,
                quantidade=quantidade,
                produto=produto

            )
            st.write(venda)
            salvar_no_postgres(venda)

        except ValidationError as e:
            st.error(f"Deu erro! {e}")


if __name__ == "__main__":
    main()
