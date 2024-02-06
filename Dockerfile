FROM python:3.9-alpine

WORKDIR /workoutcomp_api

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod +x /workoutcomp_api/script.sh

EXPOSE 8000

CMD ["./script.sh"]