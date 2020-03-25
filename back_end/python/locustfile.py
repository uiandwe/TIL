# -*- coding: utf-8 -*-
"""
locust 성능 측정


$ locust -f locustfile.py

# https://medium.com/@jspark141515/locust%EB%A1%9C-%EC%84%9C%EB%B2%84-%EC%84%B1%EB%8A%A5-%ED%85%8C%EC%8A%A4%ED%8A%B8%ED%95%98%EA%B8%B0-7490d882015

# https://dejavuqa.tistory.com/131



"""

from locust import HttpLocust, TaskSet, between
from locust.exception import StopLocust

def index(l):
    response = l.client.get("/animal/")
    if response.status_code != 200:
        raise StopLocust()
    return response

# def test(l):
#     l.client.get("/animal/")

class UserBehavior(TaskSet):
    tasks = {index: 1}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(1, 1)
