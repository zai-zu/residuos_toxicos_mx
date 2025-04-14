from config import df_residuos_tox_grouped_generacion_anio
import pandas as pd

def variacion_porcentual(df):
    """Calcula la variación porcentual de la generación de residuos tóxicos por año en cada entidad."""
    
    df = df.sort_values(by=["ent_fed", "anio"])
    df["variacion_porcentual"] = (
        df.groupby("ent_fed")["generacion_estimada_ton_anio_total"].pct_change() * 100
    )

    #df.to_csv('df_residuos_tox_grouped_generacion_anio_variacion.csv', index=False)
    return df

df_result_variacion_porcentual = variacion_porcentual(df_residuos_tox_grouped_generacion_anio)
print(df_result_variacion_porcentual.head(20))
