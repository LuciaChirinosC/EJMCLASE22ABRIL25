import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_price_distribution(df: pd.DataFrame):
    """
    Genera un histograma que muestra la distribución de precios de los vehículos.
    :param df: DataFrame con los datos de vehículos.
    :return: Figura de Matplotlib con el gráfico generado.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(df["price"], bins=30, kde=True, color="blue", ax=ax)
    ax.set_xlabel("Precio")
    ax.set_ylabel("Frecuencia")
    ax.set_title("Distribución de Precios de los Vehículos")
    ax.grid()
    return fig