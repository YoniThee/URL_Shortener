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