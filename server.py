from flask import Flask
import smp
import socket
import sys
import M2Crypto
app = Flask(__name__)

# mocked data of second person
def mockedVerification(id):
  # mocked identifier of bob's position (for presentation purpose)
  bobId = 5

  aliceSmp = smp.SMP(id)
  bobSmp = smp.SMP(bobId)

  aliceBuffer = aliceSmp.step1()
  bobBuffer = bobSmp.step2(aliceBuffer)
  aliceBuffer = aliceSmp.step3(bobBuffer)
  bobBuffer = bobSmp.step4(aliceBuffer)
  aliceSmp.step5(bobBuffer)

  return aliceSmp.match

@app.route("/<id>")
def verify(id):
  return mockedVerification(id)

if __name__ == "__main__":
  app.run()