FROM python:3.9-slim
RUN pip install --no-cache-dir "fastapi[standard]"
COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
COPY ./app ./app
COPY ./main.py ./main.py
CMD ["fastapi", "run", "main.py", "--port", "8080"]