stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53,
 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(x):
  return stock_prices[x-1]

def max_price(a, b):
    m_a_x = 0
    for i in range(a,b + 1):
        m_a_x = max(m_a_x, price_at(i))
    return m_a_x

def min_price(a,b):
    m_i_n = price_at(a)
    for i in range(a, b + 1):
        m_i_n = min(m_i_n, price_at(i))
    return m_i_n

print(max_price(2,17))
print(min_price(1,5))
print(price_at(4))