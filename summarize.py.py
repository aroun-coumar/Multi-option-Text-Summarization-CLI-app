"""summarize.
Usage:
  summarize -h | --help
  summarize --version
  summarize -l | --list
  summarize -wf | --word_frequency_model
  summarize -tr | --textrank_graph_model
  summarize -bs | --bert_clustering_summary
Options:
  -h, --help            Show this screen.
  --version             Show version.
  -wf, --word_frequency_model                 Summarize with word_frequency_model
  -tr, --textrank_graph_model                 Summarize with textrank_graph_model
  -bs, --bert_clustering_summary              Summarize with --bert_clustering_summary

"""
from docopt import docopt
import numpy as np
import pandas as pd
import sys


#df = pd.read_csv('C:\Users\ansar\Desktop\nlp_text_summarization_implementation-master\opinosis.csv')
## Clean the paragraph

def rm_rrn(string):
    if isinstance(string, str):
        return string.replace('\r\r\n',' ')
def clean_para(para):
    df = df.applymap(rm_rrn) 
    text1 = df['text'][0]
    #df['summary_number_1'][0]  
    from rouge import Rouge
    #rouge = Rouge() 
    #rouge.get_scores(df['summary_number_2'][0], df['summary_number_1'][0])


def main():
    args=docopt(__doc__,version='summarize 1.0.11')
    util(args)



def util(docopt_args):
    if docopt_args["--word_frequency_model"]:
        print ("1")
        sys.path.append(r"C:/Users\ansar\AppData\Local\Programs\Python\Python39\Lib\site-packages\summarize\word_frequency_model.py")
        import word_frequency_model as wf
        val1 = input("Enter your paragraph: /n/n/n")
        df = pd.DataFrame([val1], columns=['string_values'])
        ab=df['string_values'][0]
        #clean_para(val1)
        wf_summary1 = wf.summarize_text_wf(ab)
        print(wf_summary1) 

    elif docopt_args["--textrank_graph_model"]:
        print("2")
        sys.path.append(r"C:\Users\ansar\AppData\Local\Programs\Python\Python39\Lib\site-packages\summarize\textrank_graph_model.py")
        import textrank_graph_model as tr
        val2 = input("Enter your paragraph: ")
        df = pd.DataFrame([val2], columns=['string_values'])
        ab=df['string_values'][0]
        #clean_para(val2)
        tr_summary1 = tr.gensim_summarize(val2)
        print(tr_summary1)


    elif docopt_args["--bert_clustering_summary"]:
        print("3")
        sys.path.append(r"C:\Users\ansar\AppData\Local\Programs\Python\Python39\Lib\site-packages\summarize\bert_clustering_summary.py")
        import bert_clustering_summary as bs
        val3 = input("Enter your paragraph: /n/n/n")
        #clean_para(val3)
        df = pd.DataFrame([val1], columns=['string_values'])
        ab=df['string_values'][0]
        bs_summary1 = bs.bertSummarize(val3)
        print(bs_summary1)

if __name__=='__main__':
    main()