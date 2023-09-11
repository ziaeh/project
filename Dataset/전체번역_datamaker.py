from tqdm import tqdm
import pandas as pd
import os

##########################################################################################

class Datamaker():

    def __init__(self, FOLDER_PATH, SAVE_PATH):
        # 경로
        self.FOLDER_PATH = FOLDER_PATH
        self.SAVE_PATH = SAVE_PATH

        self.file_name_list = os.listdir(self.FOLDER_PATH)


    def extract_columns(self, save=False):
        """ 원본 xlsx 파일에서 필요한 컬럼을 추출하여 csv로 저장하는 함수 """

        for idx, file_name in enumerate(tqdm(self.file_name_list)):
            # xlsx 파일 불러오기
            df = pd.read_excel(os.path.join(self.FOLDER_PATH, file_name), engine='openpyxl')
            # 특정 컬럼 추출
            extract_columns = df[['원문', '번역문']]

            # 저장 여부
            if save: 
                extract_columns.to_csv(os.path.join(self.SAVE_PATH, f'extracted_cols_{idx+1}_file.csv'), index=False)
                print(f'{file_name} csv로 저장 완료')


    def concat_csv(self, shuffle=False):
        """ 위에서 추출된 csv를 concat하는 함수 """

        # 빈 DataFrame을 생성
        combined_df = pd.DataFrame()
        # csv 불러올 경로
        csv_file_list = os.listdir(self.SAVE_PATH)

        for file_name in csv_file_list:
            # csv 파일 불러오기
            df = pd.read_csv(os.path.join(self.SAVE_PATH, file_name))
            # csv concat하기
            combined_df = pd.concat([combined_df, df], ignore_index=True)

        # suffle 여부
        if shuffle:
            # 무작위로 suffle하기
            combined_df = combined_df.sample(frac = 1, random_state = 42)
            # 새로운 무작위 순서로 인덱스를 다시 설정
            combined_df = combined_df.reset_index(drop = True)

        # 결과를 CSV 파일로 저장
        combined_df.to_csv(os.path.join(self.SAVE_PATH, 'concated_dataframe.csv'), index=False, encoding='utf-8')
        print('shuffle된 csv 저장 완료')

    def slicing_csv(self,  slicing_num = 0):
        """ concat한 csv를 slicing하여 사용할 데이터셋을 나누는 함수 """
        file_name = input("슬라이싱할 csv명을 입력하시오(확장자 표현) >> ")
        df = pd.read_csv(os.path.join(self.SAVE_PATH, file_name))

        # 설정한 slicing_num만큼 슬라이싱
        sliced_df = df[:slicing_num]

        # 결과를 CSV 파일로 저장
        sliced_df.to_csv(os.path.join(self.SAVE_PATH, 'sliced_dataframe.csv'), index=False, encoding='utf-8')
        print('shuffle된 csv 저장 완료')



##########################################################################################
# 해당 py파일 실행 시 전체 원본 excel파일을 concat-> shuffle -> 8만개 행만 뽑아 csv file로 변환해줌ㅋ 
if __name__ == "__main__":

    # 변수 설정
    FOLDER_PATH = 'data/korean_english_dataset/original/'
    SAVE_PATH = 'data/korean_english_dataset/new/'

    # 객체 생성
    dk = Datamaker(FOLDER_PATH, SAVE_PATH)

    # 객체내 함수 실행
    dk.extract_columns(save=True)
    dk.concat_csv(shuffle=True)
    dk.slicing_csv(slicing_num = 800000)
