import json
from datetime import datetime, time, timedelta
import logging

import click
import requests_cache

from uktrains import *


requests_cache.install_cache()
logging.basicConfig(level=logging.DEBUG)
hour = timedelta(hours=1)
week = timedelta(days=7)

def today_at(h, m):
    return datetime.combine(datetime.now(), time(h, m))


@click.command()
@click.option('--dep', default='CHX', help='Departing station code')
def get_data(dep):

    times = [
        h * hour + today_at(0, 00) + week
        for h in range(5, 27)
    ]
    journies = [
        j
        for dt in times
        for j in search_trains(dep, 'HIB', when=dt)
    ]
    assert journies, journies
    print journies

    data = []
    for journey in journies:
        print(journey.depart_time)
        if journey.changes == 0:
            data.append(journey)
        print 'skip', journey

    json.dump(data, open('train_data_{}.json'.format(dep), 'w'), indent=4)
    return data


if __name__ == '__main__':
    get_data()
