import polars as pl
from plotnine import *
from pyhere import here

# Load data.
customer_data = pl.read_csv(here('data', 'customer_data.csv'))
store_transactions = pl.read_csv(here('data', 'store_transactions.csv'))

# Visualize customers by region.
(ggplot(customer_data, aes(x = 'region'))
  + geom_bar()
)

# Number of customers by region.
(customer_data
  .group_by(pl.col('region'))
  .agg(n = pl.len())
)

# Visualize income distribution.
(ggplot(customer_data, aes(x = 'income'))
  + geom_histogram()
)

# Average customer income.
(customer_data
  .select(pl.col('income'))
  .mean()
)

# Visualize relationship between income and gender by region.
(ggplot(customer_data, aes(x = 'income', fill = 'gender', color = 'gender'))
  + stat_bin(geom = 'area', alpha = 0.5, position = 'identity')
  + facet_wrap('~region')
)

# Summary of average income by gender and region.
(customer_data
  .group_by(pl.col(['gender', 'region']))
  .agg(
    n = pl.len(), 
    avg_income = pl.col('income').mean()
  )
  .sort(pl.col('avg_income'), descending=True)
)

# How old is the customer in the West who purchased the most in Feb 2005?
(customer_data
  .join(store_transactions, on='customer_id', how='left')
  .filter(pl.col('region') == 'West', pl.col('feb_2005') == pl.col('feb_2005').max())
  .with_columns(age = 2024 - pl.col('birth_year'))
  .select(pl.col(['age', 'feb_2005']))
  .sort(pl.col('age'), descending = True)
  .slice(0, 1)
)
