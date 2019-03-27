import numpy as np
import  matplotlib.pyplot as plt
#x=np.array([1,2,3,4])

#plt.plot(x,x,label='chart')
#plt.legend()
#plt.show()
fig=plt.figure()
ax=fig.add_subplot(121)
ax.set(title="a chart",xlabel="x",ylabel="y")

ax2=fig.add_subplot(122)
ax.scatter(np.linspace(0,1,5),np.linspace(0,5,5))
ax2.scatter(np.linspace(0,1,5),np.linspace(0,5,5))
#plt.show()
#plt.savefig("my_chart.png")
from matplotlib.backends.backend_pdf import PdfPages
ax.set_xlim(1,3)
#pp=PdfPages("my_chart.pdf")
#pp.savefig()
#pp.close()
plt.title("new plot")
plt.show()
