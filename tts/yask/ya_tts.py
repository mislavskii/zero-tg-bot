import requests


def synthesize(folder_id, iam_token, text):
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
    headers = {
        'Authorization': "Api-Key {}".format(iam_token),
    }

    data = {
        'text': text,
        'lang': 'ru-RU',
        'voice': 'filipp',
        'folderId': folder_id
    }

    with requests.post(url, headers=headers, data=data, stream=True) as resp:
        if resp.status_code != 200:
            raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))

        for chunk in resp.iter_content(chunk_size=None):
            yield chunk


def text2file(folder_id, iam_token, text, output='speech.ogg'):
    with open(output, "wb") as f:
        for audio_content in synthesize(folder_id, iam_token, text):
            f.write(audio_content)
    return True
    