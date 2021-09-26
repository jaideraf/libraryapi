from fastapi import FastAPI
from libraryapi.pergamum import PergamumDownloader
from fastapi.responses import StreamingResponse, Response

app = FastAPI()
pergamumDownloader = PergamumDownloader()

@app.get("/download_pergamum_marciso")
async def download_pergamum_marciso(url: str, id: int) -> StreamingResponse:
    return StreamingResponse(pergamumDownloader.download_iso(url, id), media_type="application/marc")

@app.get("/download_pergamum_marcxml")
async def download_pergamum_marcxml(url: str, id: int) -> Response:
    return Response(pergamumDownloader.download_xml(url, id), media_type="application/xml")