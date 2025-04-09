import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Substitua esta lista pelos seus dados
dados = [
    3259.0926, 3409.0904, 3840.652, 3997.495, 4125.8268,
    3275.2636, 3639.0954, 3657.5272, 3129.9444, 3106.7712,
    3562.9818, 3543.0742, 3562.9504, 3316.9628, 3251.6508
]

# Criar DataFrame
df = pd.DataFrame(dados, columns=["Valores"])

# Calcular estatísticas
media = df["Valores"].mean()
mediana = df["Valores"].median()
desvio_padrao = df["Valores"].std()
q1 = df["Valores"].quantile(0.25)
q3 = df["Valores"].quantile(0.75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
outliers = df[(df["Valores"] < limite_inferior) |
              (df["Valores"] > limite_superior)]

# Mostrar tabela de estatísticas
tabela = pd.DataFrame({
    "Estatística": [
        "Média", "Mediana", "Desvio Padrão", "Q1 (25%)", "Q3 (75%)",
        "IQR (Q3 - Q1)", "Limite Inferior", "Limite Superior", "Outliers?"
    ],
    "Valor": [
        round(media, 2), round(mediana, 2), round(desvio_padrao, 2),
        round(q1, 2), round(q3, 2), round(iqr, 2),
        round(limite_inferior, 2), round(limite_superior, 2),
        "Sim" if not outliers.empty else "Não"
    ]
})

print(tabela.to_string(index=False))

# Criar box plot
plt.figure(figsize=(6, 8))
sns.boxplot(y=df["Valores"], color="lightgreen")
plt.title("Box Plot dos Valores")
plt.ylabel("Valor")
plt.grid(True)
plt.tight_layout()

# Caminho para salvar fora da pasta src, dentro de ../img/
caminho_img = os.path.join(os.path.dirname(
    __file__), '..', 'img', 'boxplot.png')

# Criar pasta img se não existir
os.makedirs(os.path.dirname(caminho_img), exist_ok=True)

# Salvar imagem
plt.savefig(caminho_img)
plt.close()
print(f"Imagem salva em: {caminho_img}")
