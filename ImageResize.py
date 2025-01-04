# Register this blueprint by adding the following line of code 
# to your entry point file.  
# app.register_functions(ImageResize) 
# 
# Please refer to https://aka.ms/azure-functions-python-blueprints

import azure.functions as func
from azure.storage.blob import BlobServiceClient
from PIL import Image
from io import BytesIO
import json
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        connection_string = os.environ["AzureWebJobsStorage"]
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        file = req.files.get("file")
        width = int(req.form.get("width"))
        height = int(req.form.get("height"))

        if not file or not width or not height:
            return func.HttpResponse("Invalid inputs", status_code=400)

        # Process the image
        img = Image.open(file.stream)
        img = img.resize((width, height))
        output = BytesIO()
        img.save(output, format=img.format)
        output.seek(0)

        # Upload to Blob Storage
        container_name = "uploads-resized"
        blob_name = f"resized-{file.filename}"
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        blob_client.upload_blob(output, overwrite=True)

        # Return download URL
        blob_url = blob_client.url
        return func.HttpResponse(json.dumps({"downloadUrl": blob_url}), mimetype="application/json")
    except Exception as e:
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)