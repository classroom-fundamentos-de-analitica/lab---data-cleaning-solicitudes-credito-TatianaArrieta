"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():
    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    df[["sexo", "tipo_de_emprendimiento","idea_negocio","barrio","línea_credito"]] = df[["sexo", "tipo_de_emprendimiento","idea_negocio","barrio","línea_credito"]].apply(lambda x: x.astype(str).str.lower())
    df = df.replace(to_replace = "(_)|(-)", value = " ", regex = True)    

    df.comuna_ciudadano = df.comuna_ciudadano.astype(float)
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if (len(re.findall("^\d+/", x)[0]) - 1) == 4 else datetime.strptime(x, "%d/%m/%Y"))

    df.monto_del_credito = df.monto_del_credito.str.replace("\$[\s*]", "")
    df.monto_del_credito = df.monto_del_credito.str.replace(",", "")
    df.monto_del_credito = df.monto_del_credito.str.replace("\.00", "")
    df.monto_del_credito = df.monto_del_credito.astype(int)
    df.dropna(axis = 0, inplace = True)
    df.drop_duplicates(inplace = True)
    return df
