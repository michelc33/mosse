import cv2
import numpy as np

# Initialize the MOSSE tracker
class MOSSE:
    def __init__(self, frame, rect):
        x, y, w, h = rect
        self.pos = (x + w // 2, y + h // 2)
        self.size = (w, h)
        self.win = cv2.createHanningWindow((w, h), cv2.CV_64F)
        self.G = self.preprocess(cv2.getRectSubPix(frame, (w, h), self.pos))
        self.H1 = np.zeros_like(self.G)
        self.H2 = np.zeros_like(self.G)
        self.update(frame, rect)

    def preprocess(self, img):
        img = np.log(np.float32(img) + 1.0)
        img = (img - np.mean(img)) / (np.std(img) + 1e-5)
        return img * self.win

    def update(self, frame, rect):
        x, y, w, h = rect
        self.pos = (x + w // 2, y + h // 2)
        img = cv2.getRectSubPix(frame, (w, h), self.pos)
        A = cv2.dft(self.preprocess(img), flags=cv2.DFT_COMPLEX_OUTPUT)
        self.H1 += cv2.mulSpectrums(self.G, A, 0, conjB=True)
        self.H2 += cv2.mulSpectrums(A, A, 0, conjB=True)
        self.H = self.H1 / (self.H2 + 1e-5)

    def detect(self, frame):
        img = cv2.getRectSubPix(frame, self.size, self.pos)
        A = cv2.dft(self.preprocess(img), flags=cv2.DFT_COMPLEX_OUTPUT)
        R = cv2.mulSpectrums(A, self.H, 0, conjB=True)
        resp = cv2.idft(R, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
        _, max_val, _, max_loc = cv2.minMaxLoc(resp)
        self.pos = (self.pos[0] + max_loc[0] - self.size[0] // 2,
                    self.pos[1] + max_loc[1] - self.size[1] // 2)
        return self.pos

# Main function to run the tracker
def main():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture video")
        return

    # Select ROI
    rect = cv2.selectROI("Frame", frame, fromCenter=False, showCrosshair=True)
    tracker = MOSSE(frame, rect)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        pos = tracker.detect(frame)
        x, y = int(pos[0] - tracker.size[0] // 2), int(pos[1] - tracker.size[1] // 2)
        w, h = tracker.size
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()