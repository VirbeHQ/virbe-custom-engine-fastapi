from fastapi import FastAPI
from starlette.background import BackgroundTasks

from app.task import prepare_async_response_on_text
from app.schema import ChatRequest, ChatResponse, ChatResponseBeingAction, RoomConversationResponse, \
    RoomConversationRequest, RoomMessageAction, RoomMessageTextData

app = FastAPI()


@app.get('/api/v1/health')
def health():
    return 'OK'


def your_textual_response():
    # TODO: Add your logic here
    return "This is your virtual being speaking!"


@app.post("/api/v1/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return ChatResponse(
        conversationId=request.conversationId,
        beingActions=[ChatResponseBeingAction(text=your_textual_response())]
    )


@app.post("/api/v1/room", response_model=RoomConversationResponse)
def room(request: RoomConversationRequest):
    return RoomConversationResponse(
        action=RoomMessageAction(text=RoomMessageTextData(text=your_textual_response()))
    )


@app.post("/api/v1/room/async", response_model=RoomConversationResponse)
def room(request: RoomConversationRequest,
         background_tasks: BackgroundTasks):

    if request.action and request.action.text:
        background_tasks.add_task(
            prepare_async_response_on_text,
            request,
        )

    return RoomConversationResponse(
        action=RoomMessageAction(text=RoomMessageTextData(text="Let me think for a moment..."))
    )
