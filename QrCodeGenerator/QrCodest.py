import streamlit as st
import qrcode
from io import BytesIO

class MyQr:

    def __init__(self, size: int, padding: int):
        self.size = size
        self.padding = padding

    def createQr(self, userInput, fileName, fg, bg):
        try:
            qr = qrcode.QRCode(box_size=self.size, border=self.padding)
            qr.add_data(userInput)
            qr_image = qr.make_image(fill_color=fg, back_color=bg)
            with BytesIO() as output:
                qr_image.save(output, format="PNG")
                qr_image_bytes = output.getvalue()
            st.success(f'Successfully Created! {fileName}')

            return qr_image_bytes
        except Exception as e:
            st.error(f'Error: {e}')


def main():
    st.title("QR Code Generator")
    st.write("Enter the text to generate QR code")

    userInput = st.text_input("Text:")
    size = st.slider("Size:", min_value=10, max_value=100, value=30, step=1)
    padding = st.slider("Padding:", min_value=0, max_value=10, value=2, step=1)
    fg_color = st.color_picker("Foreground color", "#000000")  # Default is black
    bg_color = st.color_picker("Background color", "#FFFFFF")  # Default is white
    file_name = st.text_input("Enter the file name:") + ".png"

    if st.button("Generate QR Code"):
        myqr = MyQr(size=size, padding=padding)
        qr_image_bytes = myqr.createQr(userInput, fileName=file_name, fg=fg_color, bg=bg_color)
        if qr_image_bytes:
            st.download_button(label="Download QR Code", data=qr_image_bytes, file_name=file_name)


if __name__ == "__main__":
    main()
