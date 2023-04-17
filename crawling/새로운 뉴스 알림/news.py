import pandas as pd
def read_data(file_path):
    df = pd.read_csv(file_path)

    return df


def preprocessing(df):
    # 전처리
    return df

def select_topic(df):
    # 토픽 추출
    return ['topic1']

def summarize(df):
    # df['content'] 요약

    df['summarized_text'] = df['content']
    return df['summarized_text']

import telegram
import asyncio
class TelegramManager:
    def __init__(self):
        pass
        
        
    async def init_bot(self):
        self.token = 'Enter telegram_bot api_key'  # 받는게 맞나?
        self.bot = telegram.Bot(self.token)
        self.updates = await self.bot.getUpdates()
        print(self.updates)
        self.chat_id = self.updates[-1].message.chat.id

    async def send_msg(self, text):
        try:
            await self.bot.sendMessage(self.chat_id, text)
        except Exception as e:
            print(e)

        return 





import crawler
if __name__ == '__main__':

    # new_contents = crawler.call_news()

    t_hanlder = TelegramManager()
    t_hanlder.send_msg('test')
    # new_contents['title'].apply(t_hanlder.send_msg)    

class NewsHelper:
    
    def __init__(self) -> None:
        # 데이터 불러오기
        self.df = self.read_data('./news.txt')
        pass

    def read_data(self, file_path):
        df = []
        return df
    
    def preprocessing(self):
        return self.df
    
    def summarize(self):
        return self.df


        

# 뉴스 파일의 전체 로직

## 1. 크롤링한 뉴스기사 데이터를 불러온다.
## 2. 뉴스기사 데이터를 전처리
## 3. 뉴스기사 키워드 추출, 요약
## 4. 텔레그램 혹은 이메일을 통해 사용자에게 발송


# 파일 불러오기 방법 1, 2
# pd.read_csv('/home/ubuntu/workspace/news.csv')

# files = os.listdir('./news')
# '1'

# last_news_number = int(open('./last_csv_file_number').read())

# # for f in files[last_news_number:]:
#     # df에 추가
#     # if int(f.split('.')[0].split('_')[1]) > last_news_number:
#         # df에 추가
# # else:
# #     # last_csv_file_number에 추가
# #     int(f.split('.')[0].split('_')[1])
        

