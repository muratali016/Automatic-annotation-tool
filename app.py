import torch
import numpy as np
import cv2
import os
import time
import numpy as np
from skimage import io
import time
from glob import glob
from tqdm import tqdm
import torch, gc
import torch.nn as nn
from torch.autograd import Variable
import torch.optim as optim
import torch.nn.functional as F
from torchvision.transforms.functional import normalize
import warnings
warnings.filterwarnings("ignore")
from models import *
from tkinter import Tk, Label, Button
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import tkinter as tk
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

my_w = tk.Tk()
my_w.geometry("450x450")  # Size of the window
my_w.title('AI Photo editor')
my_font1=('times', 18, 'bold')
l1 = tk.Label(my_w,text='AI Photo editor',width=30,font=my_font1)
l1.grid(row=1,column=1,columnspan=4)
b1 = tk.Button(my_w, text='Upload your image',
   width=20,command = lambda:upload_file())
b1.grid(row=2,column=1,columnspan=4)


def annotator_tool():
    print("----------------------------")

    # sourcing the input image
    img = cv2.imread("results/maskk.png")
    img_copy = img.copy()
    img = cv2.resize(img, (450, 300), 1, 1, cv2.INTER_NEAREST)

    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)
    imgCanny = cv2.Canny(imgBlur, 255, 195)

    kernel = np.ones((2, 2))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=3)
    imgThre = cv2.erode(imgDil, kernel, iterations=3)
    locations, hierarchy = cv2.findContours(imgDil, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    org_img = cv2.imread("results/original.png")
    org_img = cv2.resize(org_img, (450, 300))
    for i in (locations):
        print(i)
        a = cv2.drawContours(org_img, locations, -1, (0, 255, 0), 2)
        cv2.imshow("annotations", a)

    cv2.waitKey(2)

def show():
    -
    -
    -
    Private code
    -
    -
    -
        show()
        annotator_tool()




my_w.mainloop()
