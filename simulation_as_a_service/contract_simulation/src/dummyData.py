import pandas as pd


def dummyPandasDf():

    df = pd.DataFrame(
            {
                'name': ['nate', 'kaitlin'],
                'age': [28, 27]
            }
        )

    return df

def someData():

    df = dummyPandasDf()

    returnData = df.to_dict('records')

    return returnData
