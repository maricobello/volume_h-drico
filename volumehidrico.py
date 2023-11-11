import streamlit as st

st.title('Aplicativo do Modelo de Energia de Usina Hidrelétrica Reversível 💡')
st.image('https://miro.medium.com/v2/resize:fit:1400/1*b73XdFeTPNkEJwfyuXT_EQ.gif', width=400, caption='Projeto de Usina Hidrelétrica.')

st.markdown("""
Este aplicativo calcula a energia disponível (em MWh) em um sistema hipotético de reservatórios. 
O usuário fornece parâmetros como os níveis e volumes dos reservatórios superior e inferior, 
bem como os valores de eficiência da bomba e do gerador. O aplicativo então calcula e exibe a 
altura líquida, eficiência geral e a energia disponível. Insira os valores abaixo e clique em 'Calcular' 
para ver os resultados.
""")

# constantes
densidade_agua = 1000  # kg/m³
gravidade = 9.81  # m/s²

# obtenha entradas do usuário
nivel_reservatorio_superior = st.number_input('Nível do Reservatório Superior (m)', value=10000.0)  # metros
nivel_reservatorio_inferior = st.number_input('Nível do Reservatório Inferior (m)', value=2000.0)  # metros
volume_reservatorio_superior = st.number_input('Volume do Reservatório Superior (metros cúbicos)', value=120000.0)  # metros cúbicos
volume_reservatorio_inferior = st.number_input('Volume do Reservatório Inferior (metros cúbicos)', value=40000.0)  # metros cúbicos
eficiencia_bomba = st.number_input('Eficiência da Bomba (decimal)', value=0.95)  # decimal
eficiencia_gerador = st.number_input('Eficiência do Gerador (decimal)', value=0.9)  # decimal

if st.button('Calcular'):
    # calcule a altura líquida e a eficiência geral
    altura_liquida = nivel_reservatorio_superior - nivel_reservatorio_inferior  # metros
    eficiencia_geral = eficiencia_bomba * eficiencia_gerador

    # calcule a energia disponível
    energia_disponivel = ((volume_reservatorio_superior - volume_reservatorio_inferior) * altura_liquida * densidade_agua * gravidade * eficiencia_geral) / 3600 / 1000  # MWh

    # imprima variáveis e resultados para depuração
    st.markdown(f"### Variáveis de entrada:")
    st.markdown(f"- Nível do reservatório superior: {nivel_reservatorio_superior} m")
    st.markdown(f"- Nível do reservatório inferior: {nivel_reservatorio_inferior} m")
    st.markdown(f"- Volume do reservatório superior: {volume_reservatorio_superior} m³")
    st.markdown(f"- Volume do reservatório inferior: {volume_reservatorio_inferior} m³")
    st.markdown(f"- Eficiência da bomba: {eficiencia_bomba}")
    st.markdown(f"- Eficiência do gerador: {eficiencia_gerador}")

    st.markdown(f"### Cálculos:")
    st.markdown(f"- Altura líquida: {altura_liquida} m")
    st.markdown(f"- Eficiência geral: {eficiencia_geral}")
    st.markdown(f"- Energia disponível: {energia_disponivel} MWh")

    # formate a energia disponível para uma casa decimal
    energia_formatada = "{:.1f}".format(energia_disponivel)

    # exiba a energia disponível
    st.markdown(f'### Energia Disponível: {energia_formatada} MWh')
    st.markdown(f'- Para cada 1000 MWh de energia, você poderia carregar {energia_disponivel / 1000:.0f} carros Tesla Model S.')
