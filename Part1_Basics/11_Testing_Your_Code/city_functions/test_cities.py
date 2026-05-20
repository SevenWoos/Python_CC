from city_functions import city_country

def test_city_country():
  formatted_city = city_country('santiago', 'chile', 5000000)
  assert formatted_city == 'Santiago, Chile - 5000000'

  formatted_city2 = city_country('Taipei', 'Taiwan')
  assert formatted_city2 == 'Taipei, Taiwan'
