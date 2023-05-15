import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django

django.setup()

import json

import requests
from bs4 import BeautifulSoup

from snifa.models import Sancion, UnidadFiscalizable

URL = "https://snifa.sma.gob.cl/Sancionatorio/Resultado"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", id="myTable")
tbody = table.find("tbody")
rows = tbody.find_all("tr")

data = []
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
    data.append(
        {
            "expediente": sancion.expediente,
            "unidad_fiscalizable": unidad_fiscalizable.nombre,
            "nombre_razon_social": sancion.nombre_razon_social,
            "categoria": sancion.categoria,
            "region": sancion.region,
            "estado": sancion.estado,
            "detalle_link": sancion.detalle_link,
        }
    )

with open("sanciones.json", "w") as file:
    json.dump(data, file)
