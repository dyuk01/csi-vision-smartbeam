# 🛰️ SmartBeam: 실시간 객체 추적 및 프로젝션 시스템

📘 [English](README.md) | 🇰🇷 [한국어](README.ko.md)

SmartBeam은 Python에서 YOLOv11 인스턴스 분할을 사용하는 실시간 객체 추적 파이프라인으로, 객체 좌표(예: 접시, 그릇, 시계)를 WebSocket을 통해 Unity로 전송하도록 설계되었습니다. Unity는 이러한 좌표를 사용하여 투영된 애니메이션이나 비디오를 정렬하여 Le Petit Chef와 유사한 매끄러운 프로젝션 매핑 효과를 만들어냅니다.

---

## 🏢 회사 소개
SmartBeam은 실시간 공간 컴퓨팅, 프로젝션 매핑, 컴퓨터 비전 솔루션에 전문화된 **CSI Vision**에서 개발 및 유지보수됩니다.
문의사항이나 협업 기회에 대해서는 [js.lee@csi-vision.com](mailto:js.lee@csi-vision.com)으로 연락하시기 바랍니다.

---

## 📁 프로젝트 구조
.
├── config.py
├── detector.py
├── logger.py
├── main.py
├── utils.py
└── websocket_server.py

---

## 🔧 파일 설명
main.py
시스템의 메인 진입점.

스레딩을 사용하여 WebSocket 서버와 감지 루프를 병렬로 시작합니다.
시스템의 모든 구성 요소를 조정합니다.

config.py
시스템 상수를 정의하는 구성 파일.

ALLOWED_CLASSES: "bowl", "clock" 등과 같은 COCO 클래스들.
MODEL_PATH: YOLOv11 분할 모델의 경로.
CAMERA_ID: OpenCV 호환 카메라 인덱스.

detector.py
YOLOv11 기반 객체 감지 모듈.

OpenCV를 통해 프레임을 캡처합니다.
YOLOv11 분할을 실행합니다.
분할 마스크에서 중심점을 추출합니다.
Unity를 위한 공유 큐에 좌표를 전송합니다.

websocket_server.py
websockets와 asyncio를 사용하는 WebSocket 서버.

Unity 클라이언트 연결을 수신합니다.
WebSocket을 통해 실시간 좌표를 전송합니다.

utils.py
도우미 함수들:

이진 마스크에서 중심점 계산.
디버깅을 위한 시각화.

logger.py
최소한의 로깅 유틸리티.

표준화된 로그 메시지를 제공합니다.


🔁 워크플로우 요약

Python 측:

YOLOv11이 웹캠 입력에서 분할을 수행합니다.
객체의 중심점을 계산합니다.
WebSocket을 통해 객체 위치를 전송합니다.


Unity 측:

Python에서 좌표를 수신합니다.
객체의 위치에 맞춰 투영된 비디오를 업데이트합니다.




🧠 사용 사례
SmartBeam은 다음과 같은 용도에 이상적입니다:

인터랙티브 프로젝션 테이블이 있는 레스토랑.
물리적 소품을 사용하는 증강 현실 경험.
높은 정밀도가 필요한 프로젝션 매핑 데모.


🔌 요구사항

Python 3.9+
OpenCV
ultralytics (YOLOv11 지원)
websockets
WebSocket 수신기가 있는 Unity 프로젝트


📦 YOLOv11 모델 다운로드
이 프로젝트를 실행하려면 YOLOv11 인스턴스 분할 모델이 필요합니다.

사전 훈련된 모델을 다운로드하세요:
yolo11n-seg.pt
(또는 원한다면 자체 훈련된 .pt 모델을 사용하세요)
모델 파일을 프로젝트 루트에 배치하거나 config.py에서 MODEL_PATH를 적절히 업데이트하세요:

pythonMODEL_PATH = "yolo11n-seg.pt"

🚀 실행 지침
bashpip install -r requirements.txt
python main.py
실시간 좌표를 받기 위해 Unity 씬이 열려 있고 WebSocket 데이터를 수신하고 있는지 확인하세요.