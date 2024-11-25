# URL_Shortener

##Overview
This Python-based URL shortener application leverages FastAPI 
to provide a RESTful API for creating and redirecting short URLs.

###1. Getting Started:
Clone the Repository:
```
git clone https://github.com/your-username/your-repo-name.git
```

### 2. Install Dependencies:
```
pip install -r requirements.txt
```

### 3. Run the Application:
```
uvicorn main:app --reload

```
if tou want to run the app on Docker container and not as server in local-app
1. make sure you have desktop app in your computer
2. run this commands
    ```
   docker build -t my-url-shortener .
   docker run -it -p 8000:8000 my-url-shortener
   ```
   where you can replace <my-url-shortener> in your name for this image

## API Endpoints:
###1. Shorten URL:

Method: POST
URL: /api/shorten
* Request Body:
    ```
    JSON    
    {
        "url": "https://www.example.com/long-url"
    }
    ```
* Response:
    ```
    JSON
    {
    "short_url": "http://localhost:8000/abc123",
    "short_code": "abc123"
    } 
  ```
  
###2. Redirect to Original URL:

Method: GET
URL: /short_code (e.g., /abc123)
Response: Redirects to the original URL.


For check the app you can open in your use this url http://127.0.0.1:8000/docs
you will got kind of swagger and you can check the functionality of the app

Another way to use this app is to install the UI from this link https://github.com/YoniThee/ShortURL_UI.git
 and run the UI app after running this one