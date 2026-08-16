#! /usr/bin/env python3

import click
import requests
import atexit
import time
from pprint import pprint
from multiprocessing import Pool
from math import ceil
import sched
import datetime
import urllib3

urllib3.disable_warnings()

P_COUNT=4

@click.group()
def cli():
    """Gather Metrics from a Redfish BMC as quickly as possible"""
    pass

def exit_cleanup(session, id, host, insecure, authtoken):
    session.delete(f"https://{host}/redfish/v1/Sessions/{id}", headers={'X-Auth-Token': authtoken}, verify=not insecure)

def fetch_urls(session, host, authtoken, sensor_urls, insecure):
    print(datetime.datetime.now())
    start = time.time()
    print("starting url fetch")
    for url in sensor_urls:
        start_time = time.time()
        res = session.get(f"https://{host}{url}", headers={'X-Auth-Token': authtoken}, verify = not insecure)
        print(f"{url} took {time.time() - start_time}s")
        # pprint(res.json())
    print(f"Total: {time.time()-start}")

def sched_inner(sch: sched.scheduler, session, host, authtoken, sensor_urls, insecure):
    sch.enter(1,1,sched_inner, (sch, session, host, authtoken, sensor_urls, insecure))

    fetch_urls(session, host, authtoken, sensor_urls, insecure)

def main(host, username, password, insecure, sensor_urls):
    with requests.Session() as session:
        resp = session.post(
            f"https://{host}/redfish/v1/Sessions", 
            json={"UserName": username, "Password": password},
            verify=not insecure)
        print(resp)
        authtoken = resp.headers['X-Auth-Token']
        id = (resp.json())['Id']
        print(authtoken)
        atexit.register(exit_cleanup, session, id, host, insecure, authtoken)

        sch = sched.scheduler(time.monotonic, time.sleep)
        sch.enter(1,1,sched_inner, (sch, session, host, authtoken, sensor_urls, insecure))

        sch.run()

        while True:
            time.sleep(1)



@cli.command()
@click.option("--host", type=str, help="IP address or hostname of the BMC to connect to.")
@click.option("--username", help="Username to connect with")
@click.option("--password", help="Password to connect with")
@click.option("--insecure", type=bool, default=False, help="Allow insecure connections")
@click.argument("sensor_urls", nargs=-1)
def run(host, username, password, insecure, sensor_urls):
    """Run the data gathering script"""
    main(host, username, password, insecure, sensor_urls)

if __name__ == "__main__":
    cli()