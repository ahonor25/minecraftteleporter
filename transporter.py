import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
mc.postToChat("Transport Anywhere!!!")
mc.postToChat("Thanks for using The Transporter. Made with Python 3n IDLE")
mc.postToChat("Made by the official TecApart YouTube Channel!")
mc.postToChat("Remember to like this Git")
mc.postToChat("When 2nd transporter is created please go to the location the frist one was located. If you destroy the 2nd one... you can still use the transporter.")
time.sleep(5)
transporter1 = mc.player.getTilePos()
mc.setBlock(transporter1.x, transporter1.y - 1,
  transporter1.z, block.DIAMOND_BLOCK)
mc.postToChat("1st Transporter Created")
time.sleep(2)
mc.postToChat("Find a new location within 30 seconds!!!")
time.sleep(30)


transporter2 = mc.player.getTilePos()
mc.setBlock(transporter2.x, transporter2.y -1,
  transporter2.z, block.DIAMOND_BLOCK)
mc.postToChat("2nd transporter created!!!")
time.sleep(2)
while True:
  time.sleep(1)
  pos = mc.player.getTilePos()

  if(pos.x == transporter1.x) and (pos.y == 
    transporter1.y) and (pos.z == transporter1.z):
        mc.player.setPos(transporter2.x, transporter2.y,
          transporter2.z)
  if(pos.x == transporter1.x) and (pos.y == 
        transporter2.y) and (pos.z == transporter2.z):
            mc.player.setPos(transporter1.x, transporter1.y,
              transporter1.z)
mc.postToChat("Thanks for using The Transporter. Made with Python 3n IDLE")
mc.postToChat("Made by the official TecApart YouTube Channel!")
mc.postToChat("Remember to like this Git")
        

