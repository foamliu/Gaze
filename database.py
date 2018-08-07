from pymongo import MongoClient
import pprint

client = MongoClient('localhost', 27017)
db = client.gazedb
packages = db.packages


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

