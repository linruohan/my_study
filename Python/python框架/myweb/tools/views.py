from django.http import HttpResponse
import qrcode
from django.utils.six import BytesIO

#生成包含data的二维码
def generate_qrcode(request, data):
    img = qrcode.make(data)

    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()

    response = HttpResponse(image_stream, content_type="image/png")
    return response
