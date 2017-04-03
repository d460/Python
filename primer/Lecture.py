import simplekml
import pandas
import tkinter
from tkinter.filedialog import askopenfilename

def browse():
    global infile
    infile=askopenfilename()


def kmlfuntion(outfile="Puntos.kml"):
    df = pandas.read_csv(infile)
    kml = simplekml.Kml()
    for lon, lat in zip(df["Longitud"], ["Latitud"]):
        kml.newpoint(coords=[(lon, lat)])
    kml.save(outfile)

root = tkinter.Tk()
root.title("KML Generator")
label = tkinter.Label(root, text="Este programa genera un archivo KML")
label.pack()
button1 = tkinter.Button(root, text="Browse", command=browse)
button1.pack()
kmlbutton = tkinter.Button(root, text="Generate KML", command=kmlfuntion)
kmlbutton.pack()
root.mainloop()

