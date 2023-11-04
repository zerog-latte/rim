# from typing import Union
from fastapi import FastAPI
from defs_items import q_items_by_cat, q_all_items, q_categories
from defs_items import q_item_by_id, q_item_search

app = FastAPI()


@app.get('/')
def get_root():
  with open('./version', 'r') as f:
    version = f.read()
  return {'RIM': version}


@app.get('/item/{item_id}')
def get_item_by_id(item_id: str):
  return q_item_by_id(item_id)


@app.get('/item/search/{query}')
def find_item(query: str):
  return q_item_search(query)


@app.get('/items')
def get_items():
  return q_all_items()


@app.get('/items/{cat_id}')
def get_item_by_cat(cat_id: str):
  return q_items_by_cat(cat_id)


@app.get('/categories')
def get_categories():
  return q_categories()

@app.get('/categories/flat')
def get_categories_flat():
  cats = q_categories()
  return [item['_id'] for item in cats]
