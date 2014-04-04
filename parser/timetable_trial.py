# -*- coding: cp1251 -*-
import re
import codecs

def parseHeaderMgtRu(header_line):  
   header_line = " ".join(header_line)
   info = str(header_line).strip('[]')
   p = re.compile('colspan=\d+>(.+)<BR>РАСП')
   tr_stop = " ".join(p.findall(info))
   p = re.compile('№(.+)<BR> ДО ОСТ')
   route = " ".join(p.findall(info))
  # print route
   p = re.compile('ДО ОСТ. (.+)<BR>')
   direction = " ".join(p.findall(info))
   p = re.compile('ДО ОСТ\..+<BR> (.+)</th>')
   days = " ".join(p.findall(info))
   return tr_stop, route, direction, days
  
def parseHeaderMgtOrg(stop_name, line_route, week_days):
   line_route = " ".join(line_route)
   info1 = str(line_route).strip('[]')
   p = re.compile('маршрута (.+)от остановки <b>')
   route = " ".join(p.findall(info1))
   p = re.compile('<b>(.+)</h3')
   direction = " ".join(p.findall(info1))
   week_days = " ".join(week_days)
   info2 = str(week_days).strip('[]')
   p = re.compile('<h3>Для дней недели: (.+)</h3>')
   days = " ".join(p.findall(info2))
   info3 = str(stop_name).strip('[]')
   p = re.compile('tr><td><h2>(.+)</h2></td></tr><tr><t')
   tr_stop = " ".join(p.findall(info3))
   return tr_stop, route, direction, days
   

def parseTimetable(f):
     """
This function does parsing information of
Moscow public ground transport timetable
from two websites:
Mosgortrans.ru and Mosgortrans.org
Params:
f: discriptor of html file with information about
timetable of one rout on its particular stop in one direction
Returns:
number of rout, diriction, stop name, timetable on this stop
and days when this timetable is active
     """
     timetable = []
     header = 'none'
     isMgtRu = True
     for line in f:
        if isinstance(line, unicode):
           line = line.encode('cp1251')
        line_m = line.strip()
        split_line = line_m.split(" ")
        if line_m == '<html>':
          isMgtRu = False
      #    print line_m
          
        if isMgtRu:          
            if split_line[0] == '<th':
               header = parseHeaderMgtRu(split_line)
            if split_line[0] == '<td':
               h = re.compile('hour\d>(\d+)</td><td')
               hour = h.findall(split_line[1])
               m = re.compile('>(\d\d)<')
               minute = m.findall(split_line[2])
               if minute != []:
                   for i in minute:
                       time = hour[0]+":"+ i
                       timetable.append(time)
        else:     
            if split_line[0] == '<h3>Расписание':                  
               line_route = split_line
            if split_line[0] == '<h3>Для':
               week_days = split_line
            if line_m[:12] == '<tr><td><h2>':
               stop_name = split_line[:2]                           
               header = parseHeaderMgtOrg(stop_name, line_route, week_days)
            if line_m[:18] == '<span class="hour"':
              # print line_m
               h = re.compile('class="hour">(\d+)</span></td>')
               hour = h.findall(line_m)
            for i in range(len(split_line)):
              if split_line[i] == 'class="minutes"':
                m = re.compile('>(\d\d)</span><br>')
                minute = m.findall(split_line[i+1])
                if minute != []:
                   time = hour[0]+":"+minute[0]
                   timetable.append(time)
            
     tr_time = timetable
     return header, tr_time 
  

if __name__ == '__main__':
  b_file = "3.htm"
  with codecs.open(b_file, encoding='utf-8') as f:
    info = parseTimetable(f)
  print info
              
