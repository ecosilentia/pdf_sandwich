import streamlit as st
from pypdf import PdfReader, PdfWriter

st.title("🔗 Unir Archivos PDF")

archivos_pdf = st.file_uploader(
    "Carga tus archivos PDF", 
    type="pdf", 
    accept_multiple_files=True
)

if archivos_pdf:
    writer = PdfWriter()
    
    for archivo in archivos_pdf:
        reader = PdfReader(archivo)
        for page in reader.pages:
            writer.add_page(page)
        st.write(f"📄 Añadido: {archivo.name}")

    st.success("✅ Archivos listos para unir")

    if st.button("🔽 Descargar PDF Unificado"):
        with open("PDF_unido.pdf", "wb") as f:
            writer.write(f)
        with open("PDF_unido.pdf", "rb") as f:
            st.download_button(
                label="📥 Descargar PDF Unido",
                data=f,
                file_name="PDF_unido.pdf",
                mime="application/pdf"
            )
