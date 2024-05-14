
remove:
	docker rmi just_some_tools:latest

build_local:
	docker build -f Dockerfile -t just_some_tools:latest .

run_api:
	docker run --env-file .env --rm --name just_some_tools_container \
	-v ./src:/app/src -v ./modules:/app/modules -v ./api:/app/api -v ./just_some_tools_cache:/app/just_some_tools_cache \
	-p 8086:8086 -it just_some_tools:latest uvicorn api.main:app --host 0.0.0.0 --port 8086 --reload