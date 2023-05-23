#!/usr/bin/python3
"""
extend Python script to export data in the CSV format.
"""

import csv
import json
import sys
import urllib.request

if __name__ == "__main__":
    employee_ID = sys.argv[1]

    employee_data = urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/users/{}/".format(
            employee_ID))
    employee_tasks = urllib.request.urlopen(
        "https://jsonplaceholder.typicode.com/users/{}/todos/".format(
            employee_ID))

    employee_data_dict = json.loads(employee_data.read().decode())
    employee_task_data_dict = json.loads(employee_tasks.read().decode())

    task_done_count = 0  # counter for tasks done
    total_tasks = 0  # counter for all tasks
    completed_tasks = []  # list to contain completed tasks
    for i in employee_task_data_dict:
        if i["completed"] is True:
            completed_tasks.append(i)
            task_done_count += 1
        total_tasks += 1

    EMPLOYEE_NAME = employee_data_dict["name"]
    USER_ID = employee_data_dict["id"]

    """
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME,
        task_done_count,
        total_tasks))

    for i in completed_tasks:
        print("\t {}".format(i["title"]))
    """

    # Export data in CSV format
    filename = "{}.csv".format(USER_ID)
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID",
                         "USERNAME",
                         "TASK_COMPLETED_STATUS",
                         "TASK_TITLE"])
        for task in employee_task_data_dict:
            task_status = True if task["completed"] else False
            writer.writerow([USER_ID,
                             EMPLOYEE_NAME,
                             task_status,
                             task["title"]])

    # print("Data exported to {}".format(filename))
