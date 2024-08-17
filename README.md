# prometheus_test_project
Simple starter for test prometheus + grafana. Every 30 second 'request_script.py' will make a random request.

usage:

1) docker-compose/docker compose up --build -d
2) http://localhost:5000 - flask app include routes:
+ /main - return page with 200 status code
+ /2x-code - return page with 200 status code
+ /4x-code - return page with 404 status code
+ /5x-code - return page with 500 status code
3) http://localhost:3000 - grafana page (username: admin, password: admin - for login)
4) http://localhost:9090 - prometheus page