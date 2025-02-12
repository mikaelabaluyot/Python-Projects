from exa_py import Exa


exa = Exa('5e4de4ba-cbd7-4816-9efc-b2114c5e3241')

query = input('Search here: ')
base_url = 'https://www.boardgamegeek.com'

response = exa.search(
  query,
  num_results=1,
  type='keyword',
  include_domains=[
    'boardgamegeek.com'
  ],
)


if response and hasattr(response, 'results'):
    for result in response.results:
        print(f'Title: {result.title}')
        print(f'URL: {result.url}')
        print()