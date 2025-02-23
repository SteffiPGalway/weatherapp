# Weather App


To run the weather app, create a virtual environment:

```
python3 -m venv env
```

Activate the virtual environment:

```
source env/bin/activate
```

Set API KEY for Openweathermap:

```
export API_KEY = ''
```
Or 

```
create an .env file with your API key, install python-dotenv, import load_dotenv from dotenv
```

Run the flask app:

```
flask run
```