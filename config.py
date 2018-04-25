from easydict import EasyDict
import numpy as np
from mxnet import gluon as gl

cfg = EasyDict()

cfg.DATA_DIR = './data'
cfg.TRAIN_RATE = 0.9

cfg.CATEGORY = ['blouse', 'skirt', 'outwear', 'dress', 'trousers']
cfg.NUM_LANDMARK = 24
cfg.LANDMARK_IDX = {
    'blouse': [0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14],
    'skirt': [15, 16, 17, 18],
    'outwear': [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
    'dress': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 17, 18],
    'trousers': [15, 16, 19, 20, 21, 22, 23],
}
cfg.LANDMARK_SWAP = [(0, 1), (3, 4), (5, 6), (10, 12), (9, 11), (7, 8), (13, 14), (15, 16), (17, 18), (21, 23), (20, 22),]
cfg.PAF_LANDMARK_PAIR = [(0, 1), (0, 2), (0, 3),
                         (1, 2), (1, 4),
                         (2, 5), (2, 6),
                         (3, 5), (3, 10),
                         (4, 6), (4, 12),
                         (5, 6), (5, 7), (5, 9), (5, 13),
                         (6, 8), (6, 11), (6, 14),
                         (7, 8), (7, 13),
                         (8, 14),
                         (9, 10),
                         (11, 12),
                         (13, 14),
                         (15, 16), (15, 17), (15, 19), (15, 21),
                         (16, 18), (16, 19), (16, 23),
                         (17, 18),
                         (19, 20), (19, 22),
                         (20, 21),
                         (22, 23),]

cfg.HEATMAP_THRES = 1
cfg.CROP_SIZE = 368
cfg.ROT_MAX = 40
cfg.SCALE_MIN_RATE = 0.6
cfg.SCALE_MAX_RATE = 1.2
cfg.CROP_CENTER_OFFSET_MAX = 40

cfg.FEAT_STRIDE = 16
#cfg.DET_SCALES = [2, 4, 8, 16]
cfg.DET_SCALES = [5, 10, 20]
cfg.DET_RATIOS = [1, 0.5, 2]


cfg.PIXEL_MEAN = [0.485, 0.456, 0.406]  # RGB
cfg.PIXEL_STD = [0.229, 0.224, 0.225]

cfg.BACKBONE_v2 = {
    'vgg16': (gl.model_zoo.vision.vgg16, 'relu8_fwd', ['conv0', 'conv1', 'conv2', 'conv3']),
    'vgg19': (gl.model_zoo.vision.vgg19, 'relu9_fwd', ['conv0', 'conv1', 'conv2', 'conv3']),
    'resnet50': (gl.model_zoo.vision.resnet50_v1, 'stage2_activation3', ['conv0']),
}

cfg.BACKBONE_v3 = {
    'resnet50': (gl.model_zoo.vision.resnet50_v1, ['stage1_activation2', 'stage2_activation3', 'stage3_activation5'], ['conv0']),
}

cfg.BACKBONE_v4 = {
    'vgg19': (gl.model_zoo.vision.vgg19, 'relu9_fwd', ['conv0', 'conv1', 'conv2', 'conv3']),
    'resnet50': (gl.model_zoo.vision.resnet50_v1, 'stage2_activation3', ['conv0']),
}

cfg.BACKBONE_Det = {
    'resnet50': (gl.model_zoo.vision.resnet50_v1, 'stage3_activation5', ['conv0']),
}

cfg.EVAL_NORMAL_IDX = {
    'blouse': (5, 6),
    'skirt': (15, 16),
    'outwear': (5, 6),
    'dress': (5, 6),
    'trousers': (15, 16),
}

cfg.SCALE_MIN = cfg.CROP_SIZE * cfg.SCALE_MIN_RATE
cfg.SCALE_MAX = cfg.CROP_SIZE * cfg.SCALE_MAX_RATE
cfg.PIXEL_MEAN = np.array(cfg.PIXEL_MEAN, dtype='float32').reshape((3, 1, 1))
cfg.PIXEL_STD = np.array(cfg.PIXEL_STD, dtype='float32').reshape((3, 1, 1))
cfg.FILL_VALUE = [int(v*255) for v in cfg.PIXEL_MEAN.flatten()[::-1]]  # BGR for opencv


