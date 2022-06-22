# Real-time Inference for Wav2Vec-Ksponspeech
# Author : Taehyoung Kim

import torch
import torch.nn as nn
from torch import Tensor
import torchaudio
import numpy as np
import librosa
from jaso import jaso
import warnings
warnings.filterwarnings('ignore')

from GetSpeech import get_speech
from transformers import Wav2Vec2CTCTokenizer, Wav2Vec2FeatureExtractor, Wav2Vec2Processor,  Wav2Vec2ForCTC

print('음성인식 모델 준비중 ... ')
processor = Wav2Vec2Processor.from_pretrained("Taeham/wav2vec2-ksponspeech")
model = Wav2Vec2ForCTC.from_pretrained("Taeham/wav2vec2-ksponspeech").to('cuda')

# Get Speech data
audiodata = get_speech()
wav_data = librosa.util.buf_to_float(audiodata)

tmp = processor(wav_data, sampling_rate = 16000, return_tensors='pt', padding=True)
input_values = tmp.input_values.to('cuda')
with torch.no_grad():
    logits = model(input_values.type(torch.cuda.FloatTensor)).logits
predicted_ids = torch.argmax(logits, dim=-1)
pred = processor.batch_decode(predicted_ids)

print('Predicted : ', jaso().to_sentence(''.join(pred)))


