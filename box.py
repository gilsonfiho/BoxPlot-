import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Substitua esta lista pelos seus dados
dados = [
    1115.7677, 1167.79715, 1033.12778, 1041.50967, 966.84937,
    1002.80573, 1099.78822, 1219.93792, 1127.10463, 1120.65313,
    1098.29805, 1256.08909, 1094.15391, 1006.35532, 1196.33049
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
sns.boxplot(y=df["Valores"], color="skyblue")
plt.title("Box Plot dos Valores")
plt.ylabel("Valor")
plt.grid(True)
plt.tight_layout()
plt.show()
