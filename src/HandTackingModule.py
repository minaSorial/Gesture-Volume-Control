import time
import cv2
import mediapipe as mp


class HandDetector:
    """
    A class to detect and track hands using MediaPipe's Hands solution.
    """

    def __init__(self, mode=False, max_hands=2, detection_conf=0.5, tracking_conf=0.5):
        """
        Initializes the HandDetector.
        :param mode: Whether to treat images as static.
        :param max_hands: Maximum number of hands to detect.
        :param detection_conf: Minimum confidence for hand detection.
        :param tracking_conf: Minimum confidence for tracking.
        """
        self.mode = mode
        self.max_hands = max_hands
        self.detection_conf = detection_conf
        self.tracking_conf = tracking_conf

        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=self.mode,
                                         max_num_hands=self.max_hands,
                                         min_detection_confidence=self.detection_conf,
                                         min_tracking_confidence=self.tracking_conf)

        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):
        """
        Detects hands in an image.
        :param img: Input image.
        :param draw: Whether to draw landmarks.
        :return: Processed image with landmarks drawn.
        """
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return img

    def find_position(self, img, hand_number=0, draw=True):
        """
        Finds the position of hand landmarks.
        :param img: Input image.
        :param hand_number: Index of the hand to track.
        :param draw: Whether to draw the points.
        :return: List of landmark positions.
        """
        landmark_list = []
        h, w, _ = img.shape
        if self.results.multi_hand_landmarks:
            selected_hand = self.results.multi_hand_landmarks[hand_number]
            for id, landmark in enumerate(selected_hand.landmark):
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                landmark_list.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 255, 255), cv2.FILLED)
        return landmark_list


def main():
    """
    Main function to run hand tracking using webcam.
    """
    p_time = 0
    capture = cv2.VideoCapture(0)
    detector = HandDetector(mode=False, max_hands=2, detection_conf=0.5, tracking_conf=0.5)

    while True:
        success, img = capture.read()
        if not success:
            break

        img = detector.find_hands(img)
        landmark_list = detector.find_position(img)
        if landmark_list:
            print(landmark_list[4])  # Example: printing the position of the index finger tip

        # Calculate and display FPS
        c_time = time.time()
        fps = 1 / (c_time - p_time)
        p_time = c_time

        cv2.putText(img, f"FPS: {int(fps)}", (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 4)
        cv2.imshow("Hand Tracking", img)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
