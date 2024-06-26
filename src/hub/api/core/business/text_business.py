from hub.api.adapter.http.v1.model.request.text_request import TextRequest
from hub.api.adapter.http.v1.model.response.text_response import *

from hub.api.adapter.service.provider_service import ProviderService


class TextBusiness:

    def __init__(self):
        self.provider_hub = ProviderService()

    def generate(self, text_request_body: TextRequest):
        return self.provider_hub.generate_text(
            provider_name=text_request_body.provider.name,
            text_request_body=text_request_body,
        )
