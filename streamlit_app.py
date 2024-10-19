import streamlit as st
import random

if 'itens' not in st.session_state:
    st.session_state.itens = []

if 'selected_image' not in st.session_state:
    st.session_state.selected_image = "mapa-sem-rota.png"  

image_folders = {
    "pasta1": ["pasta1/imagem1.png", "pasta1/imagem2.png", "pasta1/imagem3.png"],
    "pasta2": ["pasta2/imagem1.png", "pasta2/imagem2.png", "pasta2/imagem3.png"],
    "pasta3": ["pasta3/imagem1.png", "pasta3/imagem2.png", "pasta3/imagem3.png"],
}

def adicionar_item():
    item = st.session_state.novo_item
    if item: 
        st.session_state.itens.append(item)
        st.session_state.novo_item = ""  

def limpar_lista():
    st.session_state.itens.clear()  
    st.session_state.selected_image = "mapa-sem-rota.png"  
    st.experimental_rerun()  

image_path = "logo-cart.png" 
st.sidebar.image(image_path, width=300)

st.sidebar.text_input("Adicionar item:", key='novo_item')
st.sidebar.button("Adicionar", on_click=adicionar_item)

if st.sidebar.button("Limpar lista"):
    limpar_lista()

st.title("Mapa do Supermercado")
st.image(st.session_state.selected_image, width=800)

st.subheader("Itens na lista:")
for item in st.session_state.itens:
    st.checkbox(item)

st.subheader("Seleção de itens:")
if st.session_state.itens:
    selecionado = st.selectbox("Selecione um item:", st.session_state.itens)
    st.write(f"Você selecionou: {selecionado}")
else:
    st.write("Nenhum item na lista.")
