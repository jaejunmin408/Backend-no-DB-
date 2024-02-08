import pandas as pd

def save(userid):
    idx = len(pd.read_csv("database.csv"))
    print(idx)
    new_df = pd.DataFrame({"userid":userid}, 
                         index = [idx])
    new_df.to_csv("database.csv",mode = "a", header = False)
    return None

def load_list():
    photo_list = []
    df = pd.read_csv("database.csv")
    for i in range(len(df)):
        photo_list.append(df.iloc[i].tolist())
    print(photo_list)
    return photo_list

def now_index():
    df = pd.read_csv("database.csv")
    return len(df)-1


def load_photo(idx):
    df = pd.read_csv("database.csv")
    photo_info = df.iloc[idx]
    return photo_info


if __name__ =="__main__":
    load_list()