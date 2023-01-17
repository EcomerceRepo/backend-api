# backend-api
# Reproduction steps:
### 1. Clone the repository and navigate to the project directory
```
git clone https://github.com/EcomerceRepo/backend-api.git
cd backend-api
```
### 2. Create Python3 Virtual Environment
On Windows:
```
python -m venv venv 
venv\Scripts\activate
```
On macOS / Linux:
```
python3 -m venv venv
source venv/bin/activate
```
### 3. Instal the dependencies
```
pip install -r requirements.txt
```
### 4. Run the Django local server and migrations
```
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
```
### 5. Test the API
Try requesting this URL.
```
http://127.0.0.1:8000/product/
```
# Demo
https://www.youtube.com/watch?v=wegg1lghUJE&ab_channel=MaksymMalicki
