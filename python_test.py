from tqdm import tqdm
lt=range(100)
for i,item in enumerate(tqdm(lt)):
    print(i, item)
    if i > 10:
        exit()