#/usr/bin/python3
from textblob import TextBlob
import matplotlib.pyplot as plt
get_data="hello i am happy because its a beautiful day."
get_data2=" today i am watching a movie but its a bad movie."
get_data3=" i did not liked the movie. how are you?"
#for i in get_data :
#i.split()
analysis=TextBlob(get_data)
analysis2=TextBlob(get_data2)
analysis3=TextBlob(get_data3)
print(analysis.sentiment)
print(analysis2.sentiment)
print(analysis3.sentiment)
x=[1,2,3]
y=[analysis.polarity,analysis2.polarity,analysis3.polarity]
plt.pie(y)
plt.show()
