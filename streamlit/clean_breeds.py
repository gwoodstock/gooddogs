import re

def breed_func(x):
    x = x.lower().strip()

    # regex to replace breed names to remain consistent
    x = re.sub('labrador retr\Z', 'labrador retriever', x)
    x = re.sub('germ\sshepherd', 'german shepherd', x)
    x = re.sub('^staffordshire$', 'american staffordshire terrier', x)
    x = re.sub('chihuahua shorthair', 'chihuahua', x)
    x = re.sub('chihuahua longhair', 'chihuahua', x)
    x = re.sub('chihuahua sh', 'chihuahua', x)
    x = re.sub('chihuahua lh', 'chihuahua', x)
    x = re.sub('airedale terr\Z', 'airedale terrier', x)
    x = re.sub('amer ', 'american', x)
    x = re.sub('alask ', 'alaskan', x)
    x = re.sub('am pit bull ter', 'pit bull', x)
    x = re.sub('pitbull', 'pit bull', x)
    x = re.sub('pit bull terrier', 'pit bull', x)
    x = re.sub('aust ', 'australian', x)
    x = re.sub('american bulldog', 'bulldog', x)
    x = re.sub('english bulldog', 'bulldog', x)
    x = re.sub('black/tan hound', 'black and tan coonhound', x)
    x = re.sub('yorkshire terr\Z', 'yorkshire terrier', x)
    x = re.sub('australiancattle dog', 'australian cattle dog', x)
    x = re.sub('anatol shepherd', 'anatolian sheepdog', x)
    x = re.sub('doberman pinsch\Z', 'doberman pinscher', x)
    x = re.sub('poodle min\Z', 'miniature poodle', x)
    x = re.sub('alaskan husky', 'siberian husky', x)
    x = re.sub('\Zhusky', 'siberian husky', x)
    x = re.sub('rat terrier', 'fox terrier', x)
    x = re.sub('wire hair fox terrier', 'fox terrier', x)
    x = re.sub('americanbulldog', 'bulldog', x)
    x = re.sub('australianshepherd', 'australian shepherd', x)
    x = re.sub('dachshund wirehair', 'dachshund', x)
    x = re.sub('american staff\Z', 'pit bull', x)
    x = re.sub('american staffordshire terrier', 'pit bull', x)
    x = re.sub('dachshund longhair', 'dachshund', x)
    x = re.sub('schnauzer min\Z', 'miniature schnauzer', x)
    x = re.sub('flat coat retriever', 'flat-coated retriever', x)
    x = re.sub('collie smooth', 'collie', x)
    x = re.sub('chinese sharpei', 'chinese shar pei', x)
    x = re.sub('shar-pei', 'chinese shar pei', x)
    x = re.sub('queensland heeler', 'australian cattle dog', x)
    x = re.sub('rhod ridgeback', 'rhodesian ridgeback', x)
    x = re.sub('german shorthair pointer', 'german shorthaired pointer', x)
    x = re.sub('manchester terrier', 'standard manchester terrier', x)
    x = re.sub('collie rough', 'collie', x)
    x = re.sub('golden retr\Z', 'golden retriever', x)
    x = re.sub('soft coated wheaten terrier', 'soft-coated wheaten terrier', x)
    x = re.sub('west highland\Z', 'west highland white terrier', x)
    x = re.sub('australian kelpie', 'australian cattle dog', x)
    x = re.sub('redbone hound', 'redbone coonhound', x)
    x = re.sub('eng bulldog', 'bulldog', x)
    x = re.sub('german shepherd dog', 'german shepherd', x)

    return x