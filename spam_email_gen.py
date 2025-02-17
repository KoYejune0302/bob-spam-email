import random
import datetime

# Expanded templates for subjects and bodies of spam emails in Korean.
spam_subject_templates = [
    "당첨 축하합니다!",
    "긴급: 귀하의 계정이 정지되었습니다",
    "무료 혜택: 오늘만 한정!",
    "투자 제안: 높은 수익 보장!",
    "특별 할인: 단 하루!",
    "행운의 기회: 지금 바로 클릭하세요",
    "중요 알림: 보안 업데이트 필요",
    "지금 확인: 당신을 위한 특별 혜택"
]

spam_body_templates = [
    "안녕하세요, {name}님. 당신은 {prize} 당첨되었습니다! 지금 바로 {link}을(를) 클릭하세요.",
    "경고: 귀하의 계정에서 의심스러운 활동이 감지되었습니다. 즉시 {link}을(를) 방문하여 확인하십시오.",
    "무료 제품 증정 행사에 참여하세요! {link}에서 지금 신청하면 {discount} 할인을 받을 수 있습니다.",
    "안전한 거래를 보장합니다. {link}에서 자세한 내용을 확인하시고, {offer}에 참여해 보세요.",
    "당신의 건강과 안전을 위해 특별한 혜택을 준비했습니다. {link}를 방문하여 {offer}를 확인해보세요.",
    "지금 등록하면 추가 혜택이 기다리고 있습니다. {link}을(를) 방문하여 {offer}을(를) 신청하세요.",
    "보안 경고: 귀하의 정보가 유출되었습니다. 즉시 {link}에 접속하여 계정을 보호하십시오."
]

# Sample data for placeholders.
names = ["김철수", "이영희", "박민수", "최지훈", "홍길동", "정수진", "오민석"]
prizes = ["대박", "특별", "놀라운", "행운", "상금"]
discounts = ["50%", "70%", "30%", "80%"]
offers = ["특별 제안", "한정 할인", "즉시 지원", "VIP 멤버십", "무료 체험"]

def generate_random_spam_email():
    """
    Generates a single synthetic spam email.
    Returns:
        dict: A dictionary with keys 'sender', 'subject', 'body', and 'date'.
    """
    subject = random.choice(spam_subject_templates)
    body_template = random.choice(spam_body_templates)
    
    # Randomly select values for placeholders.
    name = random.choice(names)
    prize = random.choice(prizes)
    discount = random.choice(discounts)
    offer = random.choice(offers)
    # Generate a pseudo-random link (not functional)
    link = f"http://spam.example.com/{random.randint(1000, 9999)}"
    
    body = body_template.format(name=name, prize=prize, link=link, discount=discount, offer=offer)
    sender = f"noreply{random.randint(100, 999)}@example.com"
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    return {
        "sender": sender,
        "subject": subject,
        "body": body,
        "date": date
    }

def generate_spam_dataset(n):
    """
    Generates a list of synthetic spam emails.
    Args:
        n (int): Number of spam emails to generate.
    Returns:
        list: A list of dictionaries, each representing a spam email.
    """
    return [generate_random_spam_email() for _ in range(n)]

if __name__ == "__main__":
    # Generate a dataset of 20 synthetic spam emails.
    dataset = generate_spam_dataset(20)
    
    # Print out each spam email.
    for email in dataset:
        print("Sender:", email["sender"])
        print("Date:", email["date"])
        print("Subject:", email["subject"])
        print("Body:", email["body"])
        print("-" * 40)
