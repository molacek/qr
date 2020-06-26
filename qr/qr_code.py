import qrcode
import io
from flask import Response
from qr import application


@application.route('/<path:qr_text>', methods=("GET",))
def qr(qr_text):

    qr_image = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr_image.add_data(qr_text)
    qr_image.make(fit=True)
    img = qr_image.make_image(fill_color="black", back_color="white")
    img_output = io.BytesIO()
    img.save(img_output)

    return(
        Response(
            img_output.getvalue(),
            200,
            {
                'content-type': 'image/png'
            }
        )
    )

