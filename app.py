import streamlit as st
import pandas as pd
from datetime import datetime
import qrcode
from io import BytesIO
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Morón Express C.A. - Portal de Optimización Operativa",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados inspirados en APA 7ma y diseño corporativo limpio
st.markdown('''
    <style>
    .main-header {
        font-size: 28px;
        font-weight: bold;
        color: #1E3A8A;
        text-align: center;
        margin-bottom: 10px;
    }
    .sub-header {
        font-size: 16px;
        color: #4B5563;
        text-align: center;
        margin-bottom: 30px;
    }
    .metric-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        padding: 20px;
        border-radius: 8px;
        text-align: center;
    }
    .stAlert {
        font-size: 14px;
    }
    </style>
''', unsafe_allow_html=True)

# Inicializar Base de Datos en session_state si no existe
if "envios_db" not in st.session_state:
    st.session_state.envios_db = pd.DataFrame([
        {
            "Guía": "MRW-849201",
            "Remitente": "Carlos Pacheco",
            "Destinatario": "María Pérez",
            "Cédula Destinatario": "V-12345678",
            "Teléfono": "0412-1234567",
            "Tipo": "Pagado / Exprés",
            "Coordenada Bodega": "Sector A - Bandeja 4",
            "Estatus": "Disponible para Retiro",
            "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
        },
        {
            "Guía": "MRW-849202",
            "Remitente": "Ana Gómez",
            "Destinatario": "Pedro Rojas",
            "Cédula Destinatario": "V-87654321",
            "Teléfono": "0414-7654321",
            "Tipo": "Cobro en Destino",
            "Coordenada Bodega": "Sector B - Bandeja 2",
            "Estatus": "En Tránsito / Recepción",
            "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
    ])

# Sidebar de Navegación
st.sidebar.image("https://img.icons8.com/color/96/delivery-box.png", width=80)
st.sidebar.title("Morón Express C.A.")
st.sidebar.caption("Franquicia Autorizada MRW Venezuela")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Seleccione Módulo:",
    [
        "🏠 Inicio & Diagnóstico", 
        "📱 Pre-Registro & Generador QR (Cliente)", 
        "📦 Inventario & Bodega Alfanumérica (Personal)", 
        "🔍 Autoconsulta de Paquetes (Cliente)", 
        "💬 Plantillas WhatsApp & Mensajería", 
        "📊 Panel Gerencial de Tiempos"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Solución Tecnológica de Tesis**
Optimización de Procesos Operativos y Administrativos
Municipio Juan José Mora, Edo. Carabobo.")

# ----------------------------------------------------
# 1. INICIO & DIAGNÓSTICO
# ----------------------------------------------------
if menu == "🏠 Inicio & Diagnóstico":
    st.markdown('<div class="main-header">Sistema Inteligente de Optimización Operativa</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Agencia Morón Express C.A. (Franquicia MRW Venezuela)</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card"><h3>120</h3><p>Clientes Promedio / Día</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>18.7 min</h3><p>Tiempo Actual / Transacción</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h3>< 6.0 min</h3><p>Meta del Plan Propuesto</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><h3>0.00 $</h3><p>Costo de Licenciamiento</p></div>', unsafe_allow_html=True)
        
    st.markdown("### 🎯 Resumen Ejecutivo de la Herramienta")
    st.write("""
    Esta aplicación web interactiva desarrollada en **Streamlit** resuelve los nudos críticos identificados en el Trabajo Especial de Grado:
    1. **Eliminación de Transcripción Manual en Taquilla (-63% de tiempo):** Mediante pre-registro digital con códigos QR generados desde el teléfono del cliente.
    2. **Reducción de Búsqueda en Bodega (-85% de tiempo):** A través de un sistema de zonificación alfanumérica (`Sector A, B, C` y bandejas numeradas del `0 al 9` según el último dígito de la guía).
    3. **Descongestión de Sala de Espera:** Mediante un portal web de autoconsulta en tiempo real y automatización de avisos por mensajería instantánea (**WhatsApp Business**).
    """)
    
    st.info("👈 Utilice el menú lateral para navegar entre los módulos operativos y de atención al cliente.")

# ----------------------------------------------------
# 2. PRE-REGISTRO & GENERADOR QR (CLIENTE)
# ----------------------------------------------------
elif menu == "📱 Pre-Registro & Generador QR (Cliente)":
    st.markdown('<div class="main-header">Módulo de Pre-Registro de Envíos y Código QR</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Complete sus datos antes de llegar a taquilla para agilizar su atención en menos de 2 minutos</div>', unsafe_allow_html=True)
    
    with st.form("form_preregistro"):
        col1, col2 = st.columns(2)
        with col1:
            remitente = st.text_input("Nombre y Apellido del Remitente", placeholder="Ej. Carlos Pacheco")
            cedula_rem = st.text_input("Cédula de Identidad Remitente", placeholder="Ej. V-15642481")
            telefono_rem = st.text_input("Teléfono de Contacto", placeholder="Ej. 0412-4567890")
            oficina_destino = st.text_input("Oficina MRW Destino", placeholder="Ej. Valencia Centro, Edo. Carabobo")
        with col2:
            destinatario = st.text_input("Nombre y Apellido del Destinatario", placeholder="Ej. Ana Morales")
            cedula_dest = st.text_input("Cédula Destinatario", placeholder="Ej. V-18920192")
            tipo_servicio = st.selectbox("Modalidad del Servicio", ["Encomienda Pagada / Exprés", "Cobro en Destino (COD)"])
            contenido = st.text_area("Descripción breve del contenido", placeholder="Ej. Documentos legales / Repuestos mecánicos")
            
        submitted = st.form_submit_button("Generar Código QR de Envío 🚀")
        
        if submitted:
            if remitente and destinatario and cedula_rem:
                guía_gen = f"MRW-{pd.np.random.randint(100000, 999999)}"
                qr_data = f"Guia: {guia_gen} | Rem: {remitente} ({cedula_rem}) | Dest: {destinatario} | Serv: {tipo_servicio}"
                
                # Generar QR
                qr = qrcode.QRCode(version=1, box_size=10, border=4)
                qr.add_data(qr_data)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")
                
                buffered = BytesIO()
                img.save(buffered, format="PNG")
                
                st.success(f"¡Pre-registro exitoso! Número de Guía Asignado: **{guia_gen}**")
                
                col_a, col_b = st.columns([1, 2])
                with col_a:
                    st.image(buffered.getvalue(), caption="Presente este QR en Taquilla 1 o 2", width=220)
                with col_b:
                    st.markdown(f"""
                    ### 📋 Resumen del Pre-Registro:
                    * **N° de Guía:** `{guia_gen}`
                    * **Remitente:** {remitente} ({cedula_rem})
                    * **Destinatario:** {destinatario}
                    * **Destino:** {oficina_destino}
                    * **Modalidad:** {tipo_servicio}
                    * **Contenido:** {contenido}
                    
                    👉 *Muestre la pantalla de su teléfono o imprima este código QR al llegar a la agencia Morón Express C.A. El operador escaneará sus datos reduciendo el tiempo en taquilla de 4.10 min a menos de 1.5 min.*
                    """)
                
                # Agregar automáticamente al session_state de inventario temporal
                nuevo_registro = {
                    "Guía": guia_gen,
                    "Remitente": remitente,
                    "Destinatario": destinatario,
                    "Cédula Destinatario": cedula_dest,
                    "Teléfono": telefono_rem,
                    "Tipo": tipo_servicio,
                    "Coordenada Bodega": "Por Asignar (Recepción Matutina)",
                    "Estatus": "Pre-registrado (Pendiente en Taquilla)",
                    "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                st.session_state.envios_db = pd.concat([pd.DataFrame([nuevo_registro]), st.session_state.envios_db], ignore_index=True)
            else:
                st.error("Por favor complete al menos los campos obligatorios del remitente y destinatario.")

# ----------------------------------------------------
# 3. INVENTARIO & BODEGA ALFANUMÉRICA (PERSONAL)
# ----------------------------------------------------
elif menu == "📦 Inventario & Bodega Alfanumérica (Personal)":
    st.markdown('<div class="main-header">Control de Inventario y Zonificación de Bodega</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Gestión exclusiva para el equipo de Morón Express C.A. (Reducción de búsqueda a < 45 seg)</div>', unsafe_allow_html=True)
    
    st.subheader("📋 Base de Datos de Envíos y Ubicación Actual")
    
    # Filtro de búsqueda rápida
    filtro_guia = st.text_input("🔍 Buscar por Número de Guía o Cédula:", "")
    df_mostrar = st.session_state.envios_db
    if filtro_guia:
        df_mostrar = df_mostrar[df_mostrar['Guía'].str.contains(filtro_guia, case=False) | df_mostrar['Cédula Destinatario'].str.contains(filtro_guia, case=False)]
        
    st.dataframe(df_mostrar, use_container_width=True)
    
    st.markdown("---")
    st.subheader("🛠️ Actualizar Ubicación en Bodega (Protocolo Matutino)")
    
    with st.form("form_bodega"):
        col1, col2, col3 = st.columns(3)
        with col1:
            guia_sel = st.selectbox("Seleccione Guía a Ubicar", st.session_state.envios_db['Guía'].tolist())
        with col2:
            sector = st.selectbox("Zonificación de Estantería", ["Sector A - Pagadas / Exprés", "Sector B - Cobro en Destino", "Sector C - Carga Voluminosa"])
            bandeja = st.selectbox("Bandeja por Último Dígito", [f"Bandeja {i} (Dígito {i})" for i in range(10)])
        with col3:
            nuevo_estatus = st.selectbox("Actualizar Estatus", ["Disponible para Retiro", "Entregado con Éxito", "En Tránsito"])
            
        btn_actualizar = st.form_submit_button("Actualizar Ubicación y Estatus 💾")
        
        if btn_actualizar:
            coord = f"{sector} - {bandeja}"
            st.session_state.envios_db.loc[st.session_state.envios_db['Guía'] == guia_sel, 'Coordenada Bodega'] = coord
            st.session_state.envios_db.loc[st.session_state.envios_db['Guía'] == guia_sel, 'Estatus'] = nuevo_estatus
            st.success(f"¡Guía {guia_sel} actualizada correctamente a la coordenada **{coord}**!")
            st.rerun()

# ----------------------------------------------------
# 4. AUTOCONSULTA DE PAQUETES (CLIENTE)
# ----------------------------------------------------
elif menu == "🔍 Autoconsulta de Paquetes (Cliente)":
    st.markdown('<div class="main-header">Portal Público de Autoconsulta de Arribo</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Verifique si su paquete está listo para retirar en la agencia sin necesidad de hacer fila</div>', unsafe_allow_html=True)
    
    busqueda = st.text_input("Ingrese su Cédula de Identidad o Número de Guía MRW:", placeholder="Ej. V-12345678 o MRW-849201")
    
    if st.button("Consultar Estatus 🔍"):
        if busqueda:
            resultado = st.session_state.envios_db[
                st.session_state.envios_db['Guía'].str.contains(busqueda, case=False) | 
                st.session_state.envios_db['Cédula Destinatario'].str.contains(busqueda, case=False)
            ]
            
            if not resultado.empty:
                st.success("¡Paquete encontrado en el sistema!")
                for idx, row in resultado.iterrows():
                    st.markdown(f"""
                    ---
                    📦 **Guía:** `{row['Guía']}`
                    * **Destinatario:** {row['Destinatario']} ({row['Cédula Destinatario']})
                    * **Estatus Actual:** 🟢 **{row['Estatus']}**
                    * **Ubicación en Agencia:** 📍 `Coordenada: {row['Coordenada Bodega']}`
                    * **Recomendación:** *Puede pasar a retirarlo en el horario valle recomendado (8:00 a.m. a 10:00 a.m. o 3:00 p.m. a 4:30 p.m.) para una atención inmediata.*
                    """)
            else:
                st.warning("No se encontraron registros activos con ese número de guía o cédula. Verifique los datos o comuníquese con la sucursal.")
        else:
            st.error("Por favor ingrese un número de guía o cédula para realizar la consulta.")

# ----------------------------------------------------
# 5. PLANTILLAS WHATSAPP & MENSAJERÍA
# ----------------------------------------------------
elif menu == "💬 Plantillas WhatsApp & Mensajería":
    st.markdown('<div class="main-header">Centro de Mensajería Instantánea y WhatsApp Business</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Plantillas automatizadas para notificar a clientes y descongestionar la taquilla</div>', unsafe_allow_html=True)
    
    tipo_msg = st.selectbox(
        "Seleccione Plantilla de Notificación:",
        [
            "Notificación de Paquete Disponible para Retiro",
            "Información de Horarios Valle y Tarifas",
            "Recordatorio de Pre-Registro QR"
        ]
    )
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        cli_nombre = st.text_input("Nombre del Cliente", "María Pérez")
        cli_telefono = st.text_input("Teléfono WhatsApp", "584121234567")
        guia_msg = st.text_input("Número de Guía", "MRW-849201")
        ubicacion_msg = st.text_input("Coordenada en Bodega", "Sector A - Bandeja 4")
        
    with col_t2:
        st.markdown("### 📱 Vista Previa del Mensaje")
        if tipo_msg == "Notificación de Paquete Disponible para Retiro":
            mensaje_final = f"¡Hola {cli_nombre}! 📦 Le escribimos de *Morón Express C.A.* (Franquicia MRW Morón). Su guía *{guia_msg}* ya se encuentra disponible para retiro en nuestra oficina. Ubicación en bodega: *{ubicacion_msg}*. Le esperamos en horario valle (8:00am-10:00am o 3:00pm-4:30pm) para una atención rápida. ¡Gracias por preferirnos!"
        elif tipo_msg == "Información de Horarios Valle y Tarifas":
            mensaje_final = f"¡Hola {cli_nombre}! 🌟 En *Morón Express C.A.* optimizamos nuestro servicio para usted. Le invitamos a utilizar nuestros horarios valle (8:00 a.m. a 10:00 a.m. y 3:00 p.m. a 4:30 p.m.) y a realizar su pre-registro por código QR antes de llegar a taquilla para evitar filas. Consulte tarifas y estatus en nuestra web."
        else:
            mensaje_final = f"¡Hola {cli_nombre}! 📱 Para su próximo envío en *Morón Express C.A.*, recuerde utilizar nuestro sistema de pre-registro digital con código QR para reducir su tiempo de espera en taquilla a menos de 2 minutos. ¡Eficiencia y rapidez!"
            
        st.text_area("Texto listo para enviar:", value=mensaje_final, height=150)
        
        # Enlace directo a WhatsApp Web / API
        whatsapp_url = f"https://wa.me/{cli_telefono}?text={urllib.parse.quote(mensaje_final) if 'urllib' in globals() else mensaje_final}"
        st.markdown(f"""
        <a href="{whatsapp_url}" target="_blank">
            <button style="background-color:#25D366; color:white; padding:10px 20px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;">
                📲 Enviar por WhatsApp Business
            </button>
        </a>
        """, unsafe_allow_html=True)

# ----------------------------------------------------
# 6. PANEL GERENCIAL DE TIEMPOS
# ----------------------------------------------------
elif menu == "📊 Panel Gerencial de Tiempos":
    st.markdown('<div class="main-header">Panel Gerencial y Métricas de Rendimiento</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Monitoreo de tiempos de atención y control de calidad post-optimización</div>', unsafe_allow_html=True)
    
    import numpy as np
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="⏱️ Tiempo Promedio Total", value="5.4 min", delta="-13.3 min vs Inicial (18.7m)")
    with col2:
        st.metric(label="👥 Clientes Atendidos Hoy", value="118", delta="+12% capacidad operativa")
    with col3:
        st.metric(label="⭐ Satisfacción del Usuario (Likert)", value="4.7 / 5.0", delta="+2.3 vs Diagnóstico (2.4)")
        
    st.markdown("---")
    st.subheader("📈 Comparativa de Tiempos por Fase del Proceso (Antes vs. Después)")
    
    chart_data = pd.DataFrame({
        "Fase del Proceso": ["Espera en Fila", "Búsqueda en Bodega", "Procesamiento Taquilla", "Tiempo Total"],
        "Antes de la Propuesta (Min)": [9.35, 5.25, 4.10, 18.70],
        "Después de la Propuesta (Meta)": [2.10, 0.45, 1.45, 4.00]
    })
    
    st.bar_chart(chart_data.set_index("Fase del Proceso"))
    
    st.success("✅ **Conclusión Gerencial:** La implementación combinada del pre-registro QR, la zonificación alfanumérica de bodega y el portal de autoconsulta cumple a cabalidad con la meta de reducir el tiempo total por transacción por debajo de los 6 minutos, elevando la rentabilidad y la fidelización del cliente en la sucursal Morón Express C.A.")
