import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
nltk.download('punkt')
nltk.download('stopwords')
BASE2 = os.path.dirname(os.path.abspath(__file__))



with open(os.path.join(BASE2, "test.txt"),'r') as f:
    f_contents=f.read()

stop_words = nltk.corpus.stopwords.words('english')
numbers_list=[str(num) for num in range(0,30)]

new_words=[',','.','.','I','Is','(',')','?','@','You',':','"','1.',"''",'what','we','12.','if','how',"if",'where','If','How','What',';','Where','When','"','We','Select','Who','us','Can','hi']
stop_words.extend(new_words)
stop_words.extend(numbers_list)
word_tokens = word_tokenize(f_contents)

filtered_words = [w for w in word_tokens if not w in stop_words]

filtered_lower=[x.lower() for x in filtered_words]


def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
word_dict={}

for word in filtered_lower:
    word_dict[word]=countX(filtered_lower,word)
sorted_by_value = sorted(word_dict.items(), key=lambda kv: kv[1])
sorted_by_value.reverse()

def show(m):
    n=int(m)
    if n>len(sorted_by_value):
        n=len(sorted_by_value)
    return_list=[]
    for i in range(0,n):
        return_list.append(sorted_by_value[i])
    return return_list







    
