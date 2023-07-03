from typing import Optional

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, List, Any


class ChatRequestUserAction(BaseModel):
    text: str


class ChatRequest(BaseModel):
    endUserId: str
    conversationId: str
    userAction: ChatRequestUserAction
    languageCode: str
    context: Optional[Any]


class ChatResponseBeingAction(BaseModel):
    text: Optional[str]
    custom: Optional[Any]


class ChatResponse(BaseModel):
    conversationId: str
    beingActions: List[ChatResponseBeingAction]


class RoomMessageTextData(BaseModel):
    text: str
    language: Optional[str] = Field(alias="language", default=None)

    class Config:
        partial = True


class RoomMessageRoomStore(BaseModel):
    key: str
    value: str


class RoomMessageEndUserStore(BaseModel):
    key: str
    value: str


class RoomMessageNamedAction(BaseModel):
    name: str
    value: Optional[str] = Field(alias="value", default=None)
    value_json: Optional[Any] = Field(alias="valueJson", default=None)

    class Config:
        allow_population_by_field_name = True
        partial = True


class RoomMessageUiAction(BaseModel):
    name: str
    value: Optional[Any] = Field(alias="value", default=None)

    class Config:
        allow_population_by_field_name = True
        partial = True


class RoomMessageAction(BaseModel):
    text: Optional[RoomMessageTextData] = Field(alias="text", default=None)
    room_store: Optional[RoomMessageRoomStore] = Field(alias="roomStore", default=None)
    end_user_store: Optional[RoomMessageEndUserStore] = Field(alias="endUserStore", default=None)
    named_action: Optional[RoomMessageNamedAction] = Field(alias="namedAction", default=None)
    ui_action: Optional[RoomMessageUiAction] = Field(alias="uiAction", default=None)

    class Config:
        allow_population_by_field_name = True
        partial = True


class Room(BaseModel):
    id: str
    location_id: Optional[str] = Field(alias="locationId", default=None)
    client_id: Optional[str] = Field(alias="clientId", default=None)
    origin: Optional[str] = None
    user_agent: Optional[str] = Field(alias="userAgent", default=None)
    referer: Optional[str] = None
    created_at: Optional[datetime] = Field(alias="createdAt", default=None)
    updated_at: Optional[datetime] = Field(alias="updatedAt", default=None)

    class Config:
        allow_population_by_field_name = True
        partial = True


class Location(BaseModel):
    id: str
    name: str
    channel: str


class RoomConversationRequest(BaseModel):
    message_id: str = Field(alias="id")
    room: Room = Field(alias="room")
    location: Optional[Location] = Field(alias="location", default=None)
    end_user_id: str = Field(alias="endUserId")
    action: RoomMessageAction = Field(alias="action")
    instant: datetime = Field(alias="instant")

    class Config:
        allow_population_by_field_name = True


class RoomConversationResponse(BaseModel):
    action: Optional[RoomMessageAction] = None

    class Config:
        allow_population_by_field_name = True
        partial = True
