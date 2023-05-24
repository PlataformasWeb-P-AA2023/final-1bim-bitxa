from queries import one, two, three, four, five
from schemes import *


def set_running_session(session):
    global running_session
    running_session = session


def run_all_queries():
    queries_runners = [
        five
    ]

    for query in queries_runners:
        query.run_queries(running_session)
