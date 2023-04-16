from pathlib import Path
from urllib.request import urlopen
import streamClasses


Path("m3u/").mkdir(parents=True, exist_ok=True)

with urlopen("https://ft1.ftp.sh/diziler.m3u") as r:
    s = r.read().decode('utf-8')
    with open('m3u/diziler.m3u', "w") as fd:
      fd.write(s)

streams = streamClasses.rawStreamList('m3u/diziler.m3u')
