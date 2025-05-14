from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, HttpUrl
import uvicorn

app = FastAPI()

# Store the current redirect URL in memory
redirect_url = "https://www.youtube.com/watch?v=V9PVRfjEBTI&list=RDV9PVRfjEBTI"

class URLRequest(BaseModel):
    url: HttpUrl

@app.get("/", response_class=RedirectResponse)
def redirect_to_target():
    return RedirectResponse(url=redirect_url)

@app.post("/set-url")
def set_redirect_url(request: URLRequest):
    global redirect_url
    redirect_url = request.url
    return {"message": "Redirect URL updated", "new_url": redirect_url}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
