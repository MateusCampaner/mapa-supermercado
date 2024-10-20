import streamlit as st

# Inicializando a lista de itens se ainda não existir
if 'itens' not in st.session_state:
    st.session_state.itens = []

if 'selected_image' not in st.session_state:
    st.session_state.selected_image = "mapa-sem-rota.png"  # Imagem inicial

# Lista de imagens para diferentes quantidades de itens ticados
tick_to_image = {
    1: "mapa1/mapa1.png",  # Imagem para 1 item
    2: "mapa1/mapa2.png",  # Imagem para 2 itens
    3: "mapa1/mapa3.png",  # Imagem para 3 itens (ou 2 itens com 1 ticado)
    4: "mapa1/mapa4.png",  # Imagem para 2 itens todos ticados
    5: "mapa1/mapa5.png",
    6: "mapa1/mapa6.png",
    7: "mapa1/mapa7.png",
    8: "mapa1/mapa8.png",
}

def adicionar_item():
    item = st.session_state.novo_item
    if item:
        st.session_state.itens.append(item)
        st.session_state.novo_item = ""  # Limpar o campo de entrada após adicionar

def limpar_lista():
    st.session_state.itens.clear()  
    st.session_state.selected_image = "mapa-sem-rota.png"  
    st.experimental_rerun()

image_path = "logo-cart.png" 
st.sidebar.image(image_path, width=200)

st.sidebar.text_input("Adicionar item:", key='novo_item')
st.sidebar.button("Adicionar", on_click=adicionar_item)

st.sidebar.subheader("Itens na lista:")

# Variável para contar quantos itens foram ticados
itens_ticados = 0

# Verifica as checkboxes e conta quantos itens foram marcados
for item in st.session_state.itens:
    if st.sidebar.checkbox(item):
        itens_ticados += 1

# Atualiza a imagem com base na quantidade de itens ticados
if itens_ticados > 0:
    # Se todos os itens estiverem ticados e houver pelo menos 2 itens
    if len(st.session_state.itens) >= 2 and itens_ticados == len(st.session_state.itens):
        st.session_state.selected_image = "mapa1/mapa4.png"
    # Se houver pelo menos 2 itens e pelo menos 1 item ticado
    elif len(st.session_state.itens) >= 2 and itens_ticados >= 1:
        st.session_state.selected_image = "mapa1/mapa3.png"
    elif itens_ticados in tick_to_image:
        st.session_state.selected_image = tick_to_image[itens_ticados]
else:
    if st.session_state.itens:  # Se a lista não estiver vazia
        st.session_state.selected_image = "mapa1/mapa8.png"  # Imagem 8
    else:
        st.session_state.selected_image = "mapa-sem-rota.png"  # Imagem padrão se a lista estiver vazia

# Se houver apenas um item na lista, mostra a imagem mapa1
if len(st.session_state.itens) == 1:
    st.session_state.selected_image = "mapa1/mapa1.png"
# Se houver exatamente dois itens na lista e nenhum deles estiver ticado
elif len(st.session_state.itens) == 2 and itens_ticados == 0:
    st.session_state.selected_image = "mapa1/mapa2.png"

if st.sidebar.button("Limpar lista"):
    limpar_lista()

st.title("Mapa do Supermercado")
st.image(st.session_state.selected_image, width=800)
