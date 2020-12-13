"""
preprocessing data from Game of Thrones
"""

import pandas as pd
import functools

gameofthrones_edge_datas = [pd.read_csv("../data/gameofthrones/data/got-s" + str(i) + "-edges.csv") for i in range(1, 9)]

gameofthrones_edge_datas = [frame.drop(columns=['Season']) for frame in gameofthrones_edge_datas]

for i, frame in enumerate(gameofthrones_edge_datas):
    frame.to_csv("../data/gameofthrones/data_processed/s" + str(i + 1) + "-edges.csv", index=False)

def merge2frame(frame1, frame2) -> pd.DataFrame:
    """
    merge two forms
    """
    res = pd.merge(frame1, frame2, how="outer", left_on=["Source", "Target"], right_on=["Source", "Target"])
    res.fillna(0, inplace=True)
    res["Weight_x"] += res["Weight_y"]
    res.drop(columns=["Weight_y"], inplace=True)
    res.rename(columns={"Weight_x": "Weight"}, inplace=True)
    return res

frame_all = functools.reduce(merge2frame, gameofthrones_edge_datas)

frame_all.to_csv("../data/gameofthrones/data_processed/all_edges.csv", index=False)