import cv2
import mediapipe as mp
import pyautogui

class cvmodel:
    def __init__(self):
        pass

    def run(self):
        mp_holistic = mp.solutions.holistic
        mp_hands = mp.solutions.hands
        cap = cv2.VideoCapture(0)
        charac_pos = [0,1,0]
        index_pos = 1

        rec = True
        with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
            with mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) as holistic:
                while True:
                    success, frame = cap.read()
                    frame = cv2.flip(frame, 1)
                    frame = cv2.resize(frame, (440,330))
                    height, width, channel = frame.shape
                    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    results_holistic = holistic.process(img)
                    results_hands = hands.process(img)
                    img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
                    width_hf = int(width/2)
                    height_hf = int(height/2)
                    # Extracting Shoulder Landmarks
                    if results_holistic.pose_landmarks:
                        right_x = int(results_holistic.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_SHOULDER].x * width)-7
                        right_y = int(results_holistic.pose_landmarks.landmark[mp_holistic.PoseLandmark.LEFT_SHOULDER].y * height)

                        left_x = int(results_holistic.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_SHOULDER].x * width)+7
                        left_y = int(results_holistic.pose_landmarks.landmark[mp_holistic.PoseLandmark.RIGHT_SHOULDER].y * height)

                        mid_x = left_x + int(abs(right_x - left_x) / 2)
                        mid_y = int(abs(right_y + left_y) / 2)

                        if rec != None:
                            # Sideways movement command
                            if right_x < width_hf and index_pos > 0 and charac_pos[index_pos-1] == 0:
                                charac_pos[index_pos] = 0
                                charac_pos[index_pos-1] = 1
                                pyautogui.press('left')
                                index_pos -= 1
                                print("Left key")
                                print(charac_pos)
                            if left_x > width_hf and index_pos < 2 and charac_pos[index_pos+1] == 0:
                                print("Right key")
                                charac_pos[index_pos] = 0
                                charac_pos[index_pos+1] = 1
                                pyautogui.press('right')
                                index_pos += 1
                                print(charac_pos)
                            if right_x > width_hf and left_x < width_hf and index_pos == 0:
                                charac_pos[index_pos] = 0
                                charac_pos[index_pos +1] = 1
                                index_pos += 1
                                pyautogui.press('right')
                                print(charac_pos)
                                print('left to center')
                            if right_x > width_hf and left_x < width_hf and index_pos == 2:
                                charac_pos[index_pos] = 0
                                charac_pos[index_pos -1] = 1
                                index_pos -= 1
                                pyautogui.press('left')
                                print('right to center')
                                print(charac_pos)

                    # cv2.waitKey(1)