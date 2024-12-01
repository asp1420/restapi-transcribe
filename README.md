# REST-API Transcribe

REST API application. Its purpose is to provide a service through an endpoint that retrieves the value of audio transcription to text. The transcription model used is [Whisper](https://github.com/openai/whisper) from OpenAI.

The project is built to be installed with docker.

> This API currently runs on CPU only, but you can modify it to support CUDA.

## 🛠️ Installation and Execution

To install the application, follow these steps:

1. Clone and access the project.

```bash
git clone git@github.com:asp1420/restapi-transcribe.git
cd restapi-transcribe
```

2. Download the weights file and place it in the `transcribe/app/weights/` directory. The available weight files are:

<center>

|**Size**|**Parameters**|
|:-:|:-:|
|[`tiny.en`](https://openaipublic.azureedge.net/main/whisper/models/d3dd57d32accea0b295c96e26691aa14d8822fac7d9d27d5dc00b4ca2826dd03/tiny.en.pt)|39 M|
|[`tiny`](https://openaipublic.azureedge.net/main/whisper/models/65147644a518d12f04e32d6f3b26facc3f8dd46e5390956a9424a650c0ce22b9/tiny.pt)|39 M|
|[`base.en`](https://openaipublic.azureedge.net/main/whisper/models/25a8566e1d0c1e2231d1c762132cd20e0f96a85d16145c3a00adf5d1ac670ead/base.en.pt)|74 M|
|[`base`](https://openaipublic.azureedge.net/main/whisper/models/ed3a0b6b1c0edf879ad9b11b1af5a0e6ab5db9205f891f668f8b0e6c6326e34e/base.pt)|74 M|
|[`small.en`](https://openaipublic.azureedge.net/main/whisper/models/f953ad0fd29cacd07d5a9eda5624af0f6bcf2258be67c92b79389873d91e0872/small.en.pt)|244 M|
|[`small`](https://openaipublic.azureedge.net/main/whisper/models/9ecf779972d90ba49c06d968637d720dd632c55bbf19d441fb42bf17a411e794/small.pt)|244 M|
|[`medium.en`](https://openaipublic.azureedge.net/main/whisper/models/d7440d1dc186f76616474e0ff0b3b6b879abc9d1a4926b7adfa41db2d497ab4f/medium.en.pt)|769 M|
|[`medium`](https://openaipublic.azureedge.net/main/whisper/models/345ae4da62f9b3d59415adc60127b97c714f32e89e936602e85993674d08dcb1/medium.pt)|769 M|
|[`large`](https://openaipublic.azureedge.net/main/whisper/models/e4b87e7e0bf463eb8e6956e646f1e277e901512310def2c24bf0e11bd3c28e9a/large.pt)|1550 M|

</center>

3. Set the `MODEL_NAME` variable in the `.env` file to the name of the weights file.

4. Build the image.

```bash
docker build -t [image name] transcribe/
```

5. Create the container.

```bash
docker run --env-file transcribe/.env -d --name [container name] [image name]
```

## 🗂️ Documentation

The documentation for the endpoint can be found once the application is running, so it is necessary to follow these steps:

1. Run the container.
2. Obtain the container's IP address.

```bash
docker inspect [container name] | grep IPAddress
```
3. Access the documentation through a web browser.
> General documentation: `http://[IP]:8080/docs` and endpoint documentation: `http://[IP]:8080/redoc`.

## ⚙️ Usage

To use the application, you can utilize curl.

```bash
curl -X 'POST' \
  'http://[IP]:8080/api/transcribe' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'audio=@[audio file name];type=[video|audio]/[format]'
```

> Remember to replace the IP and the name of the audio file to be processed.
