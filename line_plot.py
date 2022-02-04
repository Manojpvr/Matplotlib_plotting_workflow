import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
matplotlib.rcParams['mathtext.fontset'] = 'cm'
text_size = 30
tick_r = 0.8 #text size reduction for ticks
plt_xmin = xmin
plt_xmax = xmax
plt.rcParams["font.family"] = "Times New Roman"
plt.figure(figsize=(10, 8), dpi=80)
plt.grid(linestyle = 'dotted')
plt.margins(0.01,0.1)
tick_width = tick_width
xts = np.arange(plt_xmin,plt_xmax,tick_width)
plt.xlabel('Position(m)',fontsize = text_size)
plt.ylabel('Packing fraction',fontsize = text_size)
plt.plot(x1,y1, color = 'blue', linewidth = 2,markevery = 3,markersize = 10, alpha = 1)
plt.plot(x2,y2,color = 'green',linewidth = 2.5,markevery = 3,markersize = 10, alpha = 0.5)
plt.legend(['y1_plot_legend','y2_plot_legend'], fontsize = text_size)
plt.xticks(xts,fontsize=tick_r*text_size)
plt.yticks(fontsize=tick_r*text_size)
plt.savefig("plot_file.pdf", dpi=600, pad_inches = 0, bbox_inches='tight')
