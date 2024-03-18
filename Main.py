import streamlit as st
import re
from datetime import date

from PIL import Image
img = Image.open('001.png')
st.image(img)
st.markdown("### 3º Desafio 200k - Porto Velho/Humaitá")

st.write("📅 Dia 05 de Julho de 2024")
st.write("🏃🏻 Largada às 16hs 🕗")
st.write("📍 Saída: Início do Espaço Alternativo - Av. Jorge Teixeira (Praia)")
st.write("💲 Valor da Inscrição: 500,00 reais Solo e 400,00 reais se for em equipe (valor da inscrição é individual)")
st.caption("")
st.write("Forma de Pagamento:")
st.write("Pix kelioesteves@hotmail.com - Kélio Esteves Xavier - Mercado pago.")
st.write("📱 Mais informações: (69) 99925-9005/ (69) 99308-8323 / (69) 99958-3207")
st.write("🏆 Os atletas receberão camiseta, viseira, sacolinha, medalha e um troféu por equipe ou solo.")
st.write("🚙 Os apoio devem fazer a inscrição para receber camisa e medalha do evento. Em breve link para inscrição do apoio")
st.caption("")
st.write("INSCRIÇÕES:")
st.write("✍ Período de inscrição:")
st.write("Início: 17 de março de 2024")
st.write("Término: 20 de maio 2024 ou até o limite das vagas")
st.page_link("https://www.4shared.com/web/preview/pdf/fFCk8nZrjq", label="{$} Clique aqui para ver o Regulamento {$}")
st.caption("")
st.page_link("http://191.217.246.233:8501/", label="Clique aqui para realizar sua inscrição")



from PIL import Image
img = Image.open('003.png')
st.image(img)
