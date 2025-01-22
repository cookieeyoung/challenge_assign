#코드 공유 및 재사용 파이썬 스크립트 

import seaborn as sns

def get_tips():
    tips = sns.load_dataset('tips')
    return tips

#name: 파일명 , main: 파일 -> 항상 true 처리가 됨, 스크립트에서만 자동 실행 됨. 
if __name__ == '__main__':
    get_tips()


