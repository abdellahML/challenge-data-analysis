import pandas as pd
import numpy as np


def price_mean(price: str) -> float:
    """

    :param price:
    :return:
    """
    if "-" in price:
        min_max_price = price.split()
        min_price = float(min_max_price[0])
        max_price = float(min_max_price[2])
        return float((max_price+min_price)/2)
    elif "no price" == price:
        return np.NAN

    return float(price)


def bool_converter(boolean: bool) -> int:
    """

    :param boolean:
    :return:
    """
    if boolean is False:
        return 0
    elif boolean is True:
        return 1

    return boolean


def type_converter(property_type: str) -> str:
    """

    :param property_type:
    :return:
    """
    if property_type == "apartment group":
        return "apartment"
    elif property_type == "house group":
        return "house"

    return property_type


def flanders_wallonia_bruxelles(zip_code: int) -> str:
    """

    :param zip_code:
    :return:
    """
    if (4000 <= zip_code < 5000 or 6600 <= zip_code < 7000 or 1300 <= zip_code < 1500
       or 5000 <= zip_code < 5700 or 6000 <= zip_code < 6600 or 7000 <= zip_code < 8000):
        return "Wallonia"

    elif 1500 <= zip_code < 2000 or 2000 <= zip_code < 4000 or 8000 <= zip_code < 10000:
        return "Flanders"

    elif 1000 <= zip_code < 1300:
        return "Bruxelles"

    return np.NAN


def open_and_manage(csv_file: str) -> pd.DataFrame:
    """
    
    :param csv_file:
    :return:
    """
    df = pd.read_csv(csv_file)

    df = df.drop(["Unnamed: 0", "visualisationOption", "transactionType", "short_id"], axis=1)
    df.rename(columns={"indoor": "nbr_parking_indoor", "outdoor": "nbr_parking_outdoor",
                       "mètres carrés": "square_metres", "commune": "city", "zip": "zip_code"}, inplace=True)

    nan_value = float("NaN")
    df["price"].replace("", nan_value, inplace=True)
    df.dropna(subset=["price"], inplace=True)

    df["price"] = df["price"].apply(price_mean)
    df["type"] = df["type"].apply(type_converter)
    df["region"] = df["zip_code"].apply(flanders_wallonia_bruxelles)
    df = df.applymap(bool_converter)

    df["price_by_m2"] = df["price"] / df["square_metres"]

    return df
