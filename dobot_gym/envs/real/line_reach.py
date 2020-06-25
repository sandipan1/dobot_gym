from dobot_gym.envs import DobotCamRealEnv
import numpy as np

## 480 640 3
class LineReachEnvCam(DobotCamRealEnv):
    def __init__(self, camera_port_left=1, scale_reward=0.5):
        super().__init__(camera_port_left=camera_port_left)
        self.scale_reward = scale_reward

    def compute_reward(self, image, centroid):
        im, centroid = self.get_image(centroid=True)
        cY = centroid[1]
        print(im.shape)
        bias= -10
        reward = self.scale_reward * cY + bias
        return reward


