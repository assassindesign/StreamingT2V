# These codes are copied from modelscope revision c58451baead80d83281f063d12fb377fad415257 
"""
The implementation here is modified based on insightface, originally MIT license and publicly available at
https://github.com/deepinsight/insightface/tree/master/detection/scrfd/mmdet/core/bbox
"""
from .transforms import bbox2result, distance2kps, kps2distance

__all__ = ['bbox2result', 'distance2kps', 'kps2distance']