import cv2
from detector import read_photo
from fastapi import FastAPI, Response, Query
import uvicorn

app = FastAPI()

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cv2.startWindowThread()


@app.get("/imgs")
def detect_in_photo(url: str = Query(None, min_length=1), q: int = Query(2), size: int = Query(500)):
    (flag, encoded) = cv2.imencode(".png", read_photo(url, hog, size, q))
    return Response(b''+bytearray(encoded), media_type="image/png")


@app.get("/")
def default():
    return "default"


uvicorn.run(app, host='127.0.0.1', port=8000)
