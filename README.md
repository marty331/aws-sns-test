# aws-sns-test
AWS SNS Test Demo Project


## Project Setup
- Create virtual environment
- Activate virtual environment
- Install requirements
```python
pip install -r requirements.txt
```
- Set Flask variable
```python
export FLASK_APP=setup.py
```
- Set environment variables:

    Create .env file under awssns/ directory
    
    Add TOPIC_ARN_KEY=<value-from-aws-sns-topic>

## Run Project

From the root of the project run the following command to start the development
server.  This will start the server on localhost:5000
```python
flask run
```

## Routes
Currently there are two routes.

Index route -
The index route is only used to show that the server is up and responding, 
test it by using your browser or curl - localhost:5000

Test SNS route-
The Test SNS route is a POST route that will send a message to your message
topic.  You may use curl, x, or Insomnia.  You should include a JSON body with a 
message parameter such as :
```json
{
  "message": "I'm a little teapot."
}
```
Finally the url is: localhost:5000//test-sns