import matplotlib.pyplot as plt
import cv2

################################## LINE GRAPHIC

xplot = [1,2,3,4,5,6]
yplot = [1,2,3,4,5,6]

plt.title("Line Graphic")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.plot(xplot, yplot)
plt.show()

################################## BARS GRAPHIC

xbar_1 = [1,3,5,7,9]
ybar_1 = [1,3,5,7,9]

xbar_2 = [0,2,4,6,8]
ybar_2 = [0,2,4,6,8]

plt.title("Bars Graphic")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.bar(xbar_1, ybar_1)
plt.bar(xbar_2, ybar_2)
plt.show()

################################## DOTS GRAPHIC

xscatter = [1,2,3,4,5,6]
yscatter = [1,2,3,4,5,6]

plt.title("Dots Graphic")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.scatter(xscatter, yscatter)
plt.show()

################################## DOTS AND LINE GRAPHIC WITH LEGEND

xscatter_linear = [1,2,3,4,5,6]
yscatter_linear = [1,2,3,4,5,6]
each_dot_size = [25,50,75,100,125,150]

plt.title("Dots and Line Graphic")
plt.xlabel("x Axis")
plt.ylabel("Y Axis")
plt.scatter(xscatter_linear, yscatter_linear, label="Dot", color="red", marker="^", s=each_dot_size)
plt.plot(xscatter_linear, yscatter_linear, label="Line", color="black", linestyle="--")
plt.legend()
plt.show()

################################## SAVING IMAGES

# plt.savefig("generic_name.pdf", dpi=300)

################################## DISPLAYING IMAGE

img = cv2.imread("image_1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()

################################## DISPLAYING MULITPLE IMAGES

first_image = "image_1.jpg"
second_image = "image_2.jpg"

plt.subplot(1,2,1) 
img_1 = cv2.imread(first_image)
img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
plt.imshow(img_1)
plt.xticks([])
plt.yticks([])

plt.subplot(1,2,2) 
img_2 = cv2.imread(second_image)
img_2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB)
plt.imshow(img_2)
plt.xticks([])
plt.yticks([])

plt.show()

################################## END