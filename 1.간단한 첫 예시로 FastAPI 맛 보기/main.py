from fastapi import FastAPI  # FastAPI 모듈을 가져옵니다.

app = FastAPI()  # FastAPI 애플리케이션 객체를 생성합니다.

@app.get("/")  # HTTP GET 메서드로 루트 경로(/)에 대한 요청을 처리하는 함수를 정의합니다.
def read_root():
    return {"Hello": "World"}  # 요청을 받으면 {"Hello": "World"}라는 JSON 형식의 응답을 반환합니다.
