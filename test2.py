import requests

chunk_size = 1024

url = 'https://fastcamp.video.kr.kollus.com/kr/media-file.mp4?_s=0beaf0a9b657dc52485aeac5c0896321d62ece519d3f5c59f9f8d3e70164472e4c4bf55e5a55fc42e7885f73a3845e55aaa410ad313e0335b7f07af1ade822f544291114e6584c1ec99542dba1931f3082efc90b96e3f2e5fa0391dc18f706e6d6f1f37700e1c2d6b9ee3d0827ecb08ed04c2bd11008568a8a12ab7544141fbf090a65a7d7b183f983a76826be934dec2e04ae49e12f78dff86d9630d9b925a001473dd177d82b818e26811b6cd9edf140a505c774c7e768ef577237797591de4cf53f6465c3aced4675a47df608c882ffa36f011cfad40994dcfd87893e5a0716de8704f17b071e91e8182c28ae7747d27db5bbf85cec92e7207ac1a6f666c90345cecb4ede61b1119fc93be459bbb4f040cbb296b66d5f5994974b9b5e66c579a89ff3106f7a78dfefba94e46481f06c99d16074eccba23277590181120bffb9d6f1bbeb132c8885a92cd25be93f1831544d2aff227cfed974bf9dd60b6679'
r = requests.get(url, stream=True)

with open('hacked.mp4', 'wb') as f:
    for chunk in r.iter_content(chunk_size=chunk_size):
        f.write(chunk)
