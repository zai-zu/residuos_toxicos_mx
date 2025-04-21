
from config import df_residuos_tox_grouped_generacion_anio, clean_data_residuos_toxicos
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



#hacer una función para calcular quartiles con numpy
def calculo_quartiles(df, column):
    """Calcula los cuartiles de una columna específica del DataFrame usando numpy."""
    Q1 = np.percentile(df[column], 25) #valor que deja el 25% de los datos por debajo
    Q2 = np.percentile(df[column], 50) #valor que deja el 50% de los datos por debajo (mediana)
    Q3 = np.percentile(df[column], 75) #valor que deja el 75% de los datos por debajo
    return Q1, Q2, Q3
calculo_quartiles(clean_data_residuos_toxicos, 'generacion_estimada_ton_anio')
print("Cuartiles de la columna 'generacion_estimada_ton_anio':")

Q1, Q2, Q3 = calculo_quartiles(clean_data_residuos_toxicos, 'generacion_estimada_ton_anio')
print(f"Q1: {Q1}")
print(f"Q2: {Q2}")
print(f"Q3: {Q3}")

#rango intercuartilico
RI = Q3 - Q1
print(f"Rango intercuartilico: {RI}")
#limites inferior y superior
LI = Q1 - 1.5 * RI
print(f"Limite inferior: {LI}")
LS = Q3 + 1.5 * RI
print(f"Limite superior: {LS}")  

"""
Cuando calculas los cuartiles de una serie de números, lo que haces es ordenar todos los datos de menor a mayor y luego marcarlos en cuatro “partes” iguales. 
En este caso, esos números corresponden a la generación estimada de residuos tóxicos por año (en toneladas). 
Veamos qué significa cada resultado:

*Q1 = 0.015*
Q1 marca el punto en el que el 25% de las regiones en México generan 0.015t o menos. 
Dicho de otro modo, una de cada cuatro regiones está en ese rango más bajo de generación.

*Q2 = 0.21 (la mediana)*
Q2 divide los datos en dos mitades iguales: el 50% de las regiones generan 0.21t o menos, y el otro 50% generan 0.21t o más.
Es el “punto medio” de la distribución de generación anual.

*Q3 = 1.5125*
Q3 señala que el 75% de las regiones producen 1.5125t o menos al año. Solo la cuarta parte superior supera ese valor.

*Rango intercuartílico (IQR) = Q3 - Q1 = 1.4975*
Este número mide la “anchura” de la mitad central de tus datos. 
Indica que la distancia entre el límite inferior de la “mitad media” (0.015t) y su límite superior (1.5125t) es de 1.4975t.
Mientras más grande sea el IQR, más dispersos están tus datos en ese tramo intermedio.

*Límite inferior = Q1 - 1.5·IQR = -2.23125*
*Límite superior = Q3 + 1.5·IQR = 3.75875*
Se usan estos límites para detectar valores atípicos (“outliers”).
Cualquier observación por debajo de -2.23t o por encima de 3.76t se consideraría inusualmente baja o alta. 
En la práctica, como no puedes tener toneladas negativas, simplemente interpretas que no hay outliers por debajo (el mínimo real es 0t) y
que cualquier región que genere más de 3.75875t al año estaría muy por encima del rango normal y merecería un análisis especial.
"""   

#graficar boxplot con lineas de cuartiles y limites inferior y superior
import matplotlib.pyplot as plt
import seaborn as sns

def graficar_boxplot_log(df, column):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df[column], 
                notch=True,                      # caja con muesca en la mediana
                flierprops={'marker': 'o',        # mejor visibilidad de outliers
                            'markerfacecolor': 'gray',
                            'markersize': 4,
                            'alpha': 0.6})
    plt.xscale('log') #convierte el eje x a escala logaritmica. Así las diferencias entre los valores extremos son más visibles.
    plt.axvline(Q1, color='r', linestyle='--', label='Q1')
    plt.axvline(Q2, color='g', linestyle='--', label='Q2 (Mediana)')
    plt.axvline(Q3, color='b', linestyle='--', label='Q3')
    plt.axvline(LI, color='orange', linestyle='--', label='Límite Inferior')
    plt.axvline(LS, color='purple', linestyle='--', label='Límite Superior')
    plt.title(f'Boxplot de generación de residuos tóxicos (2017-2022) en México (escala log)')
    plt.xlabel("Residuos en toneladas")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()
    plt.savefig('./reports/boxplot_residuos_toxicos.png', dpi=300, bbox_inches='tight')


graficar_boxplot_log(clean_data_residuos_toxicos, 'generacion_estimada_ton_anio')




"""
    *Caja (IQR)*
Va de Q1 = 0.015 t a Q3 = 1.5125 t. Ahí dentro vive el 50 % central de las observaciones.

Línea dentro de la caja (mediana, Q2)
En 0.21 t, marca el punto medio de la distribución: la mitad de los casos está por debajo y la mitad por encima.

“Bigotes” (whiskers)
Se extienden desde el límite inferior real (no negativo, pues se ajusta al mínimo medido) hasta el límite superior permitido antes de considerarse outlier, que en este caso es 3.75875 t (= Q3 + 1.5·IQR).

Puntos fuera de los bigotes (outliers)
Todas las entidades que aparecen a la derecha de la línea púrpura (> 3.76 t) se consideran valores atípicos: generan muchísimo más que el rango “normal” de la mayoría.

*2. Asimetría y dispersión*
Distribución muy sesgada a la derecha
La escala logarítmica comprime los valores grandes y estira los pequeños. 
La “cola” derecha (las entidades de mayor generación) se prolonga muchísimo

Concentración baja de la “mitad media”
Que el IQR solo cubra de 0.015t a 1.51t indica que la mayoría de unidades produce cantidades muy pequeñas comparadas con los grandes generadores.

*3. ¿Qué nos dice esto?*
Mayoría de bajos productores
El 50% central produce entre 0.015t y 1.51t, y la mediana (0.21t) es aún más baja. La “mayoría” de las entidades maneja volúmenes reducidos.

Pocos grandes productores
Los outliers (muchos puntos a la derecha) revelan que hay unas pocas entidades con volúmenes extraordinariamente altos 
—probablemente grandes industrias o estados muy poblados— que distorsionan la media.

Necesidad de segmentación
Para entender realmente el comportamiento, conviene analizar por separado al grupo central (cuyos valores caben en la caja) y a los outliers,
pues sus causas (políticas de manejo, tipo de industria, tamaño poblacional) son muy distintas.
"""



