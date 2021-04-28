from percorredor_pastas.percorredor_json import findAnnotatedImagesPath
from alpha_mask.alphamask import createAlphaMask

annotated = findAnnotatedImagesPath('.')

img_id = 0;
for anntd_img in annotated:
	createAlphaMask(anntd_img, img_id)
	img_id += 1
	print(img_id, "of", len(annotated))
print("Done!")