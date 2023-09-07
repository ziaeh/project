import  numpy as np
from glob import glob
import json
import pandas as pd
from sklearn.model_selection import train_test_split

class DataMaker():

    def __init__(self, folder_path, request_data_list, data_type):
        
        self.folder_path = folder_path
        self.data_type = data_type
        self.request_data_list = request_data_list
        self.data_tag = {
            0:('Meta(Acqusition)','doc_name'),
            1:('Meta(Acqusition)','author'),
            2:('Meta(Acqusition)','publisher'),
            3:('Meta(Acqusition)','publisher'),
            4:('Meta(Acqusition)','publisher_year'),
            5:('Meta(Acqusition)','doc_origin'),
            6:('Meta(Refine)','passage'), 
            7:('Annotation','summary1')
        }
        self.file_path_list = self.get_path_list()
        self.passage_summary_df = self.get_request_data()

        
    def get_path_list(self):
        
        file_path_list = glob(self.folder_path + "\\**\\*.json", recursive=True)
        return file_path_list 
    
    def get_request_data(self):
        '''
        아래의 data_tag에 따라서 숫자 리스트로 데이터를 요청받고,
        요청 받은 데이터 중 summary와 그 외의 데이터를 구분해서
        summary와, \t을 기준으로 하나의 텍스트로 combine한 그 외의 데이터를
        각 'summary', 'passage'라는 이름의 컬럼으로 가지는 데이터프레임을 반환하는 함수

        data_tag 딕셔너리에서 6('passage'),7('summary')은 필수

        data_tag = {
        0:('Meta(Acqusition)','doc_name'),
        1:('Meta(Acqusition)','author'),
        2:('Meta(Acqusition)','publisher'),
        3:('Meta(Acqusition)','publisher'),
        4:('Meta(Acqusition)','publisher_year'),
        5:('Meta(Acqusition)','doc_origin'),
        6:('Meta(Refine)','passage'), 
        7:('Annotation','summary1')
    }
        '''
        passage_values = []
        summary_values = []

        for file_path in self.file_path_list:

            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

                passage = ''

                for request in self.request_data_list:
                    tag1, tag2 = self.data_tag[request]

                    if request == 7: #summary
                        summary = data[tag1][tag2]
                    else: #summary 제외 모든 컬럼들 \t으로 구분해서 합치기
                        passage += (data[tag1][tag2] + '\t')

            passage_values.append(passage)
            summary_values.append(summary)

        request_data_dict = {'passage':passage_values, 'summary':summary_values}

        return pd.DataFrame(request_data_dict)
    
    def dict_to_file(self):        
        # 데이터프레임을 TSV 파일로 저장
        self.passage_summary_df.to_csv(f".\\news_summary_dataset_{self.data_type}.tsv", index=False, sep='\t')
        print('데이터 파일 생성 완료')
        
        
        
        
        
        
        
#train
if __name__ == '__main__':
    dataloader = DataMaker(folder_path='C:\\class_file\\NLP\\프로젝트\\요약학습데이터셋', request_data_list = [6,7], data_type='train')
    dataloader.dict_to_file()

#test  
if __name__ == '__main__':
    dataloader = DataMaker(folder_path='C:\\class_file\\NLP\\프로젝트\\요약테스트데이터셋', request_data_list = [6,7], data_type='test')
    dataloader.dict_to_file()


len(dataloader.file_path_list)