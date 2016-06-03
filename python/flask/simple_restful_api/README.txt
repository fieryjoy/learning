# TaskListAPI usage
curl -u grati:python -i -H "Content-Type: application/json" -X GET http://localhost:5000/todo/api/v1.0/tasks
curl -u grati:python -i -H "Content-Type: application/json" -X POST -d '{"title": "Check the internet", "description": "Maybe something good"}' http://localhost:5000/todo/api/v1.0/tasks

# TaskAPI usage
curl -u grati:python -i -H "Content-Type: application/json" -X GET http://localhost:5000/todo/api/v1.0/tasks/1
curl -u grati:python -i -H "Content-Type: application/json" -X PUT -d '{"title": "Buy food"}' http://localhost:5000/todo/api/v1.0/tasks/1
curl -u grati:python -i -H "Content-Type: application/json" -X DELETE http://localhost:5000/todo/api/v1.0/tasks/1