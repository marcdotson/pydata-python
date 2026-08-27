import polars as pl
import seaborn.objects as so
import os

# Load data.
customer_data = pl.read_csv(os.path.join('data', 'customer_data.csv'))
store_transactions = pl.read_csv(os.path.join('data', 'store_transactions.csv'))

# Visualize customers by region.
(so.Plot(customer_data, x = 'region')
  .add(so.Bar(), so.Hist())
)

# Number of customers by region.
(customer_data
  .group_by(pl.col('region'))
  .agg(n = pl.len())
)

# Visualize income distribution.
(so.Plot(customer_data, x = 'income')
  .add(so.Bars(), so.Hist())
)

# Average customer income.
(customer_data
  .select(pl.col('income'))
  .mean()
)

# Visualize relationship between income, credit, and gender by region.
(so.Plot(customer_data, x = 'income', y = 'credit', color = 'gender')
  .facet('region')
  .add(so.Area(), so.Hist())
)

# Summary of average income and credit by gender and region.
(customer_data
  .group_by(pl.col(['gender', 'region']))
  .agg(
    n = pl.len(), 
    avg_income = pl.col('income').mean(), 
    avg_credit = pl.col('credit').mean()
  )
  .sort(pl.col('avg_income'), descending=True)
)

