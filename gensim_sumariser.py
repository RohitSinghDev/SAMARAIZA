# prints only the core points as the summarised text

pip install gensim

from gensim.summarization import summarize

text = "Today videos organisation freed online shopping Government and private sector organisations Catering and Tourism industry or other Institutions offer Customer services are concerned about their customers and ask for feedback every single time we use the services consider the fact that these companies may be receiving enormous amount of he is a fact every single day and it will become quite tedious for the management in analyse each of those were the technology today we have reached the election was they who was the task of human beings and the field which makes this happen is machine learning the Machines have KEM Re KEM understand human language is used in National Knowledge Commission today uses of being done in the field of text analytics and ones application of text analytics and foetus is a which helps in summarising and not with the Axes of environment can be done in an algorithm to ready for the subtext but keeping his what is the meaning of giving a great insight in the original text if you're interested and Data Analytics and you will find turning about natural language processing very useful Passion Pro visor elements live"

len(text)

summary_txt = summarize(text)
len(summary_txt)
