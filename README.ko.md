# 🛰️ SmartBeam: 실시간 객체 추적 및 프로젝션 시스템

📘 [English](README.md) | 🇰🇷 [한국어](README.ko.md)

SmartBeam은 Python 기반 YOLOv11 인스턴스 세분화 모델을 활용하여 실시간으로 객체의 중심 좌표를 추적하고, 이를 WebSocket을 통해 Unity로 전송하는 시스템입니다. Unity에서는 이 좌표를 기반으로 사물 위에 영상을 정렬하여, *Le Petit Chef*와 같은 자연스러운 프로젝션 매핑 효과를 구현합니다.

---

## 🏢 회사 소개

SmartBeam은 **CSI Vision**에서 개발 및 유지보수하고 있습니다.  
CSI Vision은 실시간 공간 컴퓨팅, 프로젝션 매핑, 컴퓨터 비전 기술에 특화된 기업입니다.

협업 및 문의는 [js.lee@csi-vision.com](mailto:js.lee@csi-vision.com) 으로 연락주시기 바랍니다.

---

## 📁 프로젝트 구조

.
├── config.py
├── detector.py
├── logger.py
├── main.py
├── utils.py
└── websocket_server.py

yaml
Copy
Edit

---

## 🔧 파일 설명

### `main.py`
시스템의 **메인 실행 파일**입니다.  
- WebSocket 서버와 객체 감지 루프를 스레드로 병렬 실행합니다.
- 전체 모듈들을 조율합니다.

### `config.py`
시스템 상수를 정의하는 **설정 파일**입니다.  
- `ALLOWED_CLASSES`: "bowl", "clock" 등 COCO 클래스
- `MODEL_PATH`: YOLOv11 세분화 모델 경로
- `CAMERA_ID`: OpenCV에서 사용할 카메라 인덱스

### `detector.py`
**YOLOv11 기반 객체 탐지 모듈**입니다.  
- OpenCV를 이용해 프레임을 캡처합니다.
- YOLOv11로 객체 세분화를 수행합니다.
- 마스크에서 중심 좌표를 추출합니다.
- Unity로 전송할 좌표를 큐에 저장합니다.

### `websocket_server.py`
`websockets`와 `asyncio` 기반의 **WebSocket 서버**입니다.  
- Unity에서 들어오는 클라이언트 연결을 수신합니다.
- 객체 좌표를 실시간으로 전송합니다.

### `utils.py`
**도우미 함수 모음**입니다.  
- 바이너리 마스크에서 중심 좌표를 계산합니다.
- 디버깅용 시각화 기능 포함

### `logger.py`
**간단한 로깅 유틸리티**입니다.  
- 표준화된 로그 출력을 제공합니다.

---

## 🔁 시스템 흐름 요약

1. **Python 측**:
   - YOLOv11 모델이 웹캠 영상에서 객체 세분화를 수행합니다.
   - 각 객체의 중심 좌표를 계산합니다.
   - WebSocket을 통해 좌표를 전송합니다.

2. **Unity 측**:
   - Python으로부터 좌표를 수신합니다.
   - 객체 위치에 맞게 영상을 정렬하여 투사합니다.

---

## 🧠 사용 예시

SmartBeam은 다음과 같은 환경에 적합합니다:
- 테이블 위에 프로젝션이 연동되는 레스토랑
- 실물 소품과 상호작용하는 증강 현실 콘텐츠
- 정밀 정렬이 필요한 프로젝션 맵핑 데모

---

## 🔌 요구사항

- Python 3.9 이상
- OpenCV
- `ultralytics` (YOLOv11 지원)
- `websockets` 라이브러리
- WebSocket 수신 기능을 포함한 Unity 프로젝트

---

## 🚀 실행 방법

```bash
pip install -r requirements.txt
python main.py