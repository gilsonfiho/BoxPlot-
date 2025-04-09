# BoxPlot-

Este projeto permite a geração de box plots a partir de uma lista de dados, com relatórios de análise estatística automática.

## 📦 Funcionalidades

- Geração de box plots com `seaborn` e `matplotlib`
- Cálculo de estatísticas descritivas:
  - Média, Mediana, Desvio Padrão
  - Quartis (Q1, Q3), IQR
  - Limites inferior e superior para outliers
  - Indicação se há outliers
- Salvamento automático das imagens em uma pasta `img/` fora da pasta `src/`

## 📁 Estrutura do Projeto

```
BoxPlot-/
├── img/                # Pasta onde os gráficos são salvos
├── src/
│   └── main.py         # Script principal que gera o gráfico
└── requirements.txt    # Dependências do projeto
```

## ▶️ Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/gilsonfiho/BoxPlot-.git
cd BoxPlot-
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute o script

```bash
cd src
python main.py
```

A imagem será salva automaticamente em `../img/boxplot.png`

## 📊 Exemplo de estatísticas geradas

O script imprime algo como:

```
 Estatística       Valor
     Média       1123.12
   Mediana       1115.77
Desvio Padrão      90.45
 Q1 (25%)        1045.54
 Q3 (75%)        1196.33
IQR (Q3 - Q1)     150.79
Limite Inferior   819.36
Limite Superior  1422.51
Outliers?         Não
```

## 📌 Observações

- A pasta `img/` será criada automaticamente caso não exista.
- Você pode substituir os dados manualmente dentro do script `main.py`.

## 🤝 Contribuindo

1. Faça um fork
2. Crie sua branch: `git checkout -b minha-feature`
3. Faça commit das alterações: `git commit -m 'feat: minha nova feature'`
4. Faça push: `git push origin minha-feature`
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a Licença MIT.
