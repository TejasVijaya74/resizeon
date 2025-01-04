# ResizeOn: Image Resizing Web Application Using Azure

ResizeOn is a scalable web application that allows users to upload images, automatically resize them using an Azure Function, and download the resized images. The app leverages Azure Blob Storage for image storage and Azure Functions for the resizing logic.

## Features

- **Image Upload**: Users can upload images through an intuitive web interface.
- **Automatic Resizing**: The uploaded image is resized automatically using a serverless Azure Function.
- **Azure Blob Storage**: Secure and scalable storage of both original and resized images.
- **Download Option**: Users can download the resized images.

---

## How It Works

1. **Upload an Image**: Users upload their images via the web app's interface.
2. **Store in Blob Storage**: The uploaded image is saved in Azure Blob Storage.
3. **Resize with Azure Function**: An Azure Function listens to the upload event, processes the image, and resizes it.
4. **Download the Resized Image**: The resized image is stored back in Blob Storage, from where it can be downloaded.

---

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Azure Function)
- **Cloud Platform**: Microsoft Azure
  - Azure Blob Storage
  - Azure Functions
  - Azure Static Web Apps

---

## Deployment Steps

### Prerequisites

- Azure Subscription
- Azure CLI installed locally
- Python installed (version 3.8+)

### 1. **Set Up Azure Blob Storage**

1. Create a Blob Storage account in the Azure Portal.
2. Create a container (e.g., `images`) for storing uploaded and resized images.
3. Note the connection string for accessing the Blob Storage.

### 2. **Develop the Azure Function**

1. Create a Python Azure Function project:
   ```bash
   func init resizeon --python
   cd resizeon
   func new
   ```
2. Select **HTTP trigger** and name it `function_app`.
3. Add the resizing logic in `function_app.py`.

### 3. **Write the HTML Frontend**

Place your `index.html` file in the root of the project directory. This file serves as the user interface for the web application.

### 4. **Configure and Deploy**

1. **Add `function.json`**:
   Ensure the `function_app` has the following configuration in `function.json`:
   ```json
   {
     "bindings": [
       {
         "authLevel": "function",
         "type": "http",
         "direction": "in",
         "name": "req",
         "methods": ["get", "post"]
       },
       {
         "type": "http",
         "direction": "out",
         "name": "$return"
       }
     ]
   }
   ```
2. **Install Dependencies**:
   List dependencies in `requirements.txt` and install them locally:
   ```bash
   pip install -r requirements.txt
   ```
3. **Deploy to Azure**:
   Use the Azure CLI to deploy the function:
   ```bash
   func azure functionapp publish <your-function-app-name> --python
   ```

### 5. **Connect Blob Storage to Azure Function**

Update your Azure Function to use the Blob Storage connection string for accessing uploaded and resized images.

---

## Usage

1. Navigate to the deployed web app's URL:
   ```
   https://<your-app-name>.azurewebsites.net
   ```
2. Upload an image file.
3. Wait for the image to be resized (processed by the Azure Function).
4. Download the resized image from the provided link.

---

## Project Folder Structure

```
resizeon/
├── function_app.py         # Python function for image resizing
├── index.html              # Frontend HTML file
├── requirements.txt        # Python dependencies
├── host.json               # Azure Function host configuration
├── local.settings.json     # Local settings (not included in deployment)
└── .funcignore             # Files to ignore during deployment
```

---

## Future Enhancements

- **Multi-Image Upload**: Support batch uploads and resizing of multiple images.
- **Custom Resizing Options**: Allow users to specify custom dimensions.
- **Advanced Image Processing**: Add filters, cropping, and rotation features.
- **Progress Indicators**: Show upload and processing progress on the UI.
- **Mobile Optimization**: Enhance UI for mobile responsiveness.

---

## Contributing

We welcome contributions to improve this project. Please follow these steps:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Submit a pull request.

---

## License

See the `LICENSE` file for details.

---

## Contact

For questions, feedback, or suggestions, please contact [Your Name/Email].

--- 

Let me know if you'd like further customizations!
