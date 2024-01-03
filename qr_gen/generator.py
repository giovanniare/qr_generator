import qrcode
from PIL import Image
from notification import exceptions as NT


class QrGenerator(object):
    def __init__(self) -> None:
        self.qr = None

    def initialize(self, ver=1, error_corr=qrcode.constants.ERROR_CORRECT_H, size=10, border=4) -> None:
        qr = qrcode.QRCode(
            version = ver,
            error_correction = error_corr,
            box_size = size,
            border = border
        )

        self.qr = qr

    def load_data(self, data) -> None:
        self.qr.add_data(data)
        self.qr.make(fit=True)

    def make_image(self, name):
        imagen = self.qr.make_image()
        imagen.save(name)

    def build_single_url_qr(self, url, img_name):
        url_str = url.get()
        name_str = img_name.get()

        if not url_str:
            raise NT.NoUrl
        elif not name_str:
            raise NT.NoName

        self.load_data(url_str)
        self.make_image(name_str)

    def build_url_qr_with_logo(self, logo_path, url, name):
        url_str = url.get()
        name_str = name.get()
        logo_sel = logo_path.get()

        if not url_str:
            raise NT.NoUrl
        elif not name_str:
            raise NT.NoName
        elif not logo_sel:
            raise NT.NoLogo

        self.load_data(url_str)
        logo = Image.open(logo_sel)
        hsize = int((float(logo.size[1])*float(100/float(logo.size[0]))))
        logo = logo.resize((100, hsize), Image.ANTIALIAS)

        imagen = self.qr.make_image()
        pos = ((imagen.size[0] - logo.size[0]) // 2,(imagen.size[1] - logo.size[1]) // 2)
        imagen.paste(logo, pos)
        imagen.save(rf"C:\Users\giova\Documents\QR_GEN\{name_str}")

