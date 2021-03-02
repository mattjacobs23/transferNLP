FROM python:3.6

# tensorflow/tensorflow:1.12.0-py3

#ENV LANG=C.UTF-8

# not setting a WORKDIR because should be in gpt2_gen already?
ENV FLASK_APP text_generator
ENV FLASK_ENV development

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
