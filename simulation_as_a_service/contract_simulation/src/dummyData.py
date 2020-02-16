import pandas as pd


def dummyPandasDf():

    df = pd.DataFrame(
            {
                'name': ['nate', 'kaitlin'],
                'age': [28, 27]
            }
        )

    return df

def someData(multiplier):

    df = dummyPandasDf()

    df = multiplyAge(df, multiplier)

    returnData = df.to_dict('records')

    return returnData

def multiplyAge(df, multiplier):

    df["multiplied_age"] = df["age"] * float(multiplier)

    return df
