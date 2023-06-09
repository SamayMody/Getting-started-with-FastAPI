# Simple FastAPI code to upload any type of file's

from fastapi import FastAPI , File , UploadFile

app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

