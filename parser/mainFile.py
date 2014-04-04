from timetable_trial import parseTimetable
from dwnld import download
import sqlite3

url = 'http://www.mosgortrans.ru/rasp/1/2188303/45140/3689/index.html'
b_file = download(url)
trType = 1
info = parseTimetable(b_file)
print info

conn = sqlite3.connect('info.db')
c = conn.cursor()
c.execute('CREATE TABLE Stops(stopId int, name text, mgtId int)')
c.execute('CREATE TABLE Routes(routeId int, stopId int, stopOrder int)')
c.execute('CREATE TABLE Schedule(routeId int, stopId int, wDay int, time int)')
conn.commit()

#c.execute("INSERT INTO stocks VALUES ('й/р &quot;оепбнлюияйхи&quot;','15','&quot;яр. песрнбн&quot;','асдмх', '5:30')")

#c.execute("INSERT INTO stocks VALUES (info[0][0],info[0][1],info[0][2],info[0][3],info[0][4])")
