# YOLOv5-WTDBB: Wavelet-Enhanced Tiny Object Detection for Maritime UAVs

This is a custom fork of [Ultralytics YOLOv5](https://github.com/ultralytics/yolov5), modified to improve tiny object detection performance in cluttered ocean scenes—particularly for UAV-based maritime monitoring tasks (e.g., SAR, wildlife detection).

## 🔧 Key Modifications

- **WaveBranch Module**: Injected early in the backbone to extract low-level wave features.
- **MultiScaleWaveBranch**: Optional variant with 5×5 and 7×7 Laplacian kernels.
- **DirectionalWaveBranch**: Optional variant with Sobel kernels at multiple orientations.
- **Contrastive Cosine Loss**: Encourages disentanglement between wave clutter and target objects by aligning wave and object features.
- **Modified Forward Pass**: Contrastive loss is injected during training and logged.

## 📂 Directory Overview

- `models/yolo.py`: Contains model forward pass with WaveBranch outputs.
- `models/common.py`: Defines `WaveBranch` and its variants.
- `utils/loss.py`: Defines `contrastive_cos()` loss function.
- `train.py`: Modified training loop to support dual-branch loss.
- `runs/`: Output logs and results.

### Selecting a Wave Branch

Use the `--wave` argument when training to choose which branch to apply. Extra
arguments can be provided as JSON via `--wave-args`.

```bash
python train.py --wave multi --wave-args '{"ksizes": [3,5,7]}'
```
  
## 🧪 Training

```bash
python train.py \
  --data path/to/SeaDronesSee.yaml \
  --weights yolov5s.pt \
  --batch-size 16 \
  --epochs 100 \
  --name wtdbb_experiment
