### Designing RESTful API with Python-Flask and MongoDB

This  project  how to design RESTful API with Python-Flask and MongoDB.

First you'll need to get the source of the project. You could do this by cloning the repository:

```bash
# Get the project code
git clone <URL_Repository>
```

*NOTE: While working with Python, we would recommend to use virtual environment
to keep all the project's dependencies isolated from other projects.*

##### Create your local environment

If you use local conda IDE.

```bash
conda create -n restfulapi python=2.7 anaconda # Create the environment
source activate restfulapi # Activate the environment
```

##### Install dependencies

```python
pip install -r requirements.txt
```

##### Start MongoDB Server

If you're using MacOS, you could use `brew` to start the server.

```bash
brew services start mongodb
```
Or use a Docker-compose.yml

```bash
docker-compose -f Docker-compose-mongo.yml up -d
```

#### Config the application

Change the `DBNAME` in the config file according to the database name you are using.

##### Start the application

```bash
python run-app.py
```

Once the application is started, go to [localhost](http://localhost:5000/)
on Postman and explore the APIs.

For work with MongoDB you can use [Robo 3T](https://robomongo.org/download)

##### Build the docker api container

    docker build --no-cache --tag afarcloud/api:1.0 .

To be runing the container:

    docker run --name=afarcloud-api -it --rm -p 5000:5000 afarcloud/api:1.0

#### Testing the API-Demo

How to insert a new record in database:
```bash
curl -iX POST "0.0.0.0:5000/api/v1/data" \
  --header "Content-Type: application/json" \
  --data '{
    "id": 1,
    "name": "Afarcloud",
    "email": "afarcloud@afarcloud.com",
    "phone": "+34562412589",
    "localization": "spain"
    }'

```
How to insert more that one record in database:

```bash
curl -iX POST "0.0.0.0:5000/api/v1/data" \
  --header "Content-Type: application/json" \
  --data '[{
    "id": 2,
    "name": "Afarcloud",
    "email": "afarcloud@afarcloud.com",
    "phone": "+34562412589",
    "localization": "spain"
    },
    {
    "id": 3,
    "name": "Afarcloud",
    "email": "afarcloud@afarcloud.com",
    "phone": "+34562412589",
    "localization": "spain"
    }]'

```

How to change data  record in database:
```bash
curl -iX POST "0.0.0.0:5000/api/v1/data/1" \
  --header "Content-Type: application/json" \
  --data '{
    "$set": {
       "localization": "london"
      }
    }'

```

How to list a sensor data:
```bash
curl -H "Accept: application/json" -iX GET 'http://0.0.0.0:5000/api/v1/data?id=2'

curl -H "Accept: application/json" -iX GET 'http://0.0.0.0:5000/api/v1/data?localization=spain'

```

How to delete a entry
```bash
 curl -iX DELETE "http://0.0.0.0:5000/api/v1/data/2"
```