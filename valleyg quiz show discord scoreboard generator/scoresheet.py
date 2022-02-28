from datetime import datetime

def calculate_rank(sorted_vector):
  a={}
  rank=1
  for num in sorted_vector:
    if num not in a:
      a[num]=rank
      rank=rank+1
  return[a[i] for i in sorted_vector]

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

f = open("scoreboard.txt", "w+")
x = open("rawscores.txt", "r")

#f.write("Scores as of: {}\n".format(current_time))
f.write("---FINAL SCOREBOARD FOR QUIZ SHOW HS ELIMS---\n")
f.write("Rank       School      Score    \n")
f.write("---------------------------------\n")

schools = []
schools_txt = open("schools.txt", "r")
for school in schools_txt:
  schools.append(school[:-1])

scores = {}
ctr = 0
for score in x:
  scores[schools[ctr]] = int(score)
  ctr+=1

sorted_scores = {k: v for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)}

ranks = calculate_rank(list(sorted_scores.values()))


ctr = 1
for k,v in sorted_scores.items():
  f.write("   {}        ".format(ranks[ctr-1]))
  if(ranks[ctr-1]<10):
    f.write("  ")
  f.write(k)
  f.write("  ")
  f.write("        {}".format(v))
  f.write("\n")
  if(ctr==10):
    f.write("----------------------------------\n")
  ctr+=1

f.write("\n\n")

f.close
x.close
schools_txt.close