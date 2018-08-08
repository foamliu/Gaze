from pymongo import MongoClient
import string,random

client = MongoClient('localhost', 27017)
db = client.gazedb
packages = db.packages
deploys = db.deploys


def insert_package(user_name, package_name, description):
    info = {
        "user_name": user_name,
        "package_name": package_name,
        "description": description
    }
    packages.insert_one(info)


def query_packages():
    return packages.find()


def delete_package(package_name):
    packages.remove({"package_name": package_name})


def insert_deploy(user_name, package_name):
    info = {
        "user_name": user_name,
        "deploy_name": generate_random_string(8),
        "package_name": package_name,
        "status": "creating"
    }
    deploys.insert_one(info)


def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))
