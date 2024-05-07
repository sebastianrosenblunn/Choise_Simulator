import streamlit as st
import pandas as pd

from crear_test import crear_test

# Carga tus 5 dataframes
df1 = pd.read_csv('./data/vf1.csv')
df2 = pd.read_csv('./data/vf2.csv')
df3 = pd.read_csv('./data/vf3.csv')
df4 = pd.read_csv('./data/vf4.csv')
df5 = pd.read_csv('./data/vf5.csv')

# Cargar los datos del archivo CSV
choice = pd.read_csv("./data/choices.csv")

# Crea un menú lateral con todas las opciones
pagina = st.sidebar.selectbox('Selecciona una página', ['V-F 1', 'V-F 2', 'V-F 3', 'V-F 4', 'V-F 5', 'choice 1', 'choice 2', 'choice 3', 'choice 4', 'choice 5'])

if pagina == 'V-F 1':
    st.title('V-F 1')
    df = df1
    crear_test(df)

elif pagina == 'V-F 2':
    st.title('V-F 2')
    df = df2
    crear_test(df)

elif pagina == 'V-F 3':
    st.title('V-F 3')
    df = df3
    crear_test(df)

elif pagina == 'V-F 4':
    st.title('V-F 4')
    df = df4
    crear_test(df)

elif pagina == 'V-F 5':
    st.title('V-F 5')
    df = df5
    crear_test(df)

if pagina == 'choice 1':
    st.title('Test de Opción Múltiple')

    respuestas_correctas = 0
    respuestas_incorrectas = 0
    respuestas_seleccionadas = []
    total_preguntas = choice.shape[0]
    
    # Diccionario para mapear respuestas seleccionadas con opciones
    opciones_dict = {'a': 'Opción 1', 'b': 'Opción 2', 'c': 'Opción 3', 'd': 'Opción 4', 'e': 'Opción 5'}

    for index, row in choice.iterrows():
        pregunta = row['pregunta']
        st.write(f"{pregunta}")

        opciones = [row['Opción 1'], row['Opción 2'], row['Opción 3'], row['Opción 4'], row['Opción 5']]
        respuesta_seleccionada = st.radio("Selecciona una respuesta", list(opciones_dict.keys()), key=index)  # Usar keys del diccionario
        respuesta_correcta = opciones_dict[row['Respuesta_correcta']]  # Obtener la opción correcta del diccionario
        respuestas_seleccionadas.append((respuesta_seleccionada, respuesta_correcta))  # Usar el valor correcto directamente

        st.write("---")

    if st.button("Mostrar cantidad de respuestas correctas e incorrectas"):
        for respuesta_seleccionada, respuesta_correcta in respuestas_seleccionadas:
            if respuesta_seleccionada == respuesta_correcta:
                respuestas_correctas += 1
                st.success(f"¡Respuesta correcta! '{respuesta_seleccionada}'")
            else:
                respuestas_incorrectas += 1
                st.error(f"Respuesta incorrecta. La respuesta correcta es: '{respuesta_correcta}'")

        st.write(f"Cantidad de respuestas correctas: {respuestas_correctas}")
        st.write(f"Cantidad de respuestas incorrectas: {respuestas_incorrectas}")
