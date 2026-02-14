# Import unittest and emotion_detector in order to create tests
import unittest, json
from EmotionDetection.emotion_detection import emotion_detector

# Create a class using TestCase
class TestEmotionDetector(unittest.TestCase):
    # Create function with 1 test corresponding to each emotion
    # json.loads converts the formatted output string back to a dict
    def test_emotion_detector(self):
        self.assertEqual(
            emotion_detector("I am glad this happened")['dominant_emotion'], 
            'joy'
            )
        self.assertEqual(
            emotion_detector("I am really mad about this")['dominant_emotion'], 
            'anger'
            )
        self.assertEqual(
            emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'], 
            'disgust'
            )
        self.assertEqual(
            emotion_detector("I am so sad about this")['dominant_emotion'], 
            'sadness'
            )
        self.assertEqual(
            emotion_detector("I am really afraid this will happen")['dominant_emotion'], 
            'fear'
            )

# Set up execution of the tests
if __name__ == "__main__":
    unittest.main()