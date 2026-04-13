import streamlit as st
import random

# Configuración de la página
st.set_page_config(page_title="Acceso Restringido", page_icon="🔐")

st.title("🔐 Protocolo de Seguridad: Nivel Crítico")

st.write(
    """
    Se ha detectado un intento de acceso no autorizado a los sentimientos de **Tu Nombre**.
    Para continuar, el sistema requiere validación de la contraparte.
    """
)

# Un toque de humor sobre los besos
st.warning("⚠️ Alerta: Se han detectado múltiples 'robos de besos' en los logs del sistema.")

# La pregunta clave
st.subheader("¿Deseas formalizar este vínculo y pasar de 'Modo Prueba' a 'Producción' (Ser mi novia)?")

col1, col2 = st.columns(2)

with col1:
    if st.button("¡SÍ, ACEPTO! ❤️"):
        st.balloons()
        st.success("✅ Acceso concedido. Has sido promovida a Dueña del Sistema. ¡Te quiero!")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJreGZueGZ4Z3R4Z3R4Z3R4Z3R4Z3R4Z3R4Z3R4Z3R4Z3R4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/lNyvk6pXU7Kog/giphy.gif")

with col2:
    # El botón de "No" que se mueve o da un mensaje gracioso
    if st.button("No..."):
        mensajes_chistosos = [
            "Error 404: Sentimiento no encontrado.",
            "Opción deshabilitada por el administrador.",
            "Inténtalo de nuevo, el mouse parece haber fallado.",
            "¿Segura? El sistema detecta que tus besos dicen lo contrario.",
            "Acceso denegado. Intenta con el botón de la izquierda."
        ]
        st.error(random.choice(mensajes_chistosos))