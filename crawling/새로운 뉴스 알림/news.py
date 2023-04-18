import pandas as pd
def read_data(file_path):

    return pd.read_csv(file_path)

def preprocessing(df):
    # 전처리
    # return df
    pass

def select_topic(df):
    flags = (df['content'].str.contains('gpt')) | (df['content'].str.contains('GPT')) |\
         (df['content'].str.contains('챗')) | (df['content'].str.contains('자연어'))

    return df[flags].reset_index(drop=True)
    

def summarize(df):
    # df['content'] 요약
    # return df['summarized_text']
    pass


import telegram
import asyncio
class TelegramManager:
    def __init__(self):
        pass
        
        
    async def init_bot(self):
        self.token = '5862624931:AAHso-IJuewiTCE_DoRz5IQBY6Qu595Ra8g'  # 받는게 맞나?
        self.bot = telegram.Bot(self.token)
        self.updates = await self.bot.getUpdates()
        self.chat_id = self.updates[-1].message.chat.id

    async def send_msg(self, text):
        try:
            await self.bot.sendMessage(self.chat_id, text)
        except Exception as e:
            print(e)

        return 

async def init_telegram():
    bot = TelegramManager()

    await bot.init_bot()

    return bot

async def send_msg(bot, topics):
    print('PUSH Telegram : ', len(topics))
    for idx, row in topics.iterrows():
        msg = '[' + row['main_category'] + '-' + row['sub_category'] + ']' + '\n' + row['title'] + '(' +row['writed_at']+ ')s'
        await bot.send_msg(msg)


import crawler
if __name__ == '__main__':

    new_contents = read_data('./news.csv')

    # 키워드 뉴스 뽑아내기
    topics = select_topic(new_contents)
    print('GPT ARTICLE : ', len(topics))
    # 전처리
    # topics = preprocessing(topics)

    # # 요약
    # summarize = summarize(topics)

    # 텔레그램
    loop = asyncio.get_event_loop()
    push_article = loop.run_until_complete(init_telegram())

    loop.run_until_complete(send_msg(push_article, topics))
    loop.close()


   