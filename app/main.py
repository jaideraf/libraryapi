from fastapi import FastAPI
from fastapi.responses import Response
from fastapi.responses import StreamingResponse

import app.error as error
import app.util as util
from libraryapi.pergamum import PergamumDownloader


app = FastAPI()
pergamumDownloader = PergamumDownloader()
error.configure(app)


@app.get("/pergamum/mrc")
async def get_marc_iso(url: str, id: int) -> StreamingResponse:
    response = StreamingResponse(
        pergamumDownloader.get_marc_iso(url, id), media_type="application/marc"
    )
    util.attach_file(response, id, "mrc")
    return response


@app.get("/pergamum/xml")
async def get_marc_xml(url: str, id: int) -> Response:
    response = Response(
        pergamumDownloader.get_marc_xml(url, id),
        media_type="application/xml; charset=utf-8",
    )
    return response


@app.get("/pergamum/mrk")
async def get_marc_mrk(url: str, id: int) -> Response:
    response = Response(
        str(pergamumDownloader.build_record(url, id)),
        media_type="text/plain; charset=utf-8",
    )
    util.attach_file(response, id, "mrk")
    return response
