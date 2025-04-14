# Bulk fire with streamlit

import streamlit as st
from PIL import Image
from io import BytesIO

def main():
    st.title("📁 File Renamer & Converter App")

    # Optional user name
    name = st.text_input("Enter your name (optional):")
    if name:
        st.success(f"Welcome, {name}!  What's Up Buddy 👋")

    st.markdown("### 📤 Upload a File")
    uploaded_file = st.file_uploader(
        "Upload an image file",
        type=["jpg", "jpeg", "png", "webp", "bmp", "tiff", "ico", "pdf"]
    )

    if uploaded_file is not None:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image Preview", use_container_width=True)
        except Exception as e:
            st.error(f"⚠️ Could not preview file: {e}")
            return

        new_name = st.text_input("Enter new file name (without extension):", max_chars=50)
        extension = st.selectbox(
            "Choose file format:",
            ["jpg", "jpeg", "png", "webp", "bmp", "tiff", "ico", "pdf"]
        )

        if new_name:
            full_new_name = f"{new_name}.{extension.lower()}"

            # Convert RGBA to RGB if needed
            if extension.lower() in ["jpg", "jpeg", "bmp", "pdf", "ico", "tiff"] and image.mode == "RGBA":
                image = image.convert("RGB")

            format_map = {
                "jpg": "JPEG",
                "jpeg": "JPEG",
                "png": "PNG",
                "webp": "WEBP",
                "bmp": "BMP",
                "tiff": "TIFF",
                "ico": "ICO",
                "pdf": "PDF"
            }

            try:
                img_bytes = BytesIO()
                image.save(img_bytes, format=format_map[extension.lower()])
                img_bytes.seek(0)

                st.success(f"✅ File renamed to: {full_new_name}")

                st.download_button(
                    label="📥 Download Renamed File",
                    data=img_bytes,
                    file_name=full_new_name,
                    mime=f"image/{extension}" if extension != "pdf" else "application/pdf"
                )
            except Exception as e:
                st.error(f"❌ Error saving file: {e}")

if __name__ == "__main__":
    main()
