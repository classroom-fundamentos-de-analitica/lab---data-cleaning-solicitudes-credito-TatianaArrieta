"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    df.comuna_ciudadano = df.comuna_ciudadano.astype(int)
    df.fecha_de_beneficio = pd.to_datetime(df.fecha_de_beneficio, dayfirst=True)
    df.monto_del_credito = df.monto_del_credito.str.replace("[,$]|(\.00$)","")

    df.monto_del_credito = df.monto_del_credito.astype(float)
    df[["sexo", "tipo_de_emprendimiento","idea_negocio","barrio","línea_credito"]] = df[["sexo", "tipo_de_emprendimiento","idea_negocio","barrio","línea_credito"]].apply(lambda x: x.astype(str).str.lower())
    df = df.replace(to_replace = "(_)|(-)", value = " ", regex = True)    

    df.dropna(axis = 0, inplace = True)
    df.drop_duplicates(inplace = True)

    return df
