import requests
import csv
import json
import os
from dotenv import load_dotenv

load_dotenv()

def FindUser(data: str):
    result = requests.get(f"http://{os.getenv('DOMAIN')}/api/find_user?{data}")
    return result

def FilterGroupFind(data: str):
    result = requests.get(f"http://{os.getenv('DOMAIN')}/api/filter/group?{data}")
    return result

def FilterCourseFind(data: str):
    result = requests.get(f"http://{os.getenv('DOMAIN')}/api/filter/course?{data}")
    return result

def FilterDirectionFind(data: str):
    result = requests.get(f"http://{os.getenv('DOMAIN')}/api/filter/direction?{data}")
    return result

def CheckAdmin(data: str):
    result = requests.get(f"http://{os.getenv('DOMAIN')}/api/check_admin?{data}")
    return result

def AddUser(data: list):
    params = {
    "fio": data[0],
    "course": data[1],
    "group": data[2],
    "direction": data[3],
    }

    result = requests.get(f"http://{os.getenv('DOMAIN')}/api/add_user", params=params)
    return result

def AddAdmin(data: str):
    result = requests.get(f"http://{os.getenv('DOMAIN')}/api/add_admin?{data}")
    return result

def EditUser(data: list):
    params = {
        "id": data[0],
        str(data[1]): data[2],
    }
    result = requests.get(f"http://{os.getenv('DOMAIN')}/api/edit_user", params=params)
    return result

def DeleteUser(data: str):
    result = requests.get(f"http://{os.getenv('DOMAIN')}/api/detele{data}")
    return result

def ExportData(file_path: str):
    _, ext = os.path.splitext(file_path)

    if ext.lower() == ".csv":
        data = parse_csv(file_path)
    elif ext.lower() == ".json":
        data = parse_json(file_path)

    return send_data_to_api(data)

def parse_csv(file_path):
    with open(file_path, mode="r", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def parse_json(file_path):
    with open(file_path, mode="r", encoding="utf-8") as file:
        return json.load(file)

def send_data_to_api(data):
    url = f"http://{os.getenv('DOMAIN')}/api/add_user"
    return [requests.get(url, params=row).status_code for row in data]