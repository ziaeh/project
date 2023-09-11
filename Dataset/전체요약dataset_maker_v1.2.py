import  numpy as np
from glob import glob
import json
import pandas as pd

class DataMaker():

    '''
    데이터가 담긴 폴더 경로를 parameter로 받아서 
    train, test 폴더의 모든 json 파일에서 passage, summary1를 추출해 
    각 train, test 데이터에 대한 tsv 파일 저장

    [parameter]
        folder_path : 폴더경로(str) - train_json, test_json 폴더를 포함하고 있는 상위 폴더의 경로 
    '''

    def __init__(self, folder_path):
        
        self.folder_path = folder_path

        self.train_file_path_list = self.get_train_path_list()
        self.test_file_path_list = self.get_test_path_list()


    def get_train_path_list(self):
        train_file_path_list = glob(self.folder_path + "\\train_json\\**\\*.json", recursive=True)
        return train_file_path_list


    def get_test_path_list(self):
        test_file_path_list = glob(self.folder_path + "\\test_json\\**\\*.json", recursive=True)
        return test_file_path_list

    def make_passage_summary_df(self, file_path_list):
        '''
        date_tag의 모든 데이터를
        'passage','summary1','summary2' 라는 이름의 컬럼으로 가지는 데이터프레임을 반환하는 함수

        data_tag = {
            passage:('Meta(Refine)','passage'), 
            summary1:('Annotation','summary1')}
        '''
        passage_values = []
        summary_values = []


        for file_path in file_path_list:

            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
     
                passage = data['Meta(Refine)']['passage']
                passage = ' '.join(passage.split('\n')) 

                summary = data['Annotation']['summary1']
                summary = ' '.join(summary.split('\n')) 

                passage_values.append(passage)
                summary_values.append(summary)

        data_dict = {'passage':passage_values, 'summary':summary_values}

        return pd.DataFrame(data_dict)
    
    def save_as_file(self):        
        # 데이터프레임을 TSV 파일로 저장
        train_df = self.make_passage_summary_df(self.train_file_path_list)
        test_df = self.make_passage_summary_df(self.test_file_path_list)
        
        train_df.to_csv(".\\news_summary_train_dataset.tsv", index=False, sep='\t')
        test_df.to_csv(f".\\news_summary_test_dataset.tsv", index=False, sep='\t')
        print('데이터 파일 생성 완료')
        

    
        
        
        
        
        
        
        




if __name__ == '__main__':
    datamaker = DataMaker(folder_path='C:\\class_file\\NLP\\프로젝트\\요약데이터셋')
    datamaker.save_as_file()
    

