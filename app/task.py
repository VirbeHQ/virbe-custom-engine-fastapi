import asyncio
import logging

import requests

from app.schema import RoomConversationRequest, RoomMessageIngest, RoomMessageAction, RoomMessageTextData
from app.settings import settings

base_logger = logging.getLogger("virbeapp")


def send_message_to_room(
        room_id: str,
        end_user_id: str,
        reply_to_message_id: str,
        sentence_to_send: str,
) -> None:
    url = f"{settings.virbe_dashbord_api_prefix}/api/v1/rooms/{room_id}/messages/api"

    try:
        room_message_ingest = RoomMessageIngest(
            end_user_id=end_user_id,
            reply_to_message_id=reply_to_message_id,
            action=RoomMessageAction(
                text=RoomMessageTextData(text=sentence_to_send),
            ),
        )
        base_logger.info(f"Sending to url: {url}")
        response = requests.post(
            url=url,
            headers={
                "X-Room-Api-Actions-Access-Key": settings.virbe_room_actions_api_key,
            },
            timeout=5,
            json=room_message_ingest.dict(
                exclude_none=True,
                by_alias=True,
            ),
        )
        if response.ok:
            base_logger.info("Sentence sent!")
        else:
            base_logger.error(
                f"Failed! Code {response.status_code} error: {response.text}",
            )
    except requests.Timeout as timeout_err:
        base_logger.error(f"Request timed out: {timeout_err}")
    except requests.RequestException as request_err:
        base_logger.error(f"RequestException encountered: {request_err}")
    except Exception as err:
        base_logger.error(err)


async def prepare_async_response_on_text(
        room_request: RoomConversationRequest,
) -> None:
    if room_request.action and room_request.action.text:
        # Fake await to simulate async
        await asyncio.sleep(1)

        send_message_to_room(
            room_id=room_request.room.id,
            end_user_id=room_request.end_user_id,
            reply_to_message_id=room_request.message_id,
            sentence_to_send=f"This is what you said to me: \"{room_request.action.text.text}\" and I'm sending it back to you!",
        )
