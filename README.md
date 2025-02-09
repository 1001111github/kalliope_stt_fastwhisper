# FastWhisper STT
Faster-Whisper STT Engine for Kalliope, see details at [here](https://github.com/SYSTRAN/faster-whisper)

## Installation
```bash
kalliope install --git-url https://github.com/github10011111/kalliope_stt_fastwhisper.git
```

## Parameters

| parameter    | required | type    | default | choices                     | comment                                                                                          |
|--------------|----------|---------|---------|-----------------------------|----------------------------|
| language     | No       | string  |'English'|                             | 
| model        | No       | string  |'base'   |'tiny','base','small','large'| Model size, resource needs

## Example settings

```yaml
# This is the trigger engine that will catch your magic work to wake up Kalliope.

default_trigger: "fastwhisper"

# Trigger engine configuration
triggers:
  - fastwhisper:
      language: "English"
      engine: "small"
```

## Available Openwakeword wake words
To install the default Openwakeword models:
In python:
```
  import openwakeword
  from openwakeword.model import Model
  openwakeword.utils.download_models()
```

There are some available wake words [here](https://github.com/fwartner/home-assistant-wakewords-collection). 
You need the wake_word.[tflite|onnx] file and the wake_word.[tflite|onnx].json file, both need to be in the same directory. 
You will have to rename the wake_word_wake_word.[tflite|onnx].json file to wake_word.[tflite|onnx].json

## Note

You have to add the path to the trigger folder in your settings.
E.g.:
```
# ---------------------------
# resource directory path
# ---------------------------
resource_directory:
  trigger: "resources/trigger"
  neuron: "resources/neurons"
  stt: "resources/stt"
  tts: "resources/tts"
```
