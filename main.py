import re
import requests
from datetime import datetime, time

KEY = "" # NEIS API KEY

mealType = input("> ")
mealTypes = {"조식": "1", "중식": "2", "석식": "3"}

def getMeal():
    params = {
        "KEY": KEY,
        "Type": "json",
        "pIndex": 1,
        "pSize": 5,
        "ATPT_OFCDC_SC_CODE": "", # 교육청 행정코드
        "SD_SCHUL_CODE": "", # 학교 행정코드
        "MMEAL_SC_CODE": mealTypes[mealType],
        "MLSV_YMD": str(datetime.now().strftime("%Y%m%d")),
    }

    res = requests.get("https://open.neis.go.kr/hub/mealServiceDietInfo", params=params)

    mealRaw = res.json()["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"]
    mealLines = mealRaw.replace("<br/>", "\n").splitlines()
    cleanedLines = [re.sub(r"\([^)]*\)", "", line).strip() for line in mealLines]
    meal = "\n".join(line for line in cleanedLines if line)

    return meal
