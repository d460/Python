import simplekml
import pandas

df = pandas.read_csv("Coordenadas.csv")
kml = simplekml.Kml()
for lon, lat in zip(df["Longitud"], ["Latitud"]):
    kml.newpoint(coords=[(lon, lat)])
kml.save("Puntos.kml")