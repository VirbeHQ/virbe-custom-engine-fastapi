# Instalation

TODO 
```
poetry shell
```

Run project
```
uvicorn app.main:app --reload
```

To test with Virbe, launch ngrok in separate terminal process
```
ngrok http 8000
```

For old synchronous architecture
```
https://<your-ngrok-url>/api/v1/chat
```

For new asynchronous architecture (rooms)
```
https://<your-ngrok-url>/api/v1/room
```