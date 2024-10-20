import streamlit as st
import random

# Inicializando a lista de itens se ainda não existir
if 'itens' not in st.session_state:
    st.session_state.itens = []

if 'selected_image' not in st.session_state:
    st.session_state.selected_image = "mapa-sem-rota.png"  # Imagem inicial

# Lista de 8 imagens aleatórias
image_options = [
    "mapa1/mapa1.png", "mapa1/mapa2.png", "mapa1/mapa3.png", "mapa1/mapa4.png",
    "mapa1/mapa5.png", "mapa1/mapa6.png", "mapa1/mapa7.png", "mapa1/mapa8.png"
]

# Dicionário para mapear os itens às suas imagens correspondentes
item_to_image = {
    "Produto A": "mapa1/mapa1.png",
    "Produto B": "mapa1/mapa2.png",
    "Produto C": "mapa1/mapa3.png",
    "Produto D": "mapa1/mapa4.png",
    "Produto E": "mapa1/mapa5.png",
    "Produto F": "mapa1/mapa6.png",
    "Produto G": "mapa1/mapa7.png",
    "Produto H": "mapa1/mapa8.png",
}

# Função para adicionar um item à lista e alterar a imagem
def adicionar_item():
    item = st.session_state.novo_item
    if item: 
        st.session_state.itens.append(item)
        st.session_state.novo_item = ""  # Limpar a caixa de texto depois de adicionar
        # Selecionar uma imagem aleatória quando um novo item é adicionado
        st.session_state.selected_image = random.choice(image_options)

# Função para limpar a lista de itens
def limpar_lista():
    st.session_state.itens.clear()  
    st.session_state.selected_image = "mapa-sem-rota.png"  # Voltar para a imagem inicial
    st.experimental_rerun()  # Recarregar a página para refletir as alterações

# Carregar e exibir a imagem no sidebar
image_path = "logo-cart.png" 
st.sidebar.image(image_path, width=200)

# Entrada de texto para adicionar novo item
st.sidebar.text_input("Adicionar item:", key='novo_item')
st.sidebar.button("Adicionar", on_click=adicionar_item)

# Exibindo todos os itens como checkboxes na sidebar
st.sidebar.subheader("Itens na lista:")
for item in st.session_state.itens:
    st.sidebar.checkbox(item)

# Botão para limpar a lista
if st.sidebar.button("Limpar lista"):
    limpar_lista()

# Exibindo a imagem correspondente ao item selecionado
st.title("Mapa do Supermercado")
st.image(st.session_state.selected_image, width=800)

# Seção para exibir os itens na lista em um selectbox dentro da sidebar
st.sidebar.subheader("Seleção de itens:")
if st.session_state.itens:
    selecionado = st.selectbox("Selecione um item:", st.session_state.itens)

    # Alterar a imagem com base na seleção
    if selecionado:
        st.session_state.selected_image = random.choice(image_options)

    st.write(f"Você selecionou: {selecionado}")
else:
    st.write("Nenhum item na lista.")
