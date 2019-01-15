# falcon-python

POST the data to Endpoints

  curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"id":100}' http://127.0.0.1:8000/test
  
  
Run the script

   gunicorn test:app
