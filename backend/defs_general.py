import os
from dotenv import load_dotenv
from pymongo import MongoClient


def load_config():
  load_dotenv()
  # This gets all env variables starting with RIM_
  cf = {}
  for e in os.environ:
    if e.startswith('RIM_'):
      e_name = e.replace('RIM_', '').lower()
      cf[e_name] = os.getenv(e)
  # This tries to convert port numbers to int
  cf = {k: (int(v) if v.isnumeric() else v) for k, v in cf.items()}
  return cf


def flatten(ls):
  return [item for sublist in ls for item in sublist]


def db(config):
  mc = MongoClient(
    host=config['mongo_host'],
    port=config['mongo_port'],
    username=config['mongo_user'],
    password=config['mongo_pass'],
  )
  return mc
