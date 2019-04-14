# Image Processing Pipeline Interview Challenge
---

**@author**: Shuiling Yu

- [ ] imagemagic install guide
- [ ] requirements.txt (can be done automatically)
	- [ ] `pip install Augmentor`
- [ ] the time to call imagemagick_resize: python3 main.py -R or when no images are resized
	* `magick: Premature end of JPEG file `/Users/shuilingyu/Downloads/Granular/imgs_de/corn/30812628187_65a340080c_z.jpg' @ warning/jpeg.c/JPEGWarningHandler/396.
magick: Corrupt JPEG data: premature end of data segment `/Users/shuilingyu/Downloads/Granular/imgs_de/corn/30812628187_65a340080c_z.jpg' @ warning/jpeg.c/JPEGWarningHandler/396.`
- [ ] normalization: use CV considering needed to read data again when augementation
- [ ] cv2: read image in b,g,r mode

* further change if necessary: 
	- [ ] CNN size (224, 224, 3) default: to be changed in `utils\resize.py`, convert to grey scale if needed
	- [ ] Image augementation using Keras or Pytorch
	- [ ] Augementation: no noise can be add in Augmentor library, considerint other weather factor(e.g. sunny, snow, rainny)
	- [ ] Train test split