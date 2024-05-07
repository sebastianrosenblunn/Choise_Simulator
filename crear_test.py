import streamlit as st  # Importa streamlit
import pandas as pd  # Importa pandas

def crear_test(df):
    respuestas_usuario = {}

    for i, row in df.iterrows():
        pregunta = row['pregunta']
        respuesta_correcta = row['respuesta']

        st.write(f'{i+1}. {pregunta}')

        # Pasa un identificador único a st.radio
        respuesta_usuario = st.radio('Tu respuesta', ('VERDADERO', 'FALSO'), key=f'radio_{i}')

        # Guarda la respuesta del usuario en el diccionario
        respuestas_usuario[i] = respuesta_usuario

    if st.button('Enviar respuestas'):
        puntuacion = sum(respuestas_usuario[i] == df.loc[i, 'respuesta'] for i in respuestas_usuario)
        porcentaje = puntuacion / len(df) * 100
        st.write(f'Tu puntuación es: {puntuacion}/{len(df)} ({porcentaje:.2f}%)')
