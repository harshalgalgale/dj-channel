FROM python:3

# Set environment variables
ENV PYTHONUNBUFFERED=1

# RUN mkdir /code
# WORKDIR /code
# COPY requirements.txt /code/

COPY requirements.txt /


# Install dependencies.
RUN pip install -r requirements.txt

# Set work directory.
RUN mkdir /code
WORKDIR /code

# Copy project code.
COPY . /code/

EXPOSE 8080

CMD ["uwsgi", "--http", ":8080", "--ini", "./uwsgi/uwsgi.ini"]
