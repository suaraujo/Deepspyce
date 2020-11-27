import numpy as np

import pandas as pd

# records = 0
# medias = []
# deltas = []
fc = 1420.0
bw = 100.0
freq = np.linspace(fc - bw / 2.0, fc + bw / 2.0, num=2048)

path = input("Please, enter your raw data path: ")


def raw2df(raw):
    """
    Funcion para convertir datos RAW a DataFrame
    """
    spch = 2048
    bspl = 8
    raw.seek(0)
    data = raw.read()
    size = raw.tell()
    nrec = int(size / spch / bspl)
    dt = np.dtype("q")
    dt = dt.newbyteorder(">")

    np_data = np.frombuffer(data, dtype=dt)
    np_data = np.int64(np_data)
    np_data.resize(nrec, spch)
    np_data = np.transpose(np_data)
    df = pd.DataFrame(np_data)
    return df


if __name__ == "__main__":
    fd = open(path, "rb")
    data = raw2df(fd)
    # data.to_csv("test.csv")
    fd.close()
# This is the end
