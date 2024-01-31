import qrcode


class MyQr:

  def __init__(self, size: int, padding: int):
    self.qr = qrcode.QRCode(box_size=size, border=padding)

  def createQr(self, fileName, fg, bg):
    userInput = input('Enter the text: ')

    try:
      self.qr.add_data(userInput)
      qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
      qr_image.save(fileName)

      print(f'Successfully Created! {fileName}')
    except Exception as e:
      print(f'Error: {e}')


def main():
  myqr = MyQr(size=30, padding=2)
  fl = input('Enter the file name: ') + '.png'
  myqr.createQr(fileName=fl, fg='black', bg='white')


main()
