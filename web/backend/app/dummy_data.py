from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


dummy_users = [
    {
        "id": 1000,
        "name": "taro",
        "grade": "normal",
        "introduction": "hello from taro.",
        "hashed_password": get_password_hash("aaa"),
    },
    {
        "id": 2000,
        "name": "jiro",
        "grade": "advance",
        "introduction": "hello from jiro.",
        "hashed_password": get_password_hash("aaa"),
    },
    {
        "id": 3000,
        "name": "ken",
        "grade": "beginner",
        "introduction": "hello from ken.",
        "hashed_password": get_password_hash("aaa"),
    },
]

dummy_jobs = [
    {
        "id":1000,
        "user_id":3000,
        "title": "job1000",
        "description": "this is job1000.",
        "place": "honkan",
        "reawrd_money": 10000,
        "reward_item": "game",
        "status": "done",
        "time_required": 30000,
    },
    {
        "id":2000,
        "user_id":1000,
        "title": "job2000",
        "description": "this is job2000.",
        "place": "wonagan",
        "reawrd_money": 30000,
        "reward_item": "game2000",
        "status": "inprogress",
        "time_required": 300,
    },
    {
        "id":3000,
        "user_id":1000,
        "title": "job3000",
        "description": "this is job3000.",
        "place": "inmunkan",
        "reawrd_money": 300,
        "reward_item": "bingo",
        "status": "preparing",
        "time_required": 30004,
    }
]

dummy_transactions = [
    {
        "id": 1000,
        "send_user_id": 2000,
        "receive_user_id": 3000,
    },
    {
        "id": 2000,
        "send_user_id": 2000,
        "receive_user_id": 3000,
    },
    {
        "id": 3000,
        "send_user_id": 3000,
        "receive_user_id": 1000,
    },
]
