import pandas as pd
import numpy as np

from urllib.parse import unquote


def price_mean(price: str) -> float:
    """
    Change the string price in integer.
    If there is only a number it changes only the type.
    If there is a min and a max it takes the mean.
    :param price: string with the price of the ad.
    :return: the price or the mean with an integer.
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
    Changes the boolean values in 1 or 0.
    :param boolean: bool.
    :return: 1 if True, 0 if False.
    """
    if boolean is False:
        return 0
    elif boolean is True:
        return 1

    return boolean


def type_converter(property_type: str) -> str:
    """
    change the property_type to have only two values.
    :param property_type: str, property_type in the df.
    :return: apartment or house.
    """
    if property_type == "apartment group":
        return "apartment"
    elif property_type == "house group":
        return "house"

    return property_type


def flanders_wallonia_bruxelles(zip_code: int) -> str:
    """
    based on the zip_code, set the region of the house/apartment.
    :param zip_code: The zip_code of the ad.
    :return: The name of the region.
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
    Take the path to our csv file to open, clean and manage it.
    :param csv_file: str, path to the csv file.
    :return: The pandas DataFrame.
    """
    df = pd.read_csv(csv_file)

    # Rename and drop some columns.
    df = df.drop(["Unnamed: 0", "visualisationOption", "transactionType", "short_id"], axis=1)
    df.rename(columns={"indoor": "nbr_parking_indoor", "outdoor": "nbr_parking_outdoor",
                       "mètres carrés": "square_metres", "commune": "city", "zip": "zip_code"}, inplace=True)

    # Delete rows with Na in prices and duplicated rows.
    nan_value = float("NaN")
    df["price"].replace("", nan_value, inplace=True)
    df.dropna(subset=["price"], inplace=True)
    df.duplicated(subset=None, keep="first")

    # Type some data and create columns from others.
    df["price"] = df["price"].apply(price_mean)
    df["type"] = df["type"].apply(type_converter)
    df["region"] = df["zip_code"].apply(flanders_wallonia_bruxelles)
    df["city"] = df["city"].apply(unquote)
    df = df.applymap(bool_converter)
    df["price_by_m2"] = df["price"] / df["square_metres"]

    # Create one hot encode columns.
    df["region"] = pd.Categorical(df["region"])
    df["type"] = pd.Categorical(df["type"])
    df["subtype"] = pd.Categorical(df["subtype"])
    df["cuisine_type"] = pd.Categorical(df["cuisine_type"])
    df["condition"] = pd.Categorical(df["condition"])
    df["heatingType"] = pd.Categorical(df["heatingType"])
    dfdummies = pd.get_dummies(df["region"], prefix="region")
    dfdummies1 = pd.get_dummies(df["type"], prefix="type")
    dfdummies2 = pd.get_dummies(df["subtype"], prefix="subtype")
    dfdummies3 = pd.get_dummies(df["cuisine_type"], prefix="cuisine")
    dfdummies4 = pd.get_dummies(df["condition"], prefix="condition")
    dfdummies5 = pd.get_dummies(df["heatingType"], prefix="heating")

    df = pd.concat([df, dfdummies, dfdummies5, dfdummies4, dfdummies3, dfdummies2, dfdummies1], axis=1)

    return df
