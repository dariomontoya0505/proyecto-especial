import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Security Audit - Dario", page_icon="🕵️‍♂️")

st.title("🔐 Análisis de Vulnerabilidades del Sistema")

st.write(
    """
    **Informe de Estado:** Se ha ejecutado un escaneo profundo en el servidor central de **Dario**. 
    Los resultados indican que las defensas han sido vulneradas exitosamente.
    """
)

# El toque de los besos (mantenemos el humor)
st.warning("⚠️ **Log detectado:** Múltiples 'robos de besos' registrados. El sistema ya no puede ignorar esta actividad.")

# La nueva pregunta: Más tranquila y directa
st.subheader("¿Confirmas que esto que está pasando te gusta tanto como a mí?")

st.info("Nota: Si confirmas, se habilitará el acceso a contenido exclusivo (más citas y más besos).")

col1, col2 = st.columns(2)

with col1:
    if st.button("¡CONFIRMO! ❤️"):
        st.balloons()
        st.success("✅ **Vulnerabilidad aceptada.** Me encantas y me encanta lo que está pasando entre nosotros. ¡Sigamos sumando logs de estos!")
        # Una imagen más tierna/divertida
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJreGZueGZ4Z3R4Z3R4Z3R4Z3R4Z3R4Z3R4Z3R4Z3R4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/3o7TKoWXlo3M1nKS6A/giphy.gif")

with col2:
    if st.button("No..."):
        mensajes_chistosos = [
            "Error 500: El sistema se niega a creer esto.",
            "Acción bloqueada. Tus labios dicen otra cosa en el registro.",
            "Inténtalo de nuevo, hubo un lag en tu respuesta.",
            "¿Segura? El administrador del sistema (Dario) tiene otros datos.",
            "Acceso denegado. Prueba el botón verde, es más amigable."
        ]
        st.error(random.choice(mensajes_chistosos))

# Pie de página opcional
st.markdown("---")
st.caption("Hecho con Python y un par de besos robados.")