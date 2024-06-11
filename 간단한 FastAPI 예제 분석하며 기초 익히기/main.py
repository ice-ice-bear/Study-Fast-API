from fastapi import FastAPI, HTTPException  # FastAPI 및 HTTPException 모듈을 가져옵니다.
from pydantic import BaseModel  # 데이터 모델을 정의하기 위해 Pydantic의 BaseModel을 가져옵니다.

app = FastAPI()  # FastAPI 애플리케이션 객체를 생성합니다.

class Item(BaseModel):  # Pydantic 모델 정의
    name: str  # 아이템의 이름을 나타내는 문자열 필드
    price: float  # 아이템의 가격을 나타내는 실수 필드
    is_offer: bool = None  # 아이템의 할인가 여부를 나타내는 불리언 필드 (기본값: None)

# 샘플 데이터 딕셔너리
items = {
    1: {"name": "Item One", "price": 10.5},
    2: {"name": "Item Two", "price": 15.0, "is_offer": True},
}

@app.get("/")  # 루트 엔드포인트 정의
def read_root():
    return {"Hello": "World"}  # 루트 경로에 대한 요청에 "Hello": "World"를 반환합니다.

@app.get("/items/{item_id}", response_model=Item)  # 아이템 조회 엔드포인트 정의
async def read_item(item_id: int):
    if item_id not in items:  # 요청한 아이템 ID가 items 딕셔너리에 없는 경우
        raise HTTPException(status_code=404, detail="Item not found")  # HTTP 404 에러 발생
    return items[item_id]  # 요청한 아이템 ID가 있는 경우 해당 아이템을 반환

@app.post("/items/", response_model=Item)  # 아이템 생성 엔드포인트 정의
async def create_item(item: Item):
    next_id = max(items.keys()) + 1  # 새로운 아이템의 ID를 설정 (현재 최대 ID + 1)
    items[next_id] = item  # 새로운 아이템을 items 딕셔너리에 추가
    return item  # 생성된 아이템을 반환
