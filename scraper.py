import requests

# product_code = input("Podaj kod produktu: ")
product_code = "95733300"

# url = "https://www.ceneo.pl/" + product_code + "#tab=reviews"
url = f"https://www.ceneo.pl/{product_code}#tab=reviews"
# url = "https://www.ceneo.pl/{}#tab=reviews".format(product_code)

response = requests.get(url)
print(response.status_code)