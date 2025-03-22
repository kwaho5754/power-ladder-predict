import pandas as pd

df = pd.read_csv("power_ladder_data.csv", encoding="utf-8")

# 엑셀처럼 보기 좋게 출력
import ace_tools as tools
tools.display_dataframe_to_user(name="CSV 데이터", dataframe=df)
