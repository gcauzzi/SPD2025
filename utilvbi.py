## quick & dirty routine to make a movie. Sure there are better ways!

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def storeSequence(data, movieName, dpi=500, write=True):
  fig =plt.figure(dpi=300)
  im = plt.imshow(data[0,:,:], cmap='gray', vmax=95000,vmin=10000)
  fig.tight_layout()

  def animate(n):
    im.set_data(data[n,:,:])
    return im


  ani = animation.FuncAnimation(fig, animate, frames=data.shape[0], interval=100)
  
  if write:
    writer = animation.writers['ffmpeg'](fps=10)
    ani.save(movieName, writer=writer, dpi=dpi)
  plt.close(fig)  
  