cfg.LANDMARK_REF = {
    'blouse': '224.0,78.0:285.0,75.0:254.0,92.0:150.0,126.0:354.0,124.0:162.0,201.0:347.0,200.0:132.0,450.0:100.0,446.0:378.0,449.0:406.0,444.0:170.0,449.0:348.0,443.0:|270.0,176.0:352.0,175.0:295.0,216.0:241.0,184.0:392.0,189.0:219.0,278.0:357.0,271.0:251.0,150.0:228.0,122.0:273.0,232.0:303.0,208.0:213.0,353.0:354.0,374.0:|184.0,68.0:300.0,63.0:244.0,111.0:131.0,103.0:355.0,86.0:165.0,164.0:325.0,155.0:45.0,430.0:25.0,407.0:454.0,410.0:477.0,390.0:190.0,425.0:326.0,425.0:|',
    'skirt': '221.0,200.0:290.0,196.0:150.0,408.0:352.0,423.0:|237.0,214.0:303.0,227.0:97.0,414.0:375.0,466.0:|211.0,150.0:297.0,154.0:188.0,385.0:297.0,390.0:|',
    'outwear': '246.0,90.0:280.0,89.0:203.0,108.0:322.0,112.0:209.0,180.0:308.0,187.0:209.0,234.0:307.0,237.0:194.0,307.0:163.0,308.0:305.0,267.0:321.0,293.0:166.0,483.0:336.0,488.0:|175.0,209.0:199.0,202.0:158.0,217.0:230.0,217.0:157.0,262.0:215.0,249.0:158.0,276.0:208.0,281.0:144.0,339.0:126.0,336.0:198.0,339.0:224.0,348.0:111.0,422.0:232.0,447.0:|227.0,71.0:254.0,78.0:196.0,82.0:277.0,88.0:188.0,121.0:267.0,126.0:192.0,168.0:256.0,169.0:154.0,88.0:135.0,84.0:327.0,224.0:339.0,217.0:157.0,420.0:342.0,404.0:|',
    'dress': '220.0,113.0:301.0,109.0:269.0,160.0:194.0,122.0:328.0,122.0:219.0,177.0:309.0,175.0:218.0,256.0:310.0,258.0:301.0,225.0:297.0,248.0:343.0,263.0:354.0,245.0:235.0,485.0:299.0,490.0:|199.0,33.0:284.0,30.0:245.0,49.0:158.0,42.0:330.0,39.0:176.0,112.0:327.0,117.0:181.0,198.0:290.0,200.0:169.0,222.0:133.0,227.0:381.0,145.0:416.0,167.0:133.0,431.0:355.0,415.0:|221.0,39.0:290.0,41.0:257.0,51.0:185.0,54.0:330.0,50.0:201.0,101.0:312.0,100.0:207.0,183.0:309.0,179.0:185.0,298.0:164.0,297.0:330.0,298.0:349.0,297.0:207.0,495.0:309.0,493.0:|',
    'trousers': '112.0,70.0:395.0,70.0:250.0,351.0:263.0,413.0:40.0,372.0:265.0,406.0:476.0,370.0:|149.0,40.0:363.0,44.0:241.0,219.0:235.0,328.0:100.0,287.0:238.0,328.0:408.0,290.0:|162.0,214.0:228.0,237.0:172.0,278.0:79.0,411.0:114.0,427.0:171.0,427.0:205.0,433.0:|',
}

for category in cfg.LANDMARK_REF:
    refs = []
    landmard_idx = cfg.LANDMARK_IDX[category]
    for ref in cfg.LANDMARK_REF[category].split('|')[:-1]:
        ps = []
        for p in ref.split(':')[:-1]:
            x, y = p.split(',')
            x, y = float(x), float(y)
            ps.append([x, y])
        tmp = np.ones((cfg.NUM_LANDMARK, 2))
        tmp[:] = -1
        tmp[landmard_idx] = np.array(ps)
        refs.append(tmp)
    cfg.LANDMARK_REF[category] = refs
