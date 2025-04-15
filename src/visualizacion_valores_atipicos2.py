from config import df_residuos_tox_grouped_generacion_anio
import matplotlib.pyplot as plt
import seaborn as sns 
plt.figure(figsize=(10, 6))
sns.regplot(x='anio', y='generacion_estimada_ton_anio_total', data=df_residuos_tox_grouped_generacion_anio, scatter_kws={'s': 50, 'alpha': 0.5}, line_kws={'color': 'orange'})
plt.title('Generación estimada de residuos tóxicos por año en México', fontsize=16, weight='bold')


plt.xlabel('Año', fontsize=12)

plt.ylabel('Generación estimada (toneladas)', fontsize =12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('C:/Users/zaire/Portafolio/Data/residuos_tox_mex/reports/regplot_generacion_residuos.png', dpi=300, bbox_inches='tight')
plt.show()
