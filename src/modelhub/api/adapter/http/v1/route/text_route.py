from fastapi import APIRouter

from modelhub.api.adapter.http.v1.model.request.text_request import TextRequest
from modelhub.api.adapter.http.v1.model.response.text_response import TextResponse
from modelhub.api.core.business.text_business import TextBusiness

text_route = APIRouter()


@text_route.post(
    "/text",
    response_model=TextResponse,
    response_model_exclude_none=True,
    status_code=200
)
def text(text_request_body: TextRequest):
    text_business = TextBusiness()
    return text_business.generate(text_request_body)