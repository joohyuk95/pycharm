import cv2
import numpy as np

device = 'http://172.30.1.47:4747/video'
cap = cv2.VideoCapture(device)
whT = 320           # target image size 320x, 416x, 608 possible

confThreshold_1 = 0.5
confThreshold_2 = 0.7
nmsThreshold = 0.3

classesFile = './coco.names'
    # 텍스트가 한줄씩 띄어서 이름이 적혀있음
with open(classesFile, 'rt') as f:      # 읽기모드로 파일열기
    classNames = f.read().split('\n')  # 파일을 읽는데, 줄바꿈 삭제하고 줄바꿈 기준으로 문자열을 분리해서 리스트 형태로 저장

model_config = './yolov3-tiny.cfg'
model_weights = './yolov3-tiny.weights'

# readNetFromDarknet은 yolo만을 위한 Framework, net 객체 생성
net = cv2.dnn.readNetFromDarknet(model_config, model_weights)   # network는 neural network를 의미
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

def findObjects(outputs, img):
    hT, wT, cT = img.shape
    bbox = []
    classIds = []
    confs = []
    # 모든 output 중에서 확률이 50 % 넘는 것들만 모으는 반복문
    for output in outputs:      # output data form [ cx, cy, w, h, conf, (80 probabilities) ] total 85 elements
        for det in output:      # outputs has three elements, output has 85 elements
            scores = det[5:]    # scores mean 80 probabilities
            classId = np.argmax(scores)     # np.argmax는 인자의 원소중 가장 큰 값의 인덱스를 반환한다.
            confidence = scores[classId]    # 가장 높은 확률을 가지는 class의 확률을 confidence 라 칭함
            if confidence > confThreshold_1:  # 확률이 0.5가 넘지 않으면 무시
                w, h = int(det[2]*wT), int(det[3]*hT)   # 너비, 높이가 십진수로 표현되어있음 픽셀로 맞추려면 곱해줘야됨 정수형으로
                x, y = int((det[0]*wT) - w/2), int((det[1]*hT) - h/2)
                bbox.append([x, y, w, h])   # 바운딩 박스에 높은 확률의 박스 정보를 리스트 형태로 저장
                classIds.append(classId)    # 그놈의 인덱스를 저장
                confs.append(float(confidence))     # 그놈의 확률을 부동 소수점 형태로 저장
    # print(len(bbox))        # 포착된 대상의 수를 출력
    indices = cv2.dnn.NMSBoxes(bbox, confs, confThreshold_2, nmsThreshold)    # 1000개 가량의 박스가 겹칠수 있음 하나 냄기고 삭제 목적
    print(f"식별된 대상 : {len(indices)} 개")
    # None Maximum Suppression
    # nmsThreshold 는 IOU (Intersection of Union)

    for i in indices:   # nms 함수로 걸러진 놈들 리스트
        i = i[0]        # 2차원 리스트 알맹이
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)    # img 에다가 시작점, 끝점, 보라색, 두꼐 : 2
        cv2.putText(img, f'{classNames[classIds[i]].upper()} {int(confs[i]*100)}%',
                    (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)  # 박스 좌상단에 표시
                    # 문자열 출력
                    # img, text, 시작위치, 폰트, 크기, 색, 굵기

while True:
    success, img = cap.read()

    if not success:
        break

    blob = cv2.dnn.blobFromImage(img, 1 / 255, (whT, whT), [0, 0, 0], True, crop=False)  # dnn 에 맞게 이미지 전처리
    # binary large object 주로 이미지, 비디오, 사운드 같은 큰 객체를 이진으로 저장할때 사용
    # blobFromImage(image, scalefactor, size, mean, swapRB, crop)
    # 처리할이미지, 채도 값 변환 계수, 변환할 크기, 채도 평균값으로 낮추기, BGR,RGB 전환, 크기 변환할 때 짜를지 말지
    net.setInput(blob)      # input 을 전처리된 blob으로 넣음

    layerNames = net.getLayerNames()

    outputNames = [layerNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    outputs = net.forward(outputNames)

    findObjects(outputs, img)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == 27:       # esc 누르면 나가기
        break