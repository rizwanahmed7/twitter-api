- The frontend is in the twitter directory whereas the backend API is in twitter_api directory
- Clone the repository
### Setup (Backend API)
- Navigate to the twitter_api directory
- Requires python 3.8+
- Create a python virtual environment with:
```
python3 -m venv venv
```
- Activate the virtual environment with:
```
source venv/bin/activate
```
- Install the requirements with:
```
pip install -r requirements.txt
```
- Run migrations with
```
python manage.py migrate
```
- Start the server with:
```
python manage.py runserver
```

### Setup (Frontend)
- Navigate to the twitter directory
- Requires yarn
- Install npm packages with
```
yarn install
``` 
- Run the sever with
```
yarn serve
```
- Open http://localhost:8080/ on your browser
