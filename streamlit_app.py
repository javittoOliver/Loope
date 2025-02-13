import streamlit as st
import pandas as pd
from datetime import datetime
import io

def create_excel_download_link(df):
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Relevamiento')
    excel_data = output.getvalue()
    return excel_data

def main():
    st.title("Formulario de Relevamiento Técnico - Implementación Loope")
    
    # Crear diferentes secciones usando st.expander para mejor organización
    with st.expander("1. Información General", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            operacion = st.text_input("Nombre de la operación")
            contacto = st.text_input("Contacto técnico principal")
        with col2:
            fecha = st.date_input("Fecha de relevamiento", datetime.now())

    with st.expander("2. Infraestructura de Base de Datos", expanded=False):
        st.subheader("2.1 Base de Datos Actual")
        motor_db = st.selectbox("Motor de base de datos en uso", 
                              ["SQL Server", "MySQL", "PostgreSQL", "Oracle", "Otro"])
        if motor_db == "Otro":
            motor_db_otro = st.text_input("Especifique el motor de base de datos")
        
        version_db = st.text_input("Versión del motor de base de datos")
        bigquery = st.radio("¿Cuenta con acceso a BigQuery?", ["Sí", "No"])
        volumen_datos = st.text_input("Volumen aproximado de datos a procesar (diario)")

        st.subheader("2.2 Conectividad")
        odbc = st.radio("¿Dispone de conexiones ODBC configuradas?", ["Sí", "No"])
        tipo_acceso = st.multiselect("Tipo de acceso a bases de datos",
                                    ["Directo", "A través de VPN", "Otro"])

    with st.expander("3. Infraestructura Cloud", expanded=False):
        st.subheader("3.1 Google Cloud Platform")
        gcp = st.radio("¿Cuenta con proyecto en GCP?", ["Sí", "No"])
        if gcp == "Sí":
            proyecto_gcp = st.text_input("Nombre del proyecto GCP")
            region_gcp = st.text_input("Región principal")
            presupuesto_gcp = st.radio("¿Cuenta con presupuesto asignado para servicios cloud?", 
                                     ["Sí", "No"])

        st.subheader("3.2 Azure")
        azure = st.radio("¿Cuenta con infraestructura en Azure?", ["Sí", "No"])
        if azure == "Sí":
            detalles_azure = st.text_area("Detalles de la infraestructura actual en Azure")

    with st.expander("4. Requerimientos de Integración", expanded=False):

        st.subheader("4.1 Interfaces de Usuario")
        power_bi = st.radio("¿Cuenta con licencias de Power BI?", ["Sí", "No"])
        interfaz = st.multiselect("Preferencia de interfaz",
                                ["Power BI", "Interfaz web", "Aplicación portable", "Otra"])

    with st.expander("5. Datos y Procesamiento", expanded=False):
        st.subheader("5.1 Tipos de Datos")
        tipos_datos = st.multiselect("Fuentes de datos disponibles",
                                   ["Transcripciones de audio", "Archivos de audio",
                                    "Encuestas de satisfacción", "KPIs operativos", "Otros"])
        
        st.subheader("5.2 Volumen y Frecuencia")
        interacciones = st.number_input("Cantidad de interacciones diarias", min_value=0)
        tamano_audio = st.number_input("Tamaño promedio de archivos de audio (MB)", min_value=0.0)
        frecuencia = st.text_input("Frecuencia de actualización de datos requerida")

    with st.expander("6. Seguridad y Cumplimiento", expanded=False):
        st.subheader("6.1 Requisitos de Seguridad")
        encriptacion = st.radio("¿Requiere encriptación de datos sensibles?", ["Sí", "No"])
        sensibilidad = st.radio("Nivel de sensibilidad de datos", ["Alta", "Media", "Baja"])

        st.subheader("6.2 Cumplimiento Normativo")
        normativas = st.text_input("Normativas específicas a cumplir")
        auditorias = st.radio("¿Requiere auditorías de seguridad?", ["Sí", "No"])

    with st.expander("7. Módulos Requeridos", expanded=False):
        modulos = st.multiselect("Seleccione los módulos de Loope que desea implementar",
                               ["Loope CX", "Loope NPS", "Loope Asistente"])

    with st.expander("8. Recursos Disponibles", expanded=False):
        st.subheader("8.1 Equipo Técnico")
        equipo_desarrollo = st.radio("¿Cuenta con equipo de desarrollo interno?", ["Sí", "No"])
        conocimientos = st.multiselect("Conocimientos técnicos disponibles",
                                     ["Python", "SQL", "APIs", "Otros"])

        st.subheader("8.2 Infraestructura")
        ancho_banda = st.number_input("Ancho de banda disponible (Mbps)", min_value=0)
        almacenamiento = st.number_input("Capacidad de almacenamiento disponible (GB)", min_value=0)

    with st.expander("9. Observaciones Adicionales", expanded=False):
        observaciones = st.text_area("Observaciones")

    with st.expander("10. Aprobaciones", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            resp_tecnico = st.text_input("Responsable Técnico")
            resp_seguridad = st.text_input("Responsable de Seguridad")
            resp_operaciones = st.text_input("Responsable de Operaciones")
        with col2:
            fecha_tec = st.date_input("Fecha Responsable Técnico", datetime.now())
            fecha_seg = st.date_input("Fecha Responsable Seguridad", datetime.now())
            fecha_op = st.date_input("Fecha Responsable Operaciones", datetime.now())

    if st.button("Generar Excel"):
        # Crear un diccionario con todos los datos recopilados
        data = {
            "Campo": [
                "Nombre de la operación", "Contacto técnico principal", "Fecha de relevamiento",
                "Motor de base de datos", "Versión DB", "Acceso BigQuery", "Volumen de datos",
                "Conexiones ODBC", "Tipo de acceso", "Proyecto GCP", "Región GCP",
                "Infraestructura Azure", "Licencias OpenAI", "Integración sistemas externos",
                "Licencias Power BI", "Interfaces preferidas", "Tipos de datos",
                "Interacciones diarias", "Tamaño audio", "Frecuencia actualización",
                "Encriptación datos", "Nivel sensibilidad", "Normativas", "Auditorías",
                "Módulos requeridos", "Equipo desarrollo", "Conocimientos técnicos",
                "Ancho de banda", "Almacenamiento", "Observaciones",
                "Responsable Técnico", "Responsable Seguridad", "Responsable Operaciones"
            ],
            "Valor": [
                operacion, contacto, fecha.strftime("%Y-%m-%d"),
                motor_db, version_db, bigquery, volumen_datos,
                odbc, ", ".join(tipo_acceso), proyecto_gcp if gcp == "Sí" else "N/A", 
                region_gcp if gcp == "Sí" else "N/A",
                detalles_azure if azure == "Sí" else "N/A", openai, integracion,
                power_bi, ", ".join(interfaz), ", ".join(tipos_datos),
                interacciones, tamano_audio, frecuencia,
                encriptacion, sensibilidad, normativas, auditorias,
                ", ".join(modulos), equipo_desarrollo, ", ".join(conocimientos),
                ancho_banda, almacenamiento, observaciones,
                resp_tecnico, resp_seguridad, resp_operaciones
            ]
        }
        
        df = pd.DataFrame(data)
        excel_data = create_excel_download_link(df)
        
        st.download_button(
            label="Descargar Excel",
            data=excel_data,
            file_name=f"relevamiento_tecnico_{datetime.now().strftime('%Y%m%d')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

if __name__ == "__main__":
    main()
