import os

import chardet
import pandas as pd
import requests


def dicto_leagues():
    return {
        "espana": ["espana", "SP1"],
        "inglaterra": ["inglaterra", "E0"],
        "alemania": ["alemania", "D1"],
    }


def dicto_seasons():
    return {
        "previas": ["previas"],
        "actual": ["actual"],
    }


primer_temporada_90s = 93
ultima_temporada_90s = 99
ultima_temporada_20s_previa = 25
temporada_actual_20s = 26

temporadas_1 = [
    f"{str(i)}{str(i+1)}" for i in range(primer_temporada_90s, ultima_temporada_90s)
]
temporadas_2 = ["9900"]
temporadas_3 = [
    f"{str(i).zfill(2)}{str(i+1).zfill(2)}" for i in range(ultima_temporada_20s_previa)
]
temporadas = temporadas_1 + temporadas_2 + temporadas_3


def parse_mixed_dates(col):
    col = col.astype(str).str.strip()

    def fix_year(x):
        parts = x.split("/")
        if len(parts) == 3:
            d, m, y = parts
            if len(y) == 2:
                y = "20" + y if int(y) < 50 else "19" + y
            return f"{d}/{m}/{y}"
        return x

    col_fixed = col.apply(fix_year)
    fechas = pd.to_datetime(col_fixed, errors="coerce", format="%d/%m/%Y")
    return fechas


def get_seasons_info(pais, liga, current=True):
    ruta_carpeta = f"db/{pais}"
    if current:
        temporadas = [f"{str(temporada_actual_20s-1)}{str(temporada_actual_20s)}"]
    else:
        temporadas = temporadas_1 + temporadas_2 + temporadas_3

    os.makedirs(ruta_carpeta, exist_ok=True)
    for i in temporadas:
        ruta = f"https://www.football-data.co.uk/mmz4281/{i}/{liga}.csv"
        nombre_archivo = os.path.join(ruta_carpeta, f"{i}.csv")
        try:
            data = requests.get(ruta)
            with open(nombre_archivo, "wb") as file:
                file.write(data.content)
        except:
            return f"Error en descarga de informacion en pais: {pais} en temporada: {i}"
    if current:
        return f"Descarga completada para el pais: {pais} en temporada actual"
    else:
        return f"Descarga completada para el pais: {pais} en temporadas previas"


def build_dfs_with_prev_info_seasons(country):
    df_consolidated = pd.DataFrame()
    folder = f"db/{country}"
    temporadas = os.listdir(folder)
    msj = []
    for i in temporadas:
        path = os.path.join(folder, i)
        with open(path, "rb") as f:
            encoding = chardet.detect(f.read())["encoding"]
        try:
            df = pd.read_csv(path, sep=",", encoding=encoding)
            df.dropna(how="all", inplace=True)
            df["SEASON"] = str(i)
            df["Date"] = parse_mixed_dates(df["Date"])
            df_consolidated = pd.concat([df_consolidated, df])
        except Exception as e:
            msj.append(
                f"Error de carga en pais: {country} en la temporada: {i}. Error {e}"
            )
    new_cols = [col for col in df_consolidated.columns if "Unnamed" not in col]
    df_consolidated = df_consolidated[new_cols]
    df_consolidated.dropna(subset=[df_consolidated.columns[0]], inplace=True)
    df_consolidated.sort_values(by=["SEASON", "Date"], inplace=True)
    last_date = df_consolidated["Date"].max().strftime("%d/%m/%Y")
    df_consolidated.to_csv(f"db/{country}_final.csv", index=False)
    msj.append(f"Dataframe consolidado creado para el pais: {country}")
    msj.append(f"Ultima fecha: {last_date}")
    return "\n".join(msj)
