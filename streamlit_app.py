import streamlit as st
import folium
from streamlit_folium import st_folium
from streamlit_extras.image_coordinates import streamlit_image_coordinates
import plotly.graph_objects as go

# Inicializando o estado para os botões, se ainda não existir
if 'botao1' not in st.session_state:
    st.session_state['botao1'] = False
if 'botao2' not in st.session_state:
    st.session_state['botao2'] = False
if 'botao3' not in st.session_state:
    st.session_state['botao3'] = False

# Lógica dos botões para garantir que só um seja ativado por vez
def clicar_botao1():
    st.session_state['botao1'] = True
    st.session_state['botao2'] = False
    st.session_state['botao3'] = False

def clicar_botao2():
    st.session_state['botao1'] = False
    st.session_state['botao2'] = True
    st.session_state['botao3'] = False

def clicar_botao3():
    st.session_state['botao1'] = False
    st.session_state['botao2'] = False
    st.session_state['botao3'] = True

# Barra lateral com os botões
st.sidebar.title("Nome")
st.sidebar.text("Texto texto texto")

st.sidebar.button("Botao 1", on_click=clicar_botao1)
st.sidebar.button("Botao 2", on_click=clicar_botao2)
st.sidebar.button("Botao 3", on_click=clicar_botao3)

# Lógica para exibir o conteúdo de cada botão
if st.session_state['botao1']:
    # Centro do mapa (pode ser o ponto central do supermercado)
    supermercado_lat = -23.5505
    supermercado_lon = -46.6333

    # Criação do mapa
    mapa = folium.Map(location=[supermercado_lat, supermercado_lon], zoom_start=18)

    # Marcando seções do supermercado
    folium.Marker([supermercado_lat, supermercado_lon], popup='Entrada').add_to(mapa)
    folium.Marker([supermercado_lat + 0.0001, supermercado_lon], popup='Frutas').add_to(mapa)
    folium.Marker([supermercado_lat + 0.0002, supermercado_lon], popup='Laticínios').add_to(mapa)
    folium.Marker([supermercado_lat + 0.0003, supermercado_lon], popup='Carnes').add_to(mapa)

    # Exibir o mapa no Streamlit
    st.title('Mapa do Supermercado')
    st_data = st_folium(mapa, width=725)

if st.session_state['botao2']:
    st.title("Pagina 2")

    # Definir o título da aplicação no Streamlit
    st.title("Mapa Interativo do Supermercado")

    # Criar uma figura Plotly
    fig = go.Figure()

    # Corredores (representados por blocos cinzas)
    fig.add_trace(go.Scatter(
        x=[2, 6, 6, 2, 2], y=[1, 1, 7, 7, 1], fill='toself', name='Corredor Central',
        mode='lines', line=dict(color='gray'), hoverinfo='text', text="Corredor Central"
    ))

    # Prateleiras (representadas por blocos azuis)
    prateleiras = [
        {'name': 'Prateleira 1', 'x': [1, 2, 2, 1, 1], 'y': [1.5, 1.5, 6.5, 6.5, 1.5]},
        {'name': 'Prateleira 2', 'x': [6, 7, 7, 6, 6], 'y': [1.5, 1.5, 6.5, 6.5, 1.5]},
        {'name': 'Prateleira 3', 'x': [2.5, 6, 6, 2.5, 2.5], 'y': [2, 2, 2.5, 2.5, 2]},
        {'name': 'Prateleira 4', 'x': [2.5, 6, 6, 2.5, 2.5], 'y': [3, 3, 3.5, 3.5, 3]},
    ]

    for prateleira in prateleiras:
        fig.add_trace(go.Scatter(
            x=prateleira['x'], y=prateleira['y'], fill='toself', name=prateleira['name'],
            mode='lines', line=dict(color='lightblue'), hoverinfo='text', text=prateleira['name']
        ))

    # Caixas (representadas por blocos verdes)
    fig.add_trace(go.Scatter(
        x=[0.5, 2.5, 2.5, 0.5, 0.5], y=[7.5, 7.5, 8, 8, 7.5], fill='toself', name='Caixa 1',
        mode='lines', line=dict(color='green'), hoverinfo='text', text="Caixa 1"
    ))
    fig.add_trace(go.Scatter(
        x=[7.5, 9.5, 9.5, 7.5, 7.5], y=[7.5, 7.5, 8, 8, 7.5], fill='toself', name='Caixa 2',
        mode='lines', line=dict(color='green'), hoverinfo='text', text="Caixa 2"
    ))

    # Seção de produtos frescos (representada por um bloco laranja)
    fig.add_trace(go.Scatter(
        x=[8.5, 10, 10, 8.5, 8.5], y=[1.5, 1.5, 4.5, 4.5, 1.5], fill='toself', name='Produtos Frescos',
        mode='lines', line=dict(color='orange'), hoverinfo='text', text="Produtos Frescos"
    ))

    # Ajustar layout do gráfico
    fig.update_layout(
        showlegend=True,
        xaxis=dict(range=[0, 10], showgrid=False, zeroline=False),
        yaxis=dict(range=[0, 9], showgrid=False, zeroline=False),
        title="Mapa Interativo do Supermercado",
        width=800, height=600,
        margin=dict(l=40, r=40, b=40, t=40)
    )

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig)


if st.session_state['botao3']:
    st.title("Pagina 3")
