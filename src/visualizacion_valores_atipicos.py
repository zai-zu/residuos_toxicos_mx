from config import df_residuos_tox_grouped_generacion_anio
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))

# Boxplot base
sns.boxplot(
    x='anio',
    y='generacion_estimada_ton_anio_total',
    data=df_residuos_tox_grouped_generacion_anio,
    color='lightgray'  # color neutro para que resalten los puntos
)

# Agregamos los puntos con color personalizado
sns.stripplot(
    x='anio',
    y='generacion_estimada_ton_anio_total',
    data=df_residuos_tox_grouped_generacion_anio,
    jitter=True,         # separa ligeramente los puntos para mejor visibilidad
    hue='anio',          # así se les asigna un color diferente por año
    palette='Set2',      # paleta de colores ('Set1', 'pastel', etc.)
    dodge=False,
    size=6,              # tamaño de los puntos
    alpha=0.8            # un poco de transparencia
)

plt.title('Generación estimada de residuos tóxicos por año en México', fontsize=16, weight='bold')
plt.xlabel('Año', fontsize=12)
plt.ylabel('Generación Estimada (toneladas)', fontsize=12)
plt.legend([],[], frameon=False)  # Ocultar leyenda innecesaria
plt.tight_layout()

# Guardar
plt.savefig('C:/Users/zaire/Portafolio/Data/residuos_tox_mex/reports/boxplot_generacion_residuos.png', dpi=300, bbox_inches='tight')
plt.show()
