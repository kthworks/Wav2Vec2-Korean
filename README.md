# Wav2Vec2-Korean

---

## 1. Introduction

본 프로젝트는 **Wav2Vec2-xlsr-53 모델을 기반으로 실시간 한국어 음성인식 기능을 제공**합니다.

Wav2Vec2-xlsr-53 모델은 facebook에서 2020년에 개발한 [Wav2Vec 2.0](https://arxiv.org/abs/2006.11477)모델의 Pre-trained model 중 하나로, 총 53개의 언어를 사용하여 학습한 거대한 모델입니다.

해당 모델은 한국어 데이터에 대한 학습이 진행되지 않았기에 한국어 데이터셋을 이용하여 Transfer learning을 진행했습니다. 한국어 데이터셋은 KosponSpeech dataset을 사용했으며 [AI HUB](https://aihub.or.kr/)에서 무료로 제공 받을 수 있습니다.

KsponSpeech dataset의 transcription 과정은 [sooftware](https://github.com/sooftware)님께서 공유해주신 [Kospeech](https://github.com/sooftware/kospeech) 오픈소스에 포함된 코드가 있으니, 참고하시길 바랍니다.

더욱 자세한 내용은 제 [Huggingface repository](https://huggingface.co/Taeham/wav2vec2-ksponspeech)를 방문해주시면 확인하실 수 있습니다 :)

사용목적에 따라 몇몇 후처리를 추가하시면 더욱 정확한 인식 결과를 얻으실 수 있습니다.
- 숫자 / 문자 표기 통일 (예: 21 or 이십일)
- 인식결과에 특수문자 반영여부 통일 (. , ? 등)
- 존재하지 않는 단어는 비슷한 단어로 확률적으로 치환 (예: 다림이 -> 다리미)

## 2. Training Info

**Model**: WavVec2-xlsr-53 (Pre-trained model)  

**Hardware Specification**  
GPU : RTX 3080ti  
CPU : intel i9-12900k  
RAM : 32GB

**Data**
총 4만개의 데이터를 2만개씩 분할하여 순차적으로 학습했습니다.

[Train1](https://huggingface.co/datasets/Taeham/wav2vec2-ksponspeech-train): (1 ~ 20000th data in Ksponspeech)  
[Train2](https://huggingface.co/datasets/Taeham/wav2vec2-ksponspeech-train2): (20100 ~ 40100th data in Ksponspeech)  
[Validation](https://huggingface.co/datasets/Taeham/wav2vec2-ksponspeech-test): (20000 ~ 20100th data in Ksponspeech)   
[Test](https://huggingface.co/datasets/Taeham/wav2vec2-ksponspeech-test): (60000 ~ 60100th data in Ksponspeech)  

**Hyperparameter**
learning_rate: 0.0003  
train_batch_size: 4  
eval_batch_size: 4  
seed: 42  
optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08  
lr_scheduler_type: linear  
lr_scheduler_warmup_steps: 500  
num_epochs: 30  

## 3. How to use?

### Prerequisites
Numpy: ```pip install numpy```  
Pytorch (ver = 1.11.0): You can install from [here](https://pytorch.org/get-started/locally/) to suit your environment. (Also CUDA is required)      
Torchaudio: ```pip install torchaudio```  
Matplotlib: ```pip install matplotlib```  
Librosa: ```conda install -c conda-forge librosa```  
Speech_recognition: ```conda install -c conda-forge speechrecognition```  
pyaudio: ```conda install -c conda-forge PyAudio```  
transformers (ver = 4.19.4): ```pip install transformers```  
Datasets (ver = 2.2.2): ```pip install datasets```  

이곳에 기재되지 않은 라이브러리 이외에 추가적으로 라이브러리가 필요하다는 경고문이 보인다면 해당 라이브러리를 추가로 설치해주시기 바랍니다.

* 본 프로젝트를 위한 별도의 가상환경을 생성하신 후에 위의 라이브러리들을 설치하시길 권장드립니다.  
또한, CUDA가 사용가능한 상태여야 inference를 할 수 있습니다.

### Inference with pretrained Model
1. Code > Download Zip 를 통해 본 프로젝트를 다운받아주시기 바랍니다.

2. 가상환경에서 본 프로젝트가 다운로드 된 경로로 이동해주세요.

* Command
```
$ python ./infernece_main.py
```

* Output
```
소음 수치 반영하여 음성을 청취합니다. 58.945561915793384
목소리를 들을 준비가 되었습니다. 말씀해주세요 :)
```  
위 문장이 보이면 마이크를 통해 말씀해주시면 됩니다.  
음성이 수집된 이후 곧바로 인식된 결과가 제공됩니다.

```
음성인식 결과가 제공됩니다.
```

* Jupyter notebook을 통해 inference.ipynb 파일을 이용하시면 더욱 편리하게 inference를 해보실 수 있습니다.
## 4. Troubleshoots and Contributing

본 프로젝트와 관련한 이슈나 문의 사항이 있다면 아래를 통해 연락주시면 감사하겠습니다.

Author: Taehyoung Kim @kthworks  
Author e-mail: kthwork9934@gmail.com
