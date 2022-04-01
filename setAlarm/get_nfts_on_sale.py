import pandas as pd
import requests
import os
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Tuple
from pathlib import Path
import time

currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)

COLLECTIONS = [
    "Blockasset Legends",
    "Aurory",
    "Solana Monkey Business",
    "DeGods",
    "Stoned Ape Crew",
    "Degenerate Ape Academy",
]


def make_request_for_collection_stats(collection_name: str) -> Tuple:
    """This function has been created to get collection stats from magiceden.io

    Args:
        collection_name (str): Collection name, symbol that magiceden use.

    Returns:
        Tuple: collection_name(symbol) and the number of the nfts that are on sale for that collection in a tuple.
    """
    collection_name = collection_name.lower()
    collection_name = collection_name.split(" -")[0]
    collection_name = collection_name.replace(" ", "_")
    URL = f"https://api-mainnet.magiceden.dev/v2/collections/{collection_name}/stats"
    response = requests.get(url=URL).json()
    return (response["symbol"], response["listedCount"])


def make_requests_to_get_nfts_on_sale_from_collection(arguments: List) -> Dict:
    """This function has been created to get informations of the nfts that are on sale for a spesific collection.

    Args:
        arguments (List): First element of the arguments is the collection name, and the second element is ofset number.

    Returns:
        Dict: Informations of nfts that are on sale. mint,price etc.
    """
    collection_name = arguments[0]
    ofset = arguments[1]
    URL = f"https://api-mainnet.magiceden.dev/v2/collections/{collection_name}/listings?offset={ofset}&limit=20"
    response = requests.get(url=URL).json()
    updated_response = []
    for i in response:
        i["collection_name"] = collection_name
        updated_response.append(i)
    return response


def update_nfts_on_sale_table(collection_names: List):
    """This function is created to update the for sale table
    by pulling the informations of the NFTs for sale from magic eden, for each given collection.

    Args:
        collection_names (List): A list that contains collection names.
    """
    # First we get each collection stats, because we need to know total number of listed nfts(nfts for sale) for each collection.
    # We need that information to decide how many request we have to make to get information of all nfts for sale for a collection.
    if len(collection_names) > 1:
        # Here we creat a multithread, because we dont want to make requests in an order. Speed!!!
        with ThreadPoolExecutor() as executor:
            for collection_name in collection_names:
                collections_and_listed_counts = executor.map(
                    make_request_for_collection_stats, collection_names
                )
    else:
        # If we have single collection, then we don't have to worry about multi threading.
        collections_and_listed_counts = [
            make_request_for_collection_stats(collection_names[0])
        ]
    # According to the listed count of each collection,
    # a list of arguments containing the collection name and offset numbers will be created.
    # i.e [["degods",0],["degods",20],["aurory",0],["aurory",20],["aurory",40]]. We need this arguments list to
    # creaat another multithreading.
    arg_list = []
    for i in collections_and_listed_counts:
        collection_name = i[0]
        listed_count = i[1]
        if listed_count == 0:
            continue
        else:
            if listed_count % 20 == 0:
                n_iter = int(listed_count / 20)
            else:
                n_iter = int(listed_count / 20) + 1
            ofset = 0
            for _ in range(n_iter):
                arg_list.append([collection_name, ofset])
                ofset += 20
    with ThreadPoolExecutor() as executor:
        list_of_nfts_on_sale = executor.map(
            make_requests_to_get_nfts_on_sale_from_collection, arg_list
        )
    responses = []
    for i in list_of_nfts_on_sale:
        responses += i
    df = pd.DataFrame(responses)
    df[["tokenMint", "collection_name", "price"]].to_csv(
        Path(parentdir) / "data/nfts_for_sale.csv"
    )


if __name__ == "__main__":
    st = time.time()
    update_nfts_on_sale_table(COLLECTIONS)
    et = time.time()
    print(f"nfts for sale table updated in {et-st} seconds")
