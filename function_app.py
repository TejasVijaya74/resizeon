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

@app.route(route="function_app", auth_level=func.AuthLevel.FUNCTION)
def function_app(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )