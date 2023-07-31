vg_annotation_file = './vg_annotation.json'
with open(vg_annotation_file, "rb") as f:
    names = json.load(f)

evaluation_set_file = './evaluation_set.json'
with open(evaluation_set_file, "rb") as f:
    datas = json.load(f)

ids = []
num = 0
for data in tqdm(datas):
    image_id = data['image_id']
    boxs = names[image_id]
    path_o = './' + str(image_id) + '.txt'
    file_o = open(path_o, "w")
    L = ["Given an image with following information: bounding box, positions that are the object left-top corner coordinates(X, Y), object sizes(Width, Height). Highly overlapping bounding boxes may refer to the same object.\n\n"]
    L.append('bounding box:\n')
    for box in boxs:
        L.append(box['caption'] + ' X:' + str(box['bbox'][0]) + ' Y:' + str(box['bbox'][1]) + ' Width:' + str(
            box['bbox'][2]) + ' Height:' + str(box['bbox'][2]) + '\n')
    L.append('\n\n')
    L.append('Here is the instruction for the image:\n')
    L.append(data['instruction'] +'\n\n')

    #The following two are sample answers from different models, one answer from each model. I mean you can evaluate several answers for the same image and instruction in one prompt.
    answer_sample1 = 'answer sample1'
    answer_sample2 = 'answer sample2'
  
    L.append('Answer1: ' + answer_sample1 + '\n')
    L.append('Answer2: ' + answer_sample2 + '\n\n')
    L.append('Suppose you are a smart teacher, after looking at the image information above, please score the above answers(0-10) according to the following criteria:\n')
    L.append('1: whether the response directly follows the instruction.\n')
    L.append('2: whether the response is accurate concerning the image content.\n\n')
    L.append('Output format:\n\n'
             'Relevancy:\nscore of the answer1:\nreason:\nscore of the answer2:\nreason:\n\n')
    L.append('Accuracy:\nscore of the answer1:\nreason:\nscore of the answer2:\nreason:\n\n')

    file_o.writelines(L)
    file_o.close()
