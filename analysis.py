import os
import glob
import pandas as pd
import requests
import pyphen
from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')
nltk.download('cmudict')
from nltk.corpus import cmudict
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords


# creating master dictionary
master_dict = {}

# Load positive words
with open('MasterDictionary/positive-words.txt', 'r', encoding='latin-1') as f:
    for line in f:
        word = line.strip()
        master_dict[word] = 1

# Load negative words
with open('MasterDictionary/negative-words.txt', 'r', encoding='latin-1') as f:
    for line in f:
        word = line.strip()
        master_dict[word] = -1

print("master dictionary is created")


# creating Stop word tuple
stop_words = set()  
file_paths = glob.glob('StopWords/StopWords_*.txt')  
for file_path in file_paths:
    with open(file_path, 'r', encoding='latin-1') as file:
        for line in file:
            stop_words.add(line.strip())
print(f"Stop word tuple is created with {len(stop_words)} words")


#loading Input.xlsx and Output Data Structure.xlsx
df_input = pd.read_excel('Input.xlsx')
df_output = pd.read_excel('Output Data Structure.xlsx')


#folder_path for text files
folder_path = "URL_text_files"

'''

# Save the title and descriptions in the text file
os.makedirs(folder_path, exist_ok=True)  # Create the folder if it doesn't exist
for i, row in df_input.iterrows():
    url_id = str(int(row['URL_ID']))
    url = row['URL']
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title_text = soup.find('title').get_text()
    descriptions = soup.find_all('p')
    file_path = os.path.join(folder_path, f'{url_id}.txt')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(title_text + "\n\n")
        for description in descriptions:
            file.write(description.get_text() + '\n')
print("all text files created and now comment out the creater program")

'''

# Function to clean the data of each text file
def clean_text(article_text,stop_words):
    tokens = word_tokenize(article_text.lower())
    cleaned_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
    return cleaned_tokens

# Function which perform text analysis to compute variables
def analyze_text(article_text, master_dict, stop_words):
    cleaned_tokens = clean_text(article_text, stop_words)
    # Compute Derived Variables
    positive_score = sum([master_dict.get(token, 0) for token in cleaned_tokens if master_dict.get(token, 0) > 0])
    negative_score = sum([master_dict.get(token, 0) for token in cleaned_tokens if master_dict.get(token, 0) < 0])
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (len(cleaned_tokens) + 0.000001)
    # Analysis of Readability
    sentences = nltk.sent_tokenize(article_text)
    word_count = len(cleaned_tokens)
    sentence_count = len(sentences)
    # Average Sentence Length
    avg_sentence_length = word_count / sentence_count
    # Complex Word Count
    dic = pyphen.Pyphen(lang='en')
    complex_words = [word for word in cleaned_tokens if len(dic.inserted(word).split('-')) > 2]    
    # Percentage of Complex words
    percentage_complex_words = len(complex_words) / word_count
    # Fog Index
    fog_index = 0.4 * (avg_sentence_length + percentage_complex_words)
    # Average Number of Words Per Sentence
    avg_words_per_sentence = word_count / sentence_count
    # Complex Word Count
    complex_word_count = len(complex_words)
    # Syllable Count Per Word
    prondict = cmudict.dict()
    # Inside your function...
    syllables = [len(prondict[word.lower()][0]) if word.lower() in prondict else 0 for word in cleaned_tokens]
    syllable_per_word = sum(syllables) / word_count
    # Personal Pronouns
    personal_pronouns = ['I','me','you','You','Your','your','he','she','it','He','She','It','him','her','Him','Her','we','We','us','Us','Its','its','Yours','yours','they','They','Them','them','Our','our']    
    personal_pronoun_count = sum([cleaned_tokens.count(pp) for pp in personal_pronouns])
    # Average Word Length
    avg_word_length = sum(len(word) for word in cleaned_tokens) / word_count

    return (positive_score, negative_score, polarity_score, subjectivity_score, avg_sentence_length,percentage_complex_words, fog_index, avg_words_per_sentence, complex_word_count,word_count, syllable_per_word, personal_pronoun_count, avg_word_length)


# perform text analysis to compute variables

for i, row in df_output.iterrows():
    url_id = str(int(row['URL_ID']))
    for filename in os.listdir(folder_path):
        if filename.endswith(f"{url_id}.txt"):
            filepath = os.path.join(folder_path, filename)
            with open(filepath, "r", encoding='utf-8') as file:
                article_text = file.read()
                print(f"reading this file {filename}")
                positive_score, negative_score, polarity_score, subjectivity_score, avg_sentence_length, percentage_complex_words, fog_index, avg_words_per_sentence, complex_word_count, word_count, syllable_per_word, personal_pronoun_count, avg_word_length = analyze_text(article_text, master_dict, stop_words)
                df_output.at[i, 'POSITIVE SCORE'] = positive_score
                df_output.at[i, 'NEGATIVE SCORE'] = negative_score
                df_output.at[i, 'POLARITY SCORE'] = polarity_score
                df_output.at[i, 'SUBJECTIVITY SCORE'] = subjectivity_score
                df_output.at[i, 'AVG SENTENCE LENGTH'] = avg_sentence_length
                df_output.at[i, 'PERCENTAGE OF COMPLEX WORDS'] = percentage_complex_words
                df_output.at[i, 'FOG INDEX'] = fog_index
                df_output.at[i, 'AVG NUMBER OF WORDS PER SENTENCE'] = avg_words_per_sentence
                df_output.at[i, 'COMPLEX WORD COUNT'] = complex_word_count
                df_output.at[i, 'WORD COUNT'] = word_count
                df_output.at[i, 'SYLLABLE PER WORD'] = syllable_per_word
                df_output.at[i, 'PERSONAL PRONOUNS'] = personal_pronoun_count
                df_output.at[i, 'AVG WORD LENGTH'] = avg_word_length
                print(f"successful for {filename} \n\n")

                
# saving the output file
df_output.to_excel('output.xlsx', index=False)
print("output file saved")
