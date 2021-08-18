FROM python:3.9.6-slim-buster
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ./animal_scraping .
CMD [ "python3", "-m" , "flask", "run"]
EXPOSE 5000
