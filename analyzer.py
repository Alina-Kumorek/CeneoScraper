import os
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# print(*[filename.removesuffix(".json") for filename in os.listdir("./opinions")], sep="\n")
# product_code = input("Podaj kod produktu: ")
product_code = 39562616

opinions = pd.read_json(f"opinions/{product_code}.json")
opinions.score = opinions.score.map(lambda x: x.split("/")[0].replace(",", ".")).astype(float)
stats = {
    "opinions_count": opinions.shape[0],
    "pros_count": opinions.pros.astype(bool).sum(),
    "cons_count": opinions.cons.astype(bool).sum(),
    "average_score": opinions.score.mean(),
}

print(f"""Dla produktu o kodzie {product_code}
pobranych zostało {stats["opinions_count"]} opinii/opinie.
Dla {stats["pros_count"]} opinii podana została lista zalet produktu,
a dla {stats["cons_count"]} opinii podana została lista jego wad.
Średnia ocena produktu wynosii {stats["average_score"]:.2f}.""")

stars = opinions.score.value_counts().reindex(list(np.arange(0, 5.5, 0.5)), fill_value=0)
stars.plot.bar()
plt.show()