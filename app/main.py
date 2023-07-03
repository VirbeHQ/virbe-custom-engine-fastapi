from fastapi import FastAPI

from app.schema import ChatRequest, ChatResponse, ChatResponseBeingAction, RoomConversationResponse, \
    RoomConversationRequest, RoomMessageAction, RoomMessageTextData

app = FastAPI()


@app.get('/api/v1/health')
def health():
    return 'OK'


def your_textual_response():
    # TODO: Add your logic here
    return "Hello World"


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
