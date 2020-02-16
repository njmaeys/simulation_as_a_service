import pandas as pd


def dummyPandasDf():

    df = pd.DataFrame(
            {
                'ServiceType': ['Ground', 'Express', 'Ground'],
                'ServiceGuideRate': [25, 32, 26],
                'NetAmount': [20, 30, 21],
            }
        )

    return df

def someData(ground, express, international):

    df = dummyPandasDf()

    df["ProposedNetAmount"] = df.apply(lambda row: propNet(row, ground, express, international), axis=1)

    df = savings(df)

    returnData = df.to_dict('records')

    return returnData

def propNet(row, ground, express, international):

    if "ground" in row["ServiceType"].lower():
        returnVal = row["ServiceGuideRate"] * (1 - ground)
    elif "express" in row["ServiceType"].lower():
        returnVal = row["ServiceGuideRate"] * (1 - express)
    elif "international" in row["ServiceType"].lower():
        returnVal = row["ServiceGuideRate"] * (1 - international)
    else:
        returnVal = row["ServiceGuideRate"]

    returnVal = round(returnVal, 2)

    return returnVal

def savings(df):

    df["Savings"] = round(df["NetAmount"] - df["ProposedNetAmount"], 2)

    return df
