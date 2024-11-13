from fastapi import APIRouter

from api.dtos.support_request import SupportRequestDto
from notifiers.channels.slack.support_requests import send_slack_message
from notifiers.channels.email.support_requests import send_email
from enums.support_requests import Channel
from value_objects.support_request import SupportRequestEmailValueObject

router = APIRouter()

@router.post("/support-requests", tags=["Support Requests"])
async def support_request(dto: SupportRequestDto):
  channel = dto.get_channel()

  if channel == Channel.EMAIL:
    email_params = SupportRequestEmailValueObject(
      topic=dto.topic.value,
      message=dto.description,
      receiver=dto.receiver
    )
    success, message = send_email(email_params)

    if success:
      return { 'response': message }
    else:
      return { 'response': f'Error: {message}' }
    
  if channel == Channel.SLACK:
    send_slack_message()