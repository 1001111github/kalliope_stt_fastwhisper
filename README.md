# FastWhisper STT
Faster-Whisper STT Engine for Kalliope, see details at [here](https://github.com/SYSTRAN/faster-whisper)

## Installation
```bash
kalliope install --git-url https://github.com/1001111github/kalliope_stt_fastwhisper.git
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
