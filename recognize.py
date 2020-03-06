import base64
import json

import requests

from YamlHandler import YamlHandler


class ImgToLatex:

    def __init__(self):
        self.default_headers = None
        # default_headers = {
        #     'app_id': YamlHandler("myConfig.yaml").get_data("appId"),
        #     'app_key': YamlHandler("myConfig.yaml").get_data("appKey"),
        #     'Content-type': 'application/json'
        # }

        self. service = 'https://api.mathpix.com/v3/latex'

    def do_recognize(self, img):  # 识别剪贴板公式
        # im.save('equa.png', 'PNG')
        r = self.latex({
            'src': self.image_uri(img),
            "ocr": ["math", "text"],
            "skip_recrop": True,
            "formats": [
                "latex_simplified",
                "latex_styled",
                "asciimath",
            ],
            "format_options": {
                "latex_simplified": {"transforms": ["rm_spaces"]},
                "latex_styled": {"transforms": ["rm_spaces"]}
            }
        })
        print(r['latex_simplified'])
        print(r['latex_styled'])
        print(r['asciimath'])
        print(r)

        return r

    def latex(self, param, timeout=30):
        headers = {
            'app_id': YamlHandler("myConfig.yaml").get_data("appId"),
            'app_key': YamlHandler("myConfig.yaml").get_data("appKey"),
            'Content-type': 'application/json'
        }
        r = requests.post(self.service,
                          data=json.dumps(param), headers=headers, timeout=timeout)
        return json.loads(r.text)

    def image_uri(self, filename):
        with open(filename, "rb") as f:
            image_data = f.read()
        f.close()
        return "data:image/jpg;base64," + base64.b64encode(image_data).decode()
