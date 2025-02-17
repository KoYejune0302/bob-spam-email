import pandas as pd
import random
from faker import Faker
from random import randint, choice

fake = Faker('ko_KR')

# 스팸 키워드 리스트
spam_keywords = ['무료', '당첨', '이벤트', '특가', '혜택', 'VIP', '할인', '수령', '선착순', '비밀번호', '보험', '대출']
ham_keywords = ['회의', '프로젝트', '보고서', '일정', '협업', '팀원', '고객', '검토', '요청', '감사합니다', '문의']

# 메일 생성 함수
def generate_email(is_spam):
    subject = []
    content = []
    
    if is_spam:
        # 스팸 메일 생성
        subject.append('[광고] ')
        for _ in range(randint(1, 3)):
            subject.append(choice(spam_keywords))
        
        content.append(fake.sentence())
        content.append(' '.join([choice(spam_keywords) for _ in range(5)]))
        content.append(fake.url())
        content.append(fake.sentence())
        
    else:
        # 정상 메일 생성
        subject.append('[회의] ' if randint(0,1) else '[안내] ')
        for _ in range(randint(1, 3)):
            subject.append(choice(ham_keywords))
        
        content.append(fake.bs())
        content.append(fake.sentence())
        content.append(fake.name() + '님, ' + fake.sentence())
        content.append(fake.sentence())

    return {
        'text': ' '.join(subject) + ' ' + ' '.join(content),
        'spam': 1 if is_spam else 0
    }

# 데이터 생성 (5000개)
data = [generate_email(is_spam=(i % 2 == 0)) for i in range(1000)]
df = pd.DataFrame(data)

# CSV 저장
df.to_csv('spam_email_generated.csv', index=False)
print("Generated 1000 samples!")