from typing import Union
from defs_general import load_config, flatten, db


def q_items_by_cat(category: str):
  cf = load_config()
  mc = db(cf)
  return [item for item in mc['items'].get_collection(category).find()]


def q_all_items():
  cf = load_config()
  mc = db(cf)
  cats = mc['items'].list_collection_names()
  ret = []
  for cat in cats:
    ret += [item for item in mc['items'].get_collection(cat).find()]
  return ret


def q_categories():
  cf = load_config()
  mc = db(cf)
  return [cat for cat in mc['models'].get_collection('items_categories').find()]


def q_item_by_id(item_id: str):
  cf = load_config()
  mc = db(cf)
  ret = []
  cats = mc['items'].list_collection_names()
  for cat in cats:
    ci = mc['items'].get_collection(cat).find({'_id': item_id})
    for item in ci:
      ret.append(item)
  return ret


def q_item_search(query: str):
  cf = load_config()
  mc = db(cf)
  ret = []
  cats = mc['items'].list_collection_names()
  for cat in cats:
    ci = mc['items'].get_collection(cat).find({'_id': {'$regex': f"^{query}$"}})
    for item in ci:
      ret.append(item)
  return ret
