from datetime import datetime


date,time=datetime.now().strftime("%d-%m-%y"),datetime.now().time()


print(date,"\n",time)