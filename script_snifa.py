import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from bs4 import BeautifulSoup
from snifa.models import Sancion, UnidadFiscalizable

import requests

URL = "https://snifa.sma.gob.cl/Sancionatorio/Resultado"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", id="myTable")
tbody = table.find("tbody")
rows = tbody.find_all("tr")

for row in rows:
    cells = row.find_all("td")

    unidad_fiscalizable, _ = UnidadFiscalizable.objects.get_or_create(
        nombre=cells[2].find("a").text.strip()
    )
    sancion = Sancion.objects.create(
        expediente=cells[1].text.strip(),
        unidad_fiscalizable=unidad_fiscalizable,
        nombre_razon_social=cells[3].find("li").text.strip(),
        categoria=cells[4].find("li").text.strip(),
        region=cells[5].find("li").text.strip(),
        estado=cells[6].text.strip(),
        detalle_link=cells[7].find("a")["href"],
    )
