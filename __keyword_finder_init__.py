# Import libraries and modules
import pandas as pd
import nltk
#from nltk.corpus import stopwords
import re
import string
wn = nltk.WordNetLemmatizer() #Lemmatizer

#stopword = nltk.corpus.stopwords.words('english') #Stopwords in English language


def matching_keywords(job_posting, resume):

    
    def clean_the_text(text):
        """
        Function to clean and tokenize the text.
        Input: 
            job_posting: text file
            resume: text_file
        Output: 
            text: cleaned and tekenized body of text        
        """
        
        #Replace non-word characters with empty space
        text = re.sub('[^A-Za-z0-9\s]', ' ', text)
        
        #Remove punctuation
        text = ''.join([word for word in text if word not in string.punctuation])
        
        #Bring text to lower case
        text = text.lower()
        
        #Tokenize the text
        tokens = re.split('\W+', text)
        
        #Remove stopwords
        #text = [word for word in tokens if word not in stopword]
        
        #Lemmatize the words
        text = [wn.lemmatize(word) for word in tokens]
        
        #Return text
        return text
        
        
    #Apply clean_the_text function to the text files   
    list_1 = clean_the_text(job_posting)
    list_2 = clean_the_text(resume)
    
    
    def common_words(l_1, l_2):
        """
        Input: 
            l_1: list of words
            l_2: list_of words
        Output: 
            matching_words: set of common words exist in l_1 and l_2        
        """
        matching_words = set.intersection(set(l_1), set(l_2))
        return matching_words
    
    #Apply common_words function to the lists
    common_keywords = common_words(list_1, list_2)
    
    #Print number of matching words
    string_1 = 'The number of common words in your resume and the job posting is: {}'.format(len(common_keywords))
    
    #Print the percentage of matching words
    string_2 = '{:.0%} of the words in your resume are in the job description'.format(len(common_keywords)/len(list_2))    
    
    # Create an empty dictionary
    word_count_table = {}
    
    # Create frequency table for the words that are not in the list_2 but in the list_1
    for word in list_1:
        if not word in list_2:
            if word in word_count_table:
                word_count_table[word] += 1
            else:
                word_count_table[word] = 1
    
    # Sort the dictionary by values in descending order
    word_count_table = dict(sorted(word_count_table.items(), key=lambda item: item[1], reverse=True))
    
    # Create a pandas dataframe from the dictionary
    pd.set_option('display.max_rows', 300)
    df = pd.DataFrame.from_dict(word_count_table.items())
    
    # Rename columns
    df.columns = ['word','count']

    #df.to_html()
        
    """print('You can choose some words in the job posting from the table below to add your resume.')
    """

    result_dict = {}
    result_dict['string_1'] = string_1
    result_dict['string_2'] = string_2
    result_dict['table'] = df.to_html()
    return result_dict