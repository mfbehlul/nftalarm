import requests
import pandas as pd
from typing import Dict, List
import os
from pathlib import Path
import ast
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)


collection_information_dict: Dict = {}


def get_collection_information(url):
    """
    This function has been created to collect collections names and
    corresponding urls from howrare.io
    """
    global collection_information_dict
    URL = "https://howrare.is/api/v0.1/collections"
    response = requests.get(url=URL).json()
    result = response["result"]
    data = result["data"]
    for i in data:
        collection_information_dict[i["name"]] = i["url"]


def get_collection_names() -> List:
    """
    This function has been created to read collection names from the database.

    Returns:
        List: List of collection names.
    """
    data = pd.read_csv(Path(parentdir) / "data/collections_and_attributes.csv")
    return list(data["collection_name"])


def get_collections_attributes(collection_name: str) -> Dict:
    """
    This function has been created to send attributes names and their values
    for the given collection name

    Args:
        collection_name (str): Name of the collection. i.e: SolanaMonkeyBusiness (SMB)

    Returns:
        Dict: attribute names and their values.
              e.g : {'Attribute count': [0, 1, 2, 3, 4, 5], 'Type': ['Alien', 'Purple', ...], 'Clothes': ['Green Smoking', 'Orange Shirt',...]}
    """
    data = pd.read_csv(Path(parentdir) / "data/collections_and_attributes.csv")
    for i, row in data.iterrows():
        if row["collection_name"] == collection_name:
            return ast.literal_eval(row["attributes"])


def get_matched_nfts_with_selected_choices(collection_name: str, attributes: Dict):
    """
    This fucntion has been created to find nfts whose attributes match with the given attributes for the given collection.

    Args:
        collection_name (str): Name of the collection. i.e: SolanaMonkeyBusiness (SMB)
        attributes (Dict): attribute names and desired values.
                           e.g : {'Attribute count':"2", 'Type':'Alien' ,'Clothes':'Green Smoking',...]}
    """
    data = pd.read_csv(Path(parentdir) / f"data/{collection_name}.csv")
    for key, value in attributes.items():
        if value == "":
            continue
        data = data[data[key].astype(str) == value]
    return data



