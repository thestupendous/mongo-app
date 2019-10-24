
FROM python
RUN pip3 install flask pymongo

CMD ["python","/todolist/app.py"]


EXPOSE 9000

COPY . /todolist/
